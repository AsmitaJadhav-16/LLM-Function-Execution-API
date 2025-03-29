from vector_database.function_retrieval import FunctionRegistry

# Initialize the registry
registry = FunctionRegistry()

# Test function retrieval
query = "Open a web browser"
matched_functions = registry.retrieve_function(query)
print(matched_functions)