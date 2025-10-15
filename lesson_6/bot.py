import telebot
import random
import os
print(os.listdir('images'))

bot = telebot.TeleBot('8303579544:AAE-D-LxtSOfVeWC7dLena4wwphzCuBVpaQ')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Вот список команд:"
    "")



@bot.message_handler(commands=['mycor'])
def send_mem(message):
    img_name = random.choice(os.listdir('images'))  # Случайным образом выбираем изображение
    with open(f'images/{img_name}', 'rb') as f:
        # Отправляем фото, выбранное случайным образом
        bot.send_photo(message.chat.id, f)
        
@bot.message_handler(commands=['plastik'])
def start_command(message):
    bot.send_message(message.chat.id, "Ты знал что пластик разлогается больше чем 450 лет"
    "")

@bot.message_handler(commands=['steklo'])
def start_command(message):
    bot.send_message(message.chat.id, "Запомни стекло разлагается 1000 лет!"
    "")

@bot.message_handler(commands=['deti'])
def start_command(message):
    bot.send_message(message.chat.id, "Если ты будешь с маленьким ребёнком, запомни что нельзя бросать подгузники ведь они разлагаются 450 лет"
    "")

@bot.message_handler(commands=['priroda'])
def start_command(message):
    bot.send_message(message.chat.id, "Так ещё запомни что нельза кидать мусор где папало!"
    "")

bot.polling()