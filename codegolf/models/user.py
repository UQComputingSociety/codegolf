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


class Admin(Base):
    id = sa.Column(sa.Integer, sa.ForeignKey(User.id), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "Admin",
    }
