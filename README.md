# Telegram Chatbot with Gemini Integration

This project is a Telegram chatbot that leverages the Gemini API to provide interactive and intelligent conversations. It allows users to engage in chats, save chat history, and retrieve previous conversations. The bot is designed to handle multiple users, store chat data in a PostgreSQL database, and provide a seamless user experience.

## Features

- **Interactive Chat**: Users can start new chats or continue existing ones.
- **Chat History**: Users can view and retrieve their chat history.
- **Dynamic Keyboard**: Provides context-aware reply keyboards for easy navigation.
- **Database Integration**: Stores chat data in a PostgreSQL database for persistence.
- **Error Handling**: Robust exception handling and logging for debugging.

## Key Functions

### Core Functionality

- `start(bot, user: User)`: Initializes the bot, sends a welcome message, and sets up the database for the user.
- `add_conversation_to_current_chat(bot, user: User, message: str)`: Adds user messages and AI responses to the current chat dialog.
- `display_chat_in_history(bot, user: User, message: str)`: Displays a specific chat from the user's history.
- `update_history(user: User)`: Updates the user's chat history by retrieving data from the database.

### Database Operations

- `execute(command, fetchall=False, fetchone=False)`: Executes SQL commands and fetches results if needed.
- `replace_table_data(table_name, chat_1, chat_2, chat_3)`: Replaces chat data in the database table.
- `add_new_chat_to_db(user: User)`: Adds a new chat to the database.
- `update_existing_chat(user: User)`: Updates an existing chat in the database.

### Utility Functions

- `get_gemini_response(text, context="")`: Generates a response using the Gemini API.
- `short_text(text, symbols, clarification="")`: Shortens text while preserving context using Gemini.
- `log_exception(msg)`: Logs exceptions with detailed context for debugging.
- `get_reply_keyboard(*args)`: Creates a custom reply keyboard for Telegram.

### Connection Management

- `get_connection(db_name)`: Establishes and manages a connection to the PostgreSQL database.

## Setup

### Prerequisites

- Python 3.x
- PostgreSQL database
- Telegram Bot Token
- Gemini API Key

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/telegram-gemini-bot.git
   cd telegram-gemini-bot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the PostgreSQL database and update the connection details in the code.

4. Configure environment variables:

   ```bash
   export TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   export GEMINI_API_KEY=your_gemini_api_key
   ```

5. Run the bot:

   ```bash
   python main.py
   ```

## Usage

1. Start the bot on Telegram by sending `/start`.
2. Use the reply keyboard to navigate between options like **New Chat** and **History**.
3. Engage in conversations, and the bot will save your chat history for future reference.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
