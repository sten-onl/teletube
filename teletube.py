import telebot
import config
import random
import csv

bot_key = config.TELEGRAM_BOT_API


# You can set parse_mode by default. HTML or MARKDOWN
bot = telebot.TeleBot(bot_key, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, "Howdy, how are you doing? Just send me any YouTube link and I will save it! Commands are /info /user /group /help")


@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(
        message, "I am a Bot created by Sten-Onl. Please consider starring my repo here https://github.com/sten-onl/teletube")


def get_rvideo_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# You can create more user lists by duplicating this part


@bot.message_handler(commands=['user'])
def send_track(message):
    sten = get_rvideo_from_file('user.csv')
    uservideo = random.choice(sten)
    bot.reply_to(
        message, f"Your random track suggestion from User is {uservideo}.")
# until here and creating new .csv lists


@bot.message_handler(commands=['group'])
def send_track(message):
    sten = get_rvideo_from_file('group.csv')
    groupvideo = random.choice(sten)
    bot.reply_to(
        message, f"Your random track suggestion from the Group is {groupvideo}.")


def check_duplicates(link):
    with open('group.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if link in row:
                return True
    return False


@bot.message_handler(content_types=['text'])
def save_data(message):
    # You can add more types of links that can be saved by just adding more options
    if "https://www.youtube.com" or "https://youtu.be" in message.text:
        if not check_duplicates(message.text):
            with open('group.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([message.text])
        bot.send_message(chat_id=message.chat.id,
                         text="YouTube link saved successfully!")
    else:
        bot.send_message(chat_id=message.chat.id,
                         text="Invalid link. Please enter a valid YouTube link.")


print("Teletube is running...")


bot.infinity_polling()
