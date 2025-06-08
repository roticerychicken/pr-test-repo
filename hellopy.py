import subprocess

def insecure_function():
    user_input = "ls -la"
    subprocess.call(user_input, shell=True)

if __name__ == "__main__":
    insecure_function()
