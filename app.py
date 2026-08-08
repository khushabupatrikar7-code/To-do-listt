from flask import Flask  ,render_template

app = Flask(__name__)

todos =[
    {"sr no": 1, "title": "Sample task", "desc": "This is a sample task  for to do list", "date_created":"08-08-2026","status": "Pending"}

]

@app.route("/") #decorator
def home():
    return render_template("index.html", allTodos = todos)



if(__name__ == "__main__"):
    app.run(debug=True, port=5000)
