import os
import json

# SAFE: Fix for insecure deserialization
def load_user_data(data):
    return json.loads(data)

# SAFE: use subprocess without shell=True
def run_command(user_input):
    try:
        # Only allow specific commands if possible, or split safely
        result = subprocess.run(["echo", "Hello", "&&", user_input], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print("Error running command:", e)

# USAGE
if __name__ == "__main__":
    user_data_input = input("Paste your serialized data (JSON): ")
    user_data = load_user_data(user_data_input)
    
    command_input = input("Enter command to run: ")
    run_command(command_input)
