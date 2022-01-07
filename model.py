from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""

    Game.query.delete()

    # Add sample games
    game1 = Game(name='Gammer 1', description="A game about games")
    game2 = Game(name='Gaming 2', description="A game")
    game3 = Game(name='Gammmme 3', description="This is a cool game")
    game4 = Game(name='Game 4')

    db.session.add_all([game1, game2, game3, game4])
    db.session.commit()


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
