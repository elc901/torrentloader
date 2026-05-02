import json

def language():  # выбор языка
    language = input("Your Language (just write 'en' or 'ru') ->     ")
    with open("config.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if language == "en":
        data["language"] = "en"
    elif language == "ru":
        data["language"] = "ru"
    
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)    