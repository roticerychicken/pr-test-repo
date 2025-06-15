import subprocess
import pickle

def run_command(user_input):
    # 🚩 Insecure use of subprocess with shell=True
    subprocess.call(user_input, shell=True)

def deserialize_data(data):
    # 🚩 Insecure use of pickle.loads on untrusted input
    return pickle.loads(data)