import os # Para utilizar la API KEY de google

# Importaciones de langchain para estructura y carga de datos
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

# Importaciones para los modelos de Google (Embeddings y LLM)
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# CONFIGURACION DE LA API KEY PUBLICA (utilizamos una cuenta de prueba)
os.environ["GOOGLE_API_KEY"] = "API_KEY_ACA"

# CARGAR EL MODELO DE EMBEDDINGS
print("\nIniciando el sistema RAG...")
print("Cargando modelo de embeddings de Google...")

# Utilizamos text-embedding-004
try:
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004"
    )
    print("Modelo de embeddings cargado exitosamente")
    print("Modelo activo: text-embedding-004")
except:
    print("Hubo un problema al cargar el modelo de embeddings")