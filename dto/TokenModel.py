from app import db


class TokenModel(db.Model):
    __tablename__ = 'token'

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(32))

    def __repr__(self):
        return 'Token: {}'.format(self.token)
