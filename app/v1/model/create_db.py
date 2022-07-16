try:
    from app.v1.model.user_model import User
    from app.v1.model.get_engine import CreateEngine
except ImportError:
    from user_model import User  # noqa
    from get_engine import CreateEngine
from sqlmodel import SQLModel


"""
module use for the first time to create
the models in the database
"""


def create_db():
    EngineClass = CreateEngine()
    engine = EngineClass.__open__()
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db()
    print("Database created")
    exit(0)
