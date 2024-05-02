import telebot
from utils.jjson import json_open, json_write
from github import Github
import config
from utils.githubApi import commit_to_gh

bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_site_text(message):
    bot.send_message(message.chat.id, 'Команда для изменения текст: /text2site ВАШ ТЕКСТ\n\nhttps://github.com/keeniGitHub/tg2html\nhttps://keeniGitHub.github.io/tg2html')
    
@bot.message_handler(commands=['text2site'])
def handle_site_text(message):
    text = message.text[11:]

    json_file_path = "text.json"
    json_write(json_file_path, text)

    bot.send_message(message.chat.id, 'Успешно!')

    commit_to_gh(config.GH_TOKEN, 'tg2html', json_file_path, 'Update json', json_open(json_file_path))


bot.polling(non_stop=True)
