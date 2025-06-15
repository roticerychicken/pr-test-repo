import subprocess
import pickle


# Dangerous use of subprocess
subprocess.call("ls -la", shell=True)

# Dangerous use of pickle
malicious_data = b"cos\nsystem\n(S'echo hacked'\ntR."
pickle.loads(malicious_data)