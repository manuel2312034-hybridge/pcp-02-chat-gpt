from dotenv import load_dotenv
from flask import Flask, request, jsonify
import os
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return {"message": 'ok'}

@app.route('/prompt', methods=['POST'])
def obtenerDatos():
    input_json = request.get_json(force=True)
    question = input_json['question']
    answer = bot_answer(question)
    response = { 'question': question, 'answer': answer.model_dump(exclude_unset=True)}
    return response


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


def bot_answer(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion


if __name__ == '__main__':
    app.run(debug=True, port=5050)
