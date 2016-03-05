from .base import Base
import sqlalchemy as sa

__all__ = ["User", "Admin"]


class User(Base):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text)
    email = sa.Column(sa.Text, unique=True)
    uq_user = sa.Column(sa.String(8), unique=True, nullable=True)
    points = sa.Column(sa.Integer, default=0, server_default="0", nullable=False)
    role = sa.Column(sa.String(20), nullable=False)

    __mapper_args__ = {
        "polymorphic_on": role,
        "polymorphic_identity": "User",
    }

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return True

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


class Admin(Base):
    id = sa.Column(sa.Integer, sa.ForeignKey(User.id), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "Admin",
    }
