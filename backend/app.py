from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://war_app_user:password@localhost/war_app'
db = SQLAlchemy(app)

class Statistic(db.Model):
    __tablename__ = 'statistics'

    id = db.Column(db.Integer, primary_key=True)
    won = db.Column(db.Integer, nullable=False)
    lost = db.Column(db.Integer, nullable=False)
    current_winning_streak = db.Column(db.Integer, nullable=False)
    longest_winning_streak = db.Column(db.Integer, nullable=False)
    longest_losing_streak = db.Column(db.Integer, nullable=False)
    total_games = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'won': self.won,
            'lost': self.lost,
            'current_winning_streak': self.current_winning_streak,
            'longest_winning_streak': self.longest_winning_streak,
            'longest_losing_streak': self.longest_losing_streak,
            'total_games': self.total_games,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


@app.route('/')
def hello():
    return 'Hey!'

if __name__ == '__main__':
    app.run()
