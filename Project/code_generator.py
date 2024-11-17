import openai  # For AI-driven code generation (replace with your key)
import random

openai.api_key = "your_openai_api_key"

def generate_code(objective):
    """
    Generates Python code based on the given objective.
    Returns success status and the generated code.
    """
    try:
        # AI-based code generation
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Write a Python function to {objective}.",
            max_tokens=150,
        )
        code = response.choices[0].text.strip()
        return True, code
    except Exception as e:
        print(f"Error generating code: {e}")
        return False, ""

