import json

def language(user_input, write):
    with open("config.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if user_input == "en":
        data["language"] = "en"
        write("Language set to English.\n")
    elif user_input == "ru":
        data["language"] = "ru"
        write("Язык установлен: Русский.\n")
    else:
        write(f"Unknown: '{user_input}'. Use 'en' or 'ru'.\n")
    
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
def help(write):
    with open("config.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    if data["language"] == "en":
        write("help - show all commands\n")
        write("clg - allows you to select the language ( ru or en )\n")
        write("about - about project\n")
    elif data["language"] == "ru":
        write("help - показывает все команды\n")
        write("clg - позволяет тебе выбрать язык ( ru или en )\n")
        write("about - о проекте\n")
    elif data["language"] == "none":
        write("write 'clg'\n")
        write("напиши 'clg'\n")
def path_for_download_torrent(user_input, write): # дописать
    with open("config.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    pass
def about_programm(write):
    with open("config.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    if data["language"] == "en":
        write("Developer: elc901\n")
        write("Link to owner on GitHub: https://github.com/elc901\n")
        write("Link to repository on GitHub: https://github.com/elc901/torrentloader\n")
        write("Versions: https://github.com/elc901/torrentloader/releases\n")
    else:
        write("Разработчик: elc901\n")
        write("Ссылка на профиль разработчика на GitHub: https://github.com/elc901\n")
        write("Сслыка на репозиторий на GitHub: https://github.com/elc901/torrentloader\n")
        write("Версии: https://github.com/elc901/torrentloader/releases\n")