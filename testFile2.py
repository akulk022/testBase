import json

#This fixes the insecure deserialization vulnerability.
def load_user_data(data):
    return json.loads(data)

user_input = input("Paste your serialized data (JSON): ")
user_data = load_user_data(user_input)