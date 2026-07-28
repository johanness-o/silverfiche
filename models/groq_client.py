import os
from groq import Groq

# Set your API key as an environment variable:
# export GROQ_API_KEY="your_key_here"
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

MODEL_NAME = "llama-3.1-8b-instant"  # good default