import json

def load_user_data():
    with open('data/users_data.json', 'r') as file:
        return json.load(file)

def get_balance(customer_id):
    data = load_user_data()
    for user in data:
        if user['customer_id'] == customer_id:
            return user['balance']
    return None

def check_outage(customer_id):
    data = load_user_data()
    for user in data:
        if user['customer_id'] == customer_id:
            return user['outage']
    return None
