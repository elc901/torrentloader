import json

def language(write, set_handler): # выбор языка

    write("Your Language (just write 'en' or 'ru') ->  ")
    
    def handle_input(user_input):
        with open("config.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        if user_input == "en":
            data["language"] = "en"
            write("Language set to English.\n")
        elif user_input == "ru":
            data["language"] = "ru"
            write("Язык установлен: Русский.\n")
        else:
            write(f"Unknown language: '{user_input}'. Use 'en' or 'ru'.\n")
        
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    
    set_handler(handle_input)  # возврат управления в терминал



def 