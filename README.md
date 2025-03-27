# [Telegram Chatbot](https://t.me/gemini_chat_python_bot) with Gemini Integration

This project is a Telegram chatbot that leverages the Gemini API to provide interactive and intelligent conversations. It allows users to engage in chats, save chat history, and retrieve previous conversations. The bot is designed to handle multiple users, store chat data in a PostgreSQL database, and provide a seamless user experience. You can try it but after a simple installation.

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

- `get_connection(db_name, host, user, password, port)`: Establishes and manages a connection to the PostgreSQL database.

## Setup

### Prerequisites

- Python 3.x
- PostgreSQL database
- Telegram Bot Token
- Gemini API Key
- Docker (optional)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com//MaksKroha/GeminiChatBot.git
   cd GeminiChatBot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the PostgreSQL database and update the connection details in the code.

4. Configure environment variables:

   ```bash
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   GEMINI_API_KEY=your_gemini_api_key
   SEPARATOR=message_separator
   DB_NAME=your_database_name
   DB_HOST=your_service_name
   DB_USER=your_user_name
   DB_PASSWORD=your_db_password
   DB_PORT=yout_db_port
   ```
5. Run the main file which launch the bot and starts accepting requests from the user on [telegram](https://t.me/gemini_chat_python_bot)
   ```bash
   python3 main.py
   ```

## Usage

1. Start the bot on Telegram by sending `/start` (optional).
2. Use the reply keyboard to navigate between options like **New Chat** and **History**.
3. Engage in conversations, and the bot will save your chat history for future reference.

## Docker Deployment

The project includes Docker support for easy deployment.

### Running with Docker Compose

```bash
docker-compose up --build
```

To stop and remove the containers:

```bash
docker-compose down
```

### Services

- **bot**: Runs the Telegram bot backend in Python.
- **postgres**: Hosts the PostgreSQL database.
- **pgadmin**: Provides a web interface for managing the database.

### Database Initialization

Upon the first run, the PostgreSQL container executes `init.sql` to create the necessary database and tables automatically.

## Project Structure

```
telegram-gemini-bot/
├── database/               # Database-related functions
├── exception/              # Exception handling and logging
├── gemini/                 # Gemini API integration
├── handlers/               # Bot logic and command handlers
├── keyboard/               # Telegram reply keyboard setup
├── .dockerignore
├── .env                    # Environment variables
├── .gitignore
├── bot.log                 # Log file for exceptions and debug info
├── docker-compose.yml      # Docker configuration
├── Dockerfile              # Docker build instructions
├── init.sql                # SQL script to initialize database
├── main.py                 # Entry point of the bot
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── User.py                 # User model
```
## Branch 'deploy'

A branch for deploying a project to a remote server (in my case, aws).
The branch contains all the necessary files (except .env) to create and run a container on a remote server with Docker installed

## pgAdmin Access

To access pgAdmin for database management, open:

```
http://localhost:8080
```

These values can be changed in the `docker-compose.yml` file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Author

Maksym [GitHub](https://github.com/MaksKroha) | [Telegram](https://t.me/maks_kroha)
