import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types


load_dotenv()


def main():

    # Gets the API key from .env file using os & dotenv library & validates it
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("API Key Not Provided!")
    client = genai.Client(api_key=api_key)

    # Parse the user prompt into a string type and stores the answer in args
    parser = argparse.ArgumentParser(description="Agentic AI Bot")
    parser.add_argument("user_prompt", type=str, help="Prompt")

    # Adds the option to access more information(Token Information) in the output(also known as "verbose")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    # Activates the Parser
    args = parser.parse_args()

    # User prompt will be saved in a list "message". Right now only the current prompt is saved
    message = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Gets the response from gemini 2.5 flash
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message,
    )

    # Counts the token usage through "usage_metadata"
    tokens = response.usage_metadata
    if tokens is None:
        RuntimeError("API Request Failed!")

    # Prints the user & model token count only if verbose is true & the response received
    if args.verbose is True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response:\n{response.text}")


if __name__ == "__main__":
    main()
