
import telebot

TOKEN = "7905209246:AAHcZqzE7sVpubtaYv_rKK28Crd9b4PMt1E"
bot = telebot.TeleBot(TOKEN)

# Step 1: Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    countries = ['🇺🇸 USA', '🇬🇧 UK', '🇩🇪 Germany', '🇨🇦 Canada', '🇦🇺 Australia',
                 '🇫🇷 France', '🇮🇳 India', '🇧🇷 Brazil', '🇯🇵 Japan', '🇧🇩 Bangladesh']
    for i in range(0, len(countries), 2):
        markup.add(*countries[i:i+2])
    bot.send_message(message.chat.id, "🎁 Welcome to RRS Gift Card Bot!\nPlease select your country:", reply_markup=markup)

# Step 2: Country selection
@bot.message_handler(func=lambda msg: msg.text in ['🇺🇸 USA', '🇬🇧 UK', '🇩🇪 Germany', '🇨🇦 Canada', '🇦🇺 Australia',
                                                    '🇫🇷 France', '🇮🇳 India', '🇧🇷 Brazil', '🇯🇵 Japan', '🇧🇩 Bangladesh'])
def select_country(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add('🎁 Amazon Gift Card', '📺 Netflix Gift Card', '🎮 Roblox Gift Card', '🎯 Google Play Card')
    bot.send_message(message.chat.id, f"You selected {message.text}.\nNow choose your card type:", reply_markup=markup)

# Step 3: Card selection
@bot.message_handler(func=lambda msg: msg.text in ['🎁 Amazon Gift Card', '📺 Netflix Gift Card', '🎮 Roblox Gift Card', '🎯 Google Play Card'])
def send_link(message):
    card_name = message.text
    card_map = {
        '🎁 Amazon Gift Card': 'amazon',
        '📺 Netflix Gift Card': 'netflix',
        '🎮 Roblox Gift Card': 'roblox',
        '🎯 Google Play Card': 'googleplay'
    }
    card_key = card_map.get(card_name, 'default')
    link = f"https://www.rrsweb3.com/{card_key}"
    bot.send_message(message.chat.id, f"✅ Here's your {card_name} link:\n🔗 {link}")

# Run the bot
bot.polling()
