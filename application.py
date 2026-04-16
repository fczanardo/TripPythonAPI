from flask import Flask, jsonify, request
from langchain_groq import ChatGroq
import os
import logging
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

application = Flask(__name__)
CORS(application)

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise EnvironmentError("GROQ_API_KEY environment variable not set")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=api_key
)

@application.route('/', methods=['GET', 'POST'])
def generate_travel_plan():
    try:
        log.debug("Reading prompt.txt")
        # Read files with UTF-8 encoding to avoid decode errors
        with open("prompt.txt", encoding="utf-8") as f:
            prompt_text = f.read()
        log.debug("prompt.txt loaded (%d chars)", len(prompt_text))

        log.debug("Reading trip.json")
        with open("trip.json", encoding="utf-8") as f:
            trip_data = f.read()
        log.debug("trip.json loaded (%d chars)", len(trip_data))

        # Generate response using LLM
        log.debug("Invoking LLM")
        response = llm.invoke(prompt_text + trip_data)
        log.debug("LLM response received (%d chars)", len(response.content))

        log.debug("Reading template.html")
        with open("template.html", encoding="utf-8") as f:
            html_content = f.read().format(content=response.content)
        log.debug("HTML rendered successfully")

        return html_content, 200
    
    except Exception as e:
        log.exception("Error in generate_travel_plan")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
    
@application.route('/json', methods=['GET', 'POST'])
def generate_travel_plan_json_response():
    try:
        log.debug("[JSON] Reading prompt.txt")
        # Read files with UTF-8 encoding to avoid decode errors
        with open("prompt.txt", encoding="utf-8") as f:
            prompt_text = f.read()
        log.debug("[JSON] prompt.txt loaded (%d chars)", len(prompt_text))

        log.debug("[JSON] Reading trip.json")
        with open("trip.json", encoding="utf-8") as f:
            trip_data = request.data.decode('utf-8')
        log.debug("[JSON] trip.json loaded (%d chars)", len(trip_data))

        # Generate response using LLM
        log.debug("[JSON] Invoking LLM")
        response = llm.invoke(prompt_text + trip_data)
        log.debug("[JSON] LLM response received (%d chars)", len(response.content))
        
        return jsonify(
            response.content
        ), 200
    
    except Exception as e:
        log.exception("[JSON] Error in generate_travel_plan_json_response")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@application.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Local execution
if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=5000)