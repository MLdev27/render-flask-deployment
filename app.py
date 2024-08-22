from flask import Flask, jsonify, request
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import random

app = Flask(__name__)


queries = [
    "Show me attendance of 'Employee X' for last 3 months",
    "Which employee did maximum production",
    "What has been my average purchase price from 'Supplier Y'",
    "Which customers faced a delay in order last week?",
    "What is my cashflow statement for upcoming 6 months",
    "What is my Revenue per employee",
    "Who are my Top 5 customers",
    "What is my margin with 'Customer X'",
    "What is my daily attendance",
    "How many goods are in production today",
    "How many dispatches today",
    "What is my production schedule for this week/day?",
    "What is status of 'Lot no'/'Article name'",
    "How many goods of 'Lot no' are remaining?",
    "When was the 'Process y' of 'Article X' completed and by whom"
]


# Path to your service account key file
SERVICE_ACCOUNT_FILE = 'credential1_service.json'

# The audience for which the token is requested
AUDIENCE = 'https://us-central1-cobalt-alcove-395208.cloudfunctions.net/Analysis_bot-1'  

# The scope for which the token is requested
SCOPES = ['https://www.googleapis.com/auth/cloud-platform']

def get_bearer_token():
    credentials = service_account.IDTokenCredentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        target_audience=AUDIENCE
    )

    # Refresh the token
    request_obj = Request()
    credentials.refresh(request_obj)

    return credentials.token

@app.route('/get-token', methods=['GET'])
def get_token():
    try:
        token = get_bearer_token()
        return jsonify({'access_token': token}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    # Randomly select 4 queries from the predefined list
    recommendations = random.sample(queries, 4)
    return jsonify({"Query": recommendations})

if __name__ == '__main__':
    app.run(port=8080)
