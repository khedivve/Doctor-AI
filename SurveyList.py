from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

patient_queue = ["John Doe", "Jane Smith", "Bob Johnson"]
feedback_data = {}  # Store feedback data in-memory (you may want to use a database for production)

@app.route("/")
def index():
    return render_template("index.html", queue=patient_queue)

@app.route("/survey/<patient_name>", methods=["GET", "POST"])
def survey(patient_name):
    if request.method == "POST":
        feedback = request.form.get("feedback")
        feedback_data[patient_name] = feedback
        return redirect(url_for("index"))

    return render_template("survey.html", patient_name=patient_name)

if __name__ == "__main__":
    app.run(debug=True)
