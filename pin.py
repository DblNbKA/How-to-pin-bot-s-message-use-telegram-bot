import telebot #I think you know what it is for

bot = telebot.TeleBot('Your telegram bot token') #Instead of "Your telegram bot token" you insert the token that @BotFather gave you

@bot.message_handler(commands=['start']) #The bot will respond to the /start command

def pin(message): #function
    bot.send_message(message.chat.id, 'Your text with a greeting, explanation, or something similar, depending on what you need') #sending message by bot
    pinn = bot.send_message(message.chat.id, 'The message you want to pin').message_id #sending the message you want to pin and saving its ID with .message_id
    bot.pin_chat_message(message.chat.id, message_id = pinn) #Pinning a message
