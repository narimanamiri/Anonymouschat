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
