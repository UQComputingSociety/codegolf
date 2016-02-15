from .user import User
from .challenge import Challenge
from .base import Base
import sqlalchemy as sa
import sqlalchemy.orm as sao

__all__ = ["Submission"]


class Submission(Base):
    id = sa.Column(sa.Integer, primary_key=True)
    challenge_id = sa.Column(sa.Integer, sa.ForeignKey(Challenge.id))
    user_id = sa.Column(sa.Integer, sa.ForeignKey(User.id))
    submitted_at = sa.Column(sa.DateTime)
    language = sa.Column(sa.Integer)
    content = sa.Column(sa.Text, nullable=False)
    points = sa.Column(sa.Integer, default=0, server_default="0", nullable=False)

    challenge = sao.relationship('Challenge')
    user = sao.relationship('User')
