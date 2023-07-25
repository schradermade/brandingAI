import os
import openai
import argparse
import re
from typing import List

MAX_INPUT_LENGTH = 32


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    print(f"User Input:", user_input)

    if validate_length(user_input):
        generate_branding_snippet(user_input)
        generate_keywords(user_input)
    else:
        raise ValueError(
            f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Submitted input is: '{user_input}'")


def validate_length(prompt: str) -> bool:
    return len(prompt) <= MAX_INPUT_LENGTH


def generate_keywords(prompt: str) -> List[str]:
    openai.api_key = "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"
    openai.api_key = os.getenv(
        "OPENAI_API_KEY")

    enriched_prompt = f"Generate related branding keywords for {prompt}: "
    print(enriched_prompt)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=enriched_prompt,
        max_tokens=32
    )

    # Extract ouput text.
    keyword_text: str = response["choices"][0]["text"]
    # Strip white space
    keyword_text = keyword_text.strip()
    # keywords_array = re.split('[[0-9].\n]', keyword_text)
    print(f"Keywords: {keyword_text}")
    return keyword_text


def generate_branding_snippet(prompt: str) -> str:
    openai.api_key = "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"
    openai.api_key = os.getenv(
        "OPENAI_API_KEY")

    enriched_prompt = f"Generate upbeat branding snippet for {prompt}: "
    print(enriched_prompt)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=enriched_prompt,
        max_tokens=32
    )

    # Extract ouput text.
    branding_text: str = response["choices"][0]["text"]
    # Strip white space
    branding_text = branding_text.strip()
    # Add ... to truncated statements
    last_char = branding_text[-1]
    if last_char not in {".", "!", "?"}:
        branding_text += "..."

    print(f"Snippet: {branding_text}")
    return branding_text


if __name__ == "__main__":
    main()
