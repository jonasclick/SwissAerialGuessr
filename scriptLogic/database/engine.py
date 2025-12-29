from sqlalchemy import create_engine

# Parameters for the pymysql DB-API Driver
DB_USER = "root"
DB_PASS = "1234"
DB_HOST = "localhost"
DB_NAME = "swissaerialguessr"

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
)

# Create DB engine to interact with DB
engine = create_engine(DATABASE_URL)

