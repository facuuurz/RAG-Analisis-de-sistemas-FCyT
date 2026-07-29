# Installation and Usage Guide: FCyT Academic Virtual Assistant (RAG)
This document explains, step by step, how someone with no prior knowledge of the project can set it up and run it on their computer from scratch.
## 1. Prerequisites
Before you start, make sure the following is installed on your computer:
1. **Python**: You need Python 3.9 or later. You can download and install it from [python.org](https://www.python.org/downloads/).
   > [!IMPORTANT]
   > During installation on Windows, make sure to check the box that says **"Add Python to PATH"** before clicking "Install Now".
## 2. Project Setup
### Clone or download the project
1. Download this project folder (`RAG-Analisis-de-sistemas-FCyT`) and place it on your desktop or in your documents.
2. Open a terminal (Command Prompt `cmd` or PowerShell) and navigate to the project folder. For example:
   ```bash
   cd path\to\the\folder\RAG-Analisis-de-sistemas-FCyT
   ```
### Create a Virtual Environment (Recommended)
To avoid conflicts with anything else you have installed, it is best to isolate this project.
1. In the terminal, inside the project folder, run:
   ```bash
   python -m venv venv
   ```
2. **Activate the virtual environment**:
   - On Windows (Command Prompt or PowerShell):
     ```bash
     venv\Scripts\activate
     ```
   - *Note: You will know it worked because you will see `(venv)` at the beginning of the line in your terminal.*
## 3. Installing Dependencies
The `requirements.txt` file contains every library needed to run Google's models, work with PDFs, and manage the ChromaDB vector database.
1. With the environment activated, install everything by running:
   ```bash
   pip install -r requirements.txt
   ```
   *(This may take a few minutes)*
## 4. Data Structure
Make sure a folder named `Datos` exists inside the project's root folder, and that the academic PDFs are placed inside it.
## 5. Configure the API Key
The system uses the Google Gemini API and reads the key from an environment variable. Get your free key from Google AI Studio and, before running, set it in the terminal:
```bash
# PowerShell (Windows)
$env:GOOGLE_API_KEY = "your-api-key"
```
## 6. Running the System
Once all the previous steps are done, you are ready to start the system:
1. In the terminal (with the `(venv)` environment still activated), run:
   ```bash
   python main.py
   ```
### What happens next?
- **First run (Database creation)**: If it is the first time the program runs, it will read every PDF in the `Datos` folder, split them into chunks, and store them in a new folder called `DB_RAG_3`. You will see messages indicating that it saves "in batches" and pauses between them (to protect the API quota). **Be patient — this process can take several minutes.**
- **Subsequent runs**: If the `DB_RAG_3` folder already exists, the system will skip that step and connect instantly to the stored database.
Done! When the following box appears in the console:
```text
==================================================
 SISTEMA RAG ACTIVO - LISTO PARA PREGUNTAS
 (Escribí 'salir' para terminar el programa)
==================================================
```
You can now type your questions about the courses of the Systems programs at FCyT, and the Virtual Assistant will answer.
