from flask import Flask, render_template, redirect, url_for, flash
from forms import FeedbackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

feedback_list = []

@app.route("/", methods=["GET", "POST"])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback_list.append({
            "name": form.name.data,
            "email": form.email.data,
            "message": form.message.data
        })
        flash("✅ Feedback submitted successfully!", "success")
        return redirect(url_for("feedback"))
    return render_template("feedback.html", form=form, feedbacks=feedback_list)

if __name__ == "__main__":
    app.run(debug=True)