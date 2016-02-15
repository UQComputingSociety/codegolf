from .base import Base
import sqlalchemy as sa
import sqlalchemy.orm as sao
from .user import User

__all__ = ["Challenge"]


class Challenge(Base):
    id = sa.Column(sa.Integer, primary_key=True)
    start = sa.Column(sa.DateTime)
    duration = sa.Column(sa.Interval)
    submitter_id = sa.Column(sa.Integer, sa.ForeignKey(User.id))
    title = sa.Column(sa.Text)
    description = sa.Column(sa.Text)

    submitter = sao.relationship('User')

    @property
    def end(self):
        return self.start + self.duration

    @end.setter
    def end(self, endtime):
        self.duration = endtime - self.start
