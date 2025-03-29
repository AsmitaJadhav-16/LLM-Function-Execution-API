from automation_functions.system_functions import SystemFunctions

def main():
    print("=== System Functions Test ===")
    
    # Get system information
    system_info = SystemFunctions.get_system_info()
    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()