import os

from dotenv import load_dotenv


load_dotenv()


print(os.environ.get("SECRET_KEY"))
print(os.environ.get("EMAIL_PORT"))