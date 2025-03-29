import os
import webbrowser
import psutil
import subprocess
import platform

class SystemFunctions:
    @staticmethod
    def open_chrome():
        """Open Google Chrome"""
        if platform.system() == 'Darwin':  # macOS
            subprocess.Popen(['open', '-a', 'Google Chrome'])
        elif platform.system() == 'Windows':
            os.startfile('chrome')
        else:  # Linux and other Unix
            subprocess.Popen(['google-chrome'])

    @staticmethod
    def open_calculator():
        """Open system calculator"""
        if platform.system() == 'Windows':
            os.system('calc')
        elif platform.system() == 'Darwin':  # macOS
            subprocess.Popen(['open', '-a', 'Calculator'])
        else:  # Linux
            subprocess.Popen(['gnome-calculator'])

    @staticmethod
    def open_notepad():
        """Open Notepad"""
        if platform.system() == 'Windows':
            os.system('notepad')
        elif platform.system() == 'Darwin':  # macOS
            subprocess.Popen(['open', '-a', 'TextEdit'])
        else:  # Linux
            subprocess.Popen(['gedit'])

    @staticmethod
    def get_system_info():
        """Retrieve system information"""
        return {
            'cpu_usage': psutil.cpu_percent(),
            'memory_usage': psutil.virtual_memory().percent,
            'total_memory': f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
            'available_memory': f"{psutil.virtual_memory().available / (1024**3):.2f} GB",
            'operating_system': platform.platform()
        }

    @staticmethod
    def run_shell_command(command):
        """Execute a shell command"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return {
                'stdout': result.stdout,
                'stderr': result.stderr,
                'return_code': result.returncode
            }
        except Exception as e:
            return {'error': str(e)}