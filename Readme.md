# Telegram Channel Bot

## Description
This project is a Telegram bot designed to manage a telegram channel focused on Python. The bot can generate and post content to the channel using the Gemini API for text generation. It supports commands to start the bot, get user IDs, and post generated content.

## Features
- Generate and post content to a Telegram channel.
- Handle commands like `/start`, `/help`, `/get_id`, and `/post`.
- Use the Gemini API to generate text content in a casual style.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/batirniyaz/tg_channel_bot.git
    cd tg_channel_bot
    ```

2. Create a virtual environment and activate it:
    - On Unix or macOS:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
    - On Windows:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Copy the .env-example file to .env and add your configuration:
    ```sh
    cp .env-example .env
    ```

5. Edit the .env file and add your configuration:
    ```dotenv
    TOKEN='your bot token'
    CHANNEL_ID='channel id you want to post'
    ADMIN_ID='admin id'
    GEMINI_API='gemini api key'
    ```

## Usage
1. Run the bot:
    ```sh
    python main.py
    ```

2. Interact with the bot using the following commands:
    - `/start` or `/help`: Start the bot and get a welcome message.
    - `/get_id`: Get the chat ID, message ID, and user ID.
    - `/post`: Generate and post content to the channel.

## License
This project is licensed under the MIT License.