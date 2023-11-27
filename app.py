from flask import Flask, render_template

app = Flask(__name__)

# Initialize the queue with an example list of patient names
patient_queue = ["John Doe", "Jane Smith", "Bob Johnson"]

@app.route("/")
def index():
    return render_template("index.html", queue=patient_queue)

if __name__ == "__main__":
    app.run(debug=True)
