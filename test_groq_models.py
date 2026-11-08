# test_groq_models.py

from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=groq_api_key
)

models = client.models.list()

for model in models.data:
    print(model.id)
