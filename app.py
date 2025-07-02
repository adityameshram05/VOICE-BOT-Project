from flask import Flask, render_template, request, jsonify
import wikipedia
import datetime
import webbrowser

app = Flask(__name__)

def process_command(command):
    command = command.lower()

    if 'time' in command:
        now = datetime.datetime.now().strftime('%H:%M:%S')
        return f"The current time is {now}."

    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    elif 'who is' in command or 'what is' in command or 'what are' in command or 'tell me about' in command:
        try:
            summary = wikipedia.summary(command, sentences=2)
            return summary
        except:
            return "Sorry, I couldn't find anything on that."

    else:
        return "Sorry, I don't understand that command yet."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    command = data.get("command")
    if command:
        response = process_command(command)
        return jsonify({"response": response})
    return jsonify({"response": "No command received."})

if __name__ == "__main__":
    app.run(debug=True)
