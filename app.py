from flask import Flask, render_template, request, jsonify
from openai import OpenAI
client = OpenAI()
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        userinput = request.form['content']
        response = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": "Ты сленг ассистент, твоя задача выяснить есть ли сленг в заданном предложении. Если да то перефразировать предложение без сленга понятным языком, дополнительно тебе нужно обьяснит что это за слово, коротко."},
            {"role": "user", "content": userinput}
        ]
        )   
        return jsonify({'response': response.choices[0].message.content})
        
    else:
        pass

    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)
