from code_generator.dynamic_code_generator import DynamicCodeGenerator

# Generate execution script
code = DynamicCodeGenerator.generate_execution_script('open_chrome')
print(code)

# Validate the generated code
is_valid = DynamicCodeGenerator.validate_generated_code(code)
print("Code is valid:", is_valid)