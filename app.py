from flask import Flask, render_template, request
import openai

openai.api_key = "API HERE"
# Contexto del asistente 
context = {"role":"system",
           "content": "Eres un asistente muy útil."}
messages = [context]

def chatgpt_response(msg):
    messages.append({"role":"user","content":msg})
    response = openai.ChatCompletion.create( model = "gpt-3.5-turbo",messages = messages)
    response_content = response.choices[0].message.content
    messages.append({"role":"assistant","content":response_content})
    
    return response_content
app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatgpt_response(userText)

if __name__ == "__main__":
    app.run()