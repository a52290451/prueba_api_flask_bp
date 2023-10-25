import os

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ['DB_USER_FBP']}:{os.environ['DB_PASSWORD_FBP']}@{os.environ['DB_HOST_FBP']}:{os.environ['DB_PORT_FBP']}/{os.environ['DB_NAME_FBP']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
