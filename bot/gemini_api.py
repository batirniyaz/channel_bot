import json

import google.generativeai as genai
from config import GEMINI_API

genai.configure(api_key=GEMINI_API)

generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-002",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "You are an admin in a Telegram Channel. The channel is about programming(python) and your task is to post "
        "some kind of content. Below will be the topic. Write the post in casual style. NOTE: write your text in "
        "markdown mode( with markdown tegs where text should be bold or something else)"
      ],
    },
  ]
)


def generate(text):
    response = chat_session.send_message(text)
    response_data = json.loads(response.text)
    title = response_data.get("title", "No title")
    content = response_data.get("content", "No content")
    formatted_response = f"Title: {title}\n\n{content}"
    return formatted_response

