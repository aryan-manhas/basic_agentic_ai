import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types


load_dotenv()


def main():

    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("API Key Not Provided!")
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Agentic AI Bot")
    parser.add_argument("user_prompt", type=str, help="Prompt")
    args = parser.parse_args()

    message = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message,
    )

    tokens = response.usage_metadata
    if tokens is None:
        RuntimeError("API Request Failed!")

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print(f"Response:\n{response.text}")


if __name__ == "__main__":
    main()
