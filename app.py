from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Test if API key is loaded
api_key = os.getenv("OPENAI_API_KEY")

print(f"API Key loaded: {api_key}")  # This should print your actual API key, ensure it prints correctly

if api_key is None:
    raise ValueError("API key not found. Ensure OPENAI_API_KEY is set in the environment or .env file.")
