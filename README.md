# Anonymouschat
Anonymous chat telegram bot
```python
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up Telegram bot
bot_token = 'YOUR_BOT_TOKEN_HERE'
bot_chatID = 'YOUR_CHAT_ID_HERE'
bot = telegram.Bot(token=bot_token)

# Set up Updater and dispatcher
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

# Define start command handler
def start(update, context):
    bot.send_message(chat_id=update.effective_chat.id, text="Welcome! To start chatting, send /chat followed by your message.")

# Define chat command handler
def chat(update, context):
    message = update.message
    user_id = message.from_user.id

    # Check if user is authorized to chat
    if user_id not in authorized_users:
        bot.send_message(chat_id=message.chat_id, text="Sorry, you are not authorized to chat.")
        return

    # Check if user has already started a chat
    if user_id in active_chats:
        bot.send_message(chat_id=message.chat_id, text="You have already started a chat.")
        return

    # Add user to active chats list
    active_chats.append(user_id)

    # Send message to other user
    other_user_id = authorized_users[0] if user_id == authorized_users[1] else authorized_users[1]
    bot.send_message(chat_id=other_user_id, text=f"New chat started with user {user_id}.\n\n{message.text}")

# Define message handler
def message_handler(update, context):
    message = update.message
    user_id = message.from_user.id

    # Check if user is authorized to chat
    if user_id not in authorized_users:
        bot.send_message(chat_id=message.chat_id, text="Sorry, you are not authorized to chat.")
        return

    # Check if user has an active chat
    if user_id not in active_chats:
        bot.send_message(chat_id=message.chat_id, text="You are not currently in a chat. To start a new chat, send /chat followed by your message.")
        return

    # Send message to other user
    other_user_id = authorized_users[0] if user_id == authorized_users[1] else authorized_users[1]
    bot.send_message(chat_id=other_user_id, text=f"User {user_id} says:\n\n{message.text}")

# Add handlers to dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('chat', chat))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

# Set up authorized users and active chats lists
authorized_users = []  # Add user IDs of authorized users here
active_chats = []

# Start polling for updates
updater.start_polling()
updater.idle()
```

Here's how the script works:

1. The script sets up a Telegram bot using the `telegram.Bot` class from the `python-telegram-bot` library, and sets the bot token using the `bot_token` variable.
2. The script sets up an `Updater` and a `dispatcher` using the `Updater` class from the `python-telegram-bot` library.
3. The script defines a `start` function that sends a welcome message to users when they send the `/start` command.
4. The script defines a `chat` function that allows users to start a new chat. When a user sends the `/chat` command, the function adds the user to the `active_chats` list and sends a message to the other authorized user with the content of the message.
5. The script defines a `message_handler` function that sends messages between authorized users who are in an active chat.
6. The script adds the `start`, `chat`, and `message_handler` functions as handlers to the `dispatcher`.
7. The script sets the `authorized_users` list to contain the IDs of the two users who are authorized to chat.
8. The script starts polling for updates using the `start_polling` method of the `Updater` object.

Note that this is a very basic example of a chat bot, and there are many ways to improve it depending on your needs. For example, you may want to add more sophisticated authentication mechanisms, such as password protection or two-factor authentication. Additionally, you may want to add the ability to end a chat or to have multiple chats at once.
