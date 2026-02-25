from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cve(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cve_id = db.Column(db.String(50), unique=True)
    description = db.Column(db.Text)
    published = db.Column(db.String(50))
    modified = db.Column(db.String(50))
    score_v3 = db.Column(db.Float)

    def to_json(self):
        return {
            "cve_id": self.cve_id,
            "description": self.description,
            "published": self.published,
            "modified": self.modified,
            "score_v3": self.score_v3
        }