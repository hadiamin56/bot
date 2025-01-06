from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Replace with your bot's API token
BOT_TOKEN = '7805113858:AAFWsiptVGKCWEvuXa3mB4jVHtlFBqbls5o'

# Function to capture the group chat ID
async def capture_group_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    group_chat_id = update.message.chat.id  # This gets the group chat ID
    print(f"Group Chat ID: {group_chat_id}")  # Print the group chat ID in the console
    await update.message.reply_text(f"The group chat ID is: {group_chat_id}")

def main():
    # Create the application with the bot's token
    application = Application.builder().token(BOT_TOKEN).build()

    # Set up a handler to listen to any messages in the group
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, capture_group_chat_id))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
