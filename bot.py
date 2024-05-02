import telebot
import json
from github import Github
import config

bot = telebot.TeleBot(config.BOT_TOKEN)
g = Github(config.GH_TOKEN)

# Имя вашего репозитория
repo_name = config.REPOSITORY_NAME

# Получаем репозиторий
repo = g.get_user().get_repo(repo_name)

@bot.message_handler(commands=['site-text'])
def handle_site_text(message):
    text = message.text[11:]
    with open('text.json', 'w') as file:
        json.dump({'text': text}, file)
    bot.send_message(message.chat.id, 'Текст успешно записан в файл')

    json_file_path = "text.json"

    file = repo.get_contents(json_file_path)

    # Создаем коммит в репозитории
    path_to_json = json_file_path
    new_content = ""
    with open(json_file_path, "r") as file_1:
        data = json.load(file_1)
        new_content = json.dumps(data)
        
    repo.update_file(path_to_json, "update json", new_content, file.sha)


bot.polling(non_stop=True)
