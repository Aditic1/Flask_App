from flask import Flask, request, jsonify
from functions import process_documents, query_faiss

app = Flask(__name__)

# Load and process documents once
file_path = './brainlox_courses.txt'
db = process_documents(file_path)

@app.route('/query', methods=['POST'])
def query():
    user_input = request.json.get('query')
    
    # Query the FAISS index
    results = query_faiss(db, user_input)
    
    # Format and return the response
    response = {
        'query': user_input,
        'results': [result.page_content for result in results]
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
