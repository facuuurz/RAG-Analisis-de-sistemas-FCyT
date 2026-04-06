import os # Para utilizar la API KEY de google
import time # Para medir cuánto tarda en responder

# Importaciones de langchain para estructura y carga de datos
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

# Importaciones para los modelos de Google (Embeddings y LLM)
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# CONFIGURACION DE LA API KEY PUBLICA (utilizamos una cuenta de prueba)
os.environ["GOOGLE_API_KEY"] = "AIzaSyAthANhprZ4ruhfvD0xSUu75mUglPYZj2Y"

# CARGAR EL MODELO DE EMBEDDINGS
print("\nIniciando el sistema RAG...")
print("Cargando modelo de embeddings de Google...")

# Utilizamos gemini-embedding-001
try:
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )
    print("Modelo de embeddings cargado exitosamente")
    print("Modelo activo: gemini-embedding-001")
except:
    print("Hubo un problema al cargar el modelo de embeddings")



    # RUTAS DE LAS CARPETAS (Asegurate de que existan)
CARPETA_DATOS = "./Datos"
CARPETA_DB = "./DB_RAG_3"

# 1. CARGA Y FRAGMENTACIÓN (Solo si la BD no existe aún)
if not os.path.exists(CARPETA_DB) or not os.listdir(CARPETA_DB):
    print(f"\nProcesando PDFs desde la carpeta '{CARPETA_DATOS}'...")
    
    # Carga de documentos
    loader = DirectoryLoader(CARPETA_DATOS, glob="./*.pdf", loader_cls=PyPDFLoader)
    documentos = loader.load()
    print(f"Se cargaron {len(documentos)} páginas en total.")

    # Fragmentación (Chunking) según tu TP
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_documents(documentos)
    print(f"Documentos divididos en {len(chunks)} fragmentos.")

    # 2. ALMACENAMIENTO VECTORIAL (ChromaDB)
    print("\nCreando base de datos vectorial en Chroma (guardando por lotes para evitar límites de uso)...")
    vectorstore = Chroma(persist_directory=CARPETA_DB, embedding_function=embeddings)
    
    # Se introduce por lotes muy seguros con pausa obligatoria para la cuota de 100 req/min
    tamanio_lote = 10
    for i in range(0, len(chunks), tamanio_lote):
        lote_chunks = chunks[i:i + tamanio_lote]
        vectorstore.add_documents(lote_chunks)
        print(f"Guardados {i + len(lote_chunks)} de {len(chunks)} fragmentos...")
        time.sleep(8)  # 8 segundos asegura matemáticamente un máximo de 75 peticiones por minuto.
        
    print("\nBase de datos guardada exitosamente.")
else:
    # Si la BD ya existe, la cargamos directamente para ahorrar tiempo y recursos
    print(f"\nCargando base de datos existente desde '{CARPETA_DB}'...")
    vectorstore = Chroma(
        persist_directory=CARPETA_DB,
        embedding_function=embeddings
    )

# 3. CONFIGURACIÓN DEL LLM Y EL PROMPT (Generación)
print("\nIniciando el modelo de lenguaje (Gemini Flash Latest)...")
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0.0 # Se eleva la creatividad al 80%
)


# El "prompt invisible" que mencionaste en tu TP
from langchain_core.prompts import PromptTemplate

template_rag = """Sos un asistente virtual académico de la FCyT. Tu tarea es responder dudas de los alumnos sobre las carreras de Sistemas.
Utilizá ÚNICAMENTE los siguientes fragmentos de contexto para responder a la pregunta.
Si la respuesta no se encuentra en el contexto, respondé exactamente: "No cuento con los conocimientos para generar una respuesta útil sobre ese tema."
No inventes datos, ni fechas, ni correlatividades.

Contexto recuperado:
{context}

Pregunta del usuario: {question}

Respuesta:"""

PROMPT = PromptTemplate(
    template=template_rag, 
    input_variables=["context", "question"]
)

# 4. CREACIÓN DE LA CADENA DE RECUPERACIÓN (Retrieval)
from langchain_classic.chains import RetrievalQA

# k=2 para traer mucha más información de la base de datos
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
    chain_type_kwargs={"prompt": PROMPT},
    return_source_documents=True # Para saber de qué PDF sacó la info
)

# 5. BUCLE INTERACTIVO PARA EVALUAR TUS 18 PREGUNTAS
print("\n" + "="*50)
print(" SISTEMA RAG ACTIVO - LISTO PARA PREGUNTAS ")
print(" (Escribí 'salir' para terminar el programa)")
print("="*50)

while True:
    pregunta_usuario = input("\n- Ingresa tu pregunta: ")
    
    if pregunta_usuario.lower() in ['salir', 'exit', 'quit']:
        print("Cerrando el sistema...")
        break
        
    if not pregunta_usuario.strip():
        continue

    print("Buscando respuesta...")
    inicio = time.time()
    
    # Ejecutamos la consulta
    resultado = qa_chain.invoke({"query": pregunta_usuario})
    
    fin = time.time()
    
    print(f"\nRespuesta: {resultado['result']}")
    print(f"Tiempo de respuesta: {round(fin - inicio, 2)} segundos")
    
    # Pausa de protección para rate limits (Asegura no exceder 15 por minuto)
    time.sleep(4)
    
    # (Opcional) Mostrar de qué documentos sacó la información
    fuentes = set([doc.metadata.get('source', 'Desconocido') for doc in resultado['source_documents']])
    print(f"Fuentes consultadas: {', '.join(fuentes)}")