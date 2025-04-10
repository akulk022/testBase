import pickle

#pickle.loads() can execute arbitrary code if the input is malicious. An attacker could craft input that runs any Python code—a major security risk.
def load_user_data(data):
    return pickle.loads(data)

user_input = input("Paste your serialized data: ")
user_data = load_user_data(user_input.encode())
