from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/example', methods=['GET'])
def example():
    user_query = "What is my cashflow statement for upcoming 6 months"
    summary = "The cashflow statement for the upcoming 6 months shows a positive trend with expected inflows exceeding outflows."
    
    return jsonify({"Query": user_query, "result": summary})

if __name__ == '__main__':
    app.run(debug=True)
