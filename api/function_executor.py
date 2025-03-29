from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from vector_database.function_retrieval import FunctionRegistry
from code_generator.dynamic_code_generator import DynamicCodeGenerator

class ExecutionRequest(BaseModel):
    prompt: str
    args: dict = None

app = FastAPI(title="LLM Function Executor")
function_registry = FunctionRegistry()
code_generator = DynamicCodeGenerator()

@app.post("/execute")
async def execute_function(request: ExecutionRequest):
    try:
        # Retrieve matching function
        matched_functions = function_registry.retrieve_function(request.prompt)
        
        if not matched_functions:
            raise HTTPException(status_code=404, detail="No matching function found")
        
        # Take the top match
        function_metadata = matched_functions[0]
        function_name = function_metadata['name']
        
        # Generate execution script
        generated_code = code_generator.generate_execution_script(
            function_name, 
            request.args
        )
        
        # Validate generated code
        if not code_generator.validate_generated_code(generated_code):
            raise HTTPException(status_code=500, detail="Invalid generated code")
        
        return {
            "function": function_name,
            "code": generated_code,
            "description": function_metadata['description']
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))