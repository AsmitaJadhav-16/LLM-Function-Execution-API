import ast

class DynamicCodeGenerator:
    @staticmethod
    def generate_execution_script(function_name, function_args=None):
        """
        Generate a dynamic Python script for function execution
        
        :param function_name: Name of the function to execute
        :param function_args: Optional dictionary of arguments
        :return: Generated Python script as a string
        """
        # Convert function arguments to a string representation
        args_str = ', '.join([f"{k}={repr(v)}" for k, v in (function_args or {}).items()])
        
        script_template = f"""
from automation_functions.system_functions import SystemFunctions
def main():
    try:
        # Execute the specified function
        {'result = ' if function_args else ''}SystemFunctions.{function_name}({args_str})
        
        # Print success message or result
        {'print(result)' if function_args else f'print(f"Function {function_name} executed successfully.")'}
    except Exception as e:
        print(f"Error executing function: {{e}}")

if __name__ == "__main__":
    main()
"""
        return script_template.strip()

    @staticmethod
    def validate_generated_code(code):
        """
        Validate the generated Python code
        
        :param code: Python code to validate
        :return: Boolean indicating code validity
        """
        try:
            ast.parse(code)
            return True
        except SyntaxError:
            return False