import os
from dotenv import load_dotenv
from google import genai


load_dotenv()


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("API Key Not Provided!")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    )
    tokens = response.usage_metadata
    if tokens is None:
        RuntimeError("API Request Failed!")

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print(f"Response:\n{response.text}")


if __name__ == "__main__":
    main()
