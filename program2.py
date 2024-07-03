import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

print("The key :- " , os.getenv("KEY"))