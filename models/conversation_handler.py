from .chatbot import get_response
from .user_data import get_balance, check_outage
import json

def handle_input(user_input, customer_id):
    # Handle FAQs
    with open('data/faqs.json') as f:
        faqs = json.load(f)
        for faq in faqs:
            if faq['question'].lower() in user_input.lower():
                return faq['answer']
    
    # Handle balance check
    if "balance" in user_input.lower():
        balance = get_balance(customer_id)
        if balance is not None:
            return f"Your current balance is ${balance:.2f}"
        return "Customer not found."
    
    # Handle outage check
    if "outage" in user_input.lower():
        outage_status = check_outage(customer_id)
        if outage_status:
            return "There's an outage in your area."
        return "No outage reported."

    # Default: Use LangChain for AI response
    return get_response(user_input)
