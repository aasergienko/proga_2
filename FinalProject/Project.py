import telebot
import markovify
import os
from telebot import types

TOKEN = os.environ["SECRET_KEY"]
#telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'} #задаем прокси
bot = telebot.TeleBot(TOKEN, threaded = "false")

bot.remove_webhook()

with open("shahnameh.txt", encoding="utf-8") as f:
    text = f.read()
    text_model = markovify.NewlineText(text)

with open("shahnameh_pers.txt", encoding="utf-8") as f2:
    text2 = f2.read()
    text_model2 = markovify.NewlineText(text2)

keyboard = types.ReplyKeyboardMarkup(row_width=2)  
btn1 = types.KeyboardButton('На русском')
btn2 = types.KeyboardButton('На персидском')

keyboard.add(btn1, btn2)


    
@bot.message_handler(regexp='На русском')
def send_len_rus(message):
    sentence2 = generate_sentence()
    bot.send_message(message.chat.id, sentence2)

@bot.message_handler(regexp='На персидском')
def send_len_pers(message):
    sentence3 = generate_sentence2()
    bot.send_message(message.chat.id, sentence3)
    
@bot.message_handler(func=lambda m: True)
def send_welcome(message):
    bot.send_message(message.chat.id, "Этот бот генерирует цитату из Шахнаме на русском или на персидском")
    bot.send_message(message.chat.id, "Вам послать цитату на русском или на персидском?", reply_markup=keyboard)

def generate_sentence():
    sentence = str(text_model.make_sentence()) + '\n' + str(text_model.make_sentence())
    return sentence

def generate_sentence2():
    sentence = str(text_model2.make_sentence()) + '\n' + str(text_model2.make_sentence())
    return sentence


    
if __name__ == '__main__':
    import os
    bot.polling(none_stop=True)
    app.debug = True
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
