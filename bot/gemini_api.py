import json

import google.generativeai as genai
from config import GEMINI_API
from bot import message

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
      "parts": [message.prompt],
    },
  ]
)


def generate(text):
    response = chat_session.send_message(text)
    response_data = json.loads(response.text)
    title = response_data.get("title", "No title")
    content = ''

    if 'main_text' in response_data:
        content = response_data.get("main_text", "No main_text")
    elif 'body' in response_data:
        content = response_data.get("body", "No body")
    elif 'content' in response_data:
        content = response_data.get("content", "No content")

    formatted_response = f"{title}\n\n{content}"
    print(response.text)
    print(response_data)
    return formatted_response

