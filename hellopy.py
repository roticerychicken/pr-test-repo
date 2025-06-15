import subprocess

user_input = "ls -la"
subprocess.call(user_input, shell=True)  # This should trigger a warning
