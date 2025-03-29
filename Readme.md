Here's an enhanced, more attractive version of your **README.md** with a professional and visually appealing structure. It also includes placeholders where you can insert your Postman screenshots.  

---

# **🚀 LLM + RAG-Based Function Execution API**  

## **🌟 Project Overview**  
This project implements an advanced **Function Execution API** that leverages **LLM-based prompt understanding** and **RAG (Retrieval-Augmented Generation)** to dynamically execute predefined system automation tasks.  
It takes natural language user prompts, performs **semantic search** in a **vector database (FAISS)**, and generates Python code dynamically for executing the relevant function.

---

## **🔧 Features**  
- 💡 **Function Retrieval**: Search and retrieve the most relevant system function based on user queries.  
- 🧠 **Semantic Search with SentenceTransformer**: User queries are embedded and compared with stored function descriptions for matching.  
- 🛠 **Dynamic Python Code Generator**: Creates Python scripts on the fly to execute the retrieved function.  
- ⚡ **FastAPI Integration**: Provides a simple API endpoint to interact with the function execution system.  

---

## **📁 Directory Structure**  

```
project-root/
│
├── automation_functions/
│   └── system_functions.py         # Contains predefined system automation functions
│
├── vector_database/
│   └── function_retrieval.py       # FAISS-based vector search logic
│
├── code_generator/
│   └── dynamic_code_generator.py   # Python code generator for executing functions
│
├── api/
│   └── function_executor.py        # FastAPI code to handle incoming requests and execute logic
│
├── main.py                         # Entry point to run the FastAPI server
├── requirements.txt                # List of dependencies
└── README.md                       # Project documentation (this file)
```

---

## **🚀 API Documentation**  
The FastAPI server exposes the following endpoint:  

### **POST /execute**  
- **URL:** `http://127.0.0.1:8000/execute`  
- **Method:** POST  
- **Headers:**  
  - `Content-Type: application/json`  
- **Request Body (JSON)**  
  ```json  
  {  
    "prompt": "Open Chrome browser"  
  }  
  ```  

### **🛠 Sample API Response**  
```json  
{  
  "function": "open_chrome",  
  "code": "Generated Python code for executing the function",  
  "description": "Open Google Chrome browser"  
}  
```  

---

## **📝 How to Set Up and Run Locally**  

Follow these steps to set up and run the API server on your local machine:  

### **Step 1: Clone the Repository**  
```bash  
git clone <repo-url>  
cd <repo-folder>  
```  

### **Step 2: Install Dependencies**  
1. **Create a Virtual Environment (Optional but Recommended)**  
   ```bash  
   python -m venv env  
   source env/bin/activate   # On Linux/MacOS  
   env\Scripts\activate      # On Windows  
   ```  

2. **Install Required Packages**  
   ```bash  
   pip install -r requirements.txt  
   ```  

### **Step 3: Start the FastAPI Server**  
```bash  
python main.py  
```  
You should see output indicating the server is running:  
```
INFO:     Started server process [12345]  
INFO:     Application startup complete.  
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)  
```  

---

## **🚀 Using the API with Postman**  

### **Step 1: Open Postman and Create a New Request**  
1. **Set the Method to POST**  
2. **Enter the URL:** `http://127.0.0.1:8000/execute`  
3. **Go to the Body Tab:**  
   - Select **raw** input.  
   - Choose **JSON** format.  
   - Enter the following request body:  
   ```json  
   {  
     "prompt": "Retrieve system information"  
   }  
   ```  
4. **Click Send**  

---

## **📸 Postman Screenshots (Add These Below)**  

1. **Request Setup Screenshot:**  
   *(Insert a screenshot of your Postman request setup here, with the URL, method, headers, and body visible.)*  

2. **Response Screenshot:**  
   *(Insert a screenshot of the API response here.)*  

---

## **📚 Predefined Functions**  

Here are the functions currently registered in the system:  

| **Function Name**     | **Description**                       | **Category**              |  
|-----------------------|---------------------------------------|---------------------------|  
| `open_chrome`         | Open Google Chrome browser            | Application Control       |  
| `open_calculator`     | Open system calculator                | Application Control       |  
| `open_notepad`        | Open Notepad (text editor)            | Application Control       |  
| `get_system_info`     | Retrieve system performance metrics   | System Monitoring         |  
| `run_shell_command`   | Execute arbitrary shell commands      | Command Execution         |  

---

## **🌐 Tech Stack**  
- **FastAPI**: API framework  
- **Uvicorn**: ASGI server to run FastAPI  
- **SentenceTransformer**: Generates embeddings from user prompts  
- **FAISS**: High-performance similarity search for vector embeddings  
- **psutil**: Provides system performance metrics  

---

## **💡 Future Enhancements**  
- Add more automation functions (e.g., file operations, internet search).  
- Implement session-based tracking to improve prompt understanding over time.  
- Enhance logging, error handling, and API security.  

---

## **📜 License**  
This project is licensed under the **MIT License**.  

---

## **🤝 Contributing**  
We welcome contributions! To contribute:  
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature-branch`).  
3. Commit your changes (`git commit -m "Added a new feature"`).  
4. Push to the branch (`git push origin feature-branch`).  
5. Open a pull request.  

---

