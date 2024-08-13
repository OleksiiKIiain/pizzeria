from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker, Session


def get_session() -> Session:
    url = URL.create(
        drivername='postgresql',
        database="postgres",
        host="localhost",
        port=5432,
        username="postgres",
        password="postgres"
    )

    engine = create_engine(url)
    session = sessionmaker(bind=engine)

    return session()
