"""Flask site for Balloonicorn's Party."""


from flask import Flask, session, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from model import Game, connect_to_db

app = Flask(__name__)
app.secret_key = "SECRETSECRETSECRET"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("homepage.html")


@app.route("/rsvp", methods=['POST'])
def rsvp():
    """Register for the party."""

    name = request.form.get("name")
    email = request.form.get("email")

    session['RSVP'] = True
    flash("Yay!")
    return redirect("/")


@app.route("/games")
def games():
    games = Game.query.all()

    # session['RSVP'] this will give a key error. Use ".get method" instead.
    # or 
    # if 'RSVP' in session:
    # session object acts like a dictionary
    
    if session.get('RSVP'):
        return render_template("games.html", games=games)
    else:
        flash("You need to first RSVP to get to Games.")
        return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0")
