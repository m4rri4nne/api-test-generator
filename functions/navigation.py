from colorama import  init
import assets.theme as theme
import functions.read_swagger as read_swagger
import time
import os

init(autoreset=True)


def type_effect(text, delay=0.03, color=theme.TYPE_COLOR):
    for char in text:
        print(color + char + theme.RESET , end="", flush=True)
        time.sleep(delay)
    print() # New line


def title_box(text, color=theme.PASTEL_PINK):
    width = len(text) + 10
    print(color + "┌" + "─" * width + "┐")
    print(color + f"│   {text}     │")
    print(color + "└" + "─" * width + "┘" + theme.RESET)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# --------------------------
# INTERFACE
# --------------------------

def main_menu():
    print()
    type_effect(theme.OPTION_PROMPT, 0.03, theme.PASTEL_PINK)
    print(theme.PASTEL_BLUE   + theme.OPTION_1)
    print(theme.PASTEL_YELLOW + theme.OPTION_2)
    print(theme.PASTEL_GREEN  + theme.OPTION_3)
    print(theme.PASTEL_PINK   + theme.OPTION_4)
    print(theme.PASTEL_YELLOW + theme.OPTION_5)
  

def option_selector(option):
    if option == "1":
        type_effect(theme.HELP_MESSAGE, 0.035, theme.PASTEL_YELLOW)
        type_effect(theme.OPTION_6, 0.035, theme.PASTEL_BLUE)
    elif option == "2":
        swagger_load_message("file")
    elif option == "3":
        swagger_load_message("link")
    elif option == "4":
        swagger_load_message("manual")
    elif option == "5":
        type_effect(theme.GOODBYE_MESSAGE, 0.04, theme.PASTEL_GREEN)
        exit()



def app_text_box():
    title_box(theme.MENU_TITLE, theme.PASTEL_PINK)
    type_effect(theme.WELCOME_MESSAGE, 0.04, theme.PASTEL_BLUE)
    while True:
        main_menu()
        option = input(theme.PASTEL_PINK + "\n→ ")
        if option == "5":
            type_effect(theme.GOODBYE_MESSAGE, 0.04, theme.PASTEL_GREEN)
            break
        else:
            option_selector(option)




def swagger_load_message(orientation_type = "file"):
    if orientation_type == "file":
        file_path = input(theme.SWAGGER_FILE_PATH_ORIENTATION)
        type_effect("Loading swagger file and parsing the file... Please wait a moment. ⏳", 0.035, theme.PASTEL_YELLOW)
        read_swagger.read_and_parse_swagger(file_path, "file")
    elif orientation_type == "link":
        file_path = input(theme.SWAGGER_LINK_ORIENTATION)
        type_effect("Loading swagger file and parsing the file... Please wait a moment. ⏳", 0.035, theme.PASTEL_YELLOW)
        read_swagger.read_and_parse_swagger(file_path, "link")
    elif orientation_type == "manual":
        type_effect(theme.MANUAL_SPECIFICATION_ORIENTATION, 0.035, theme.PASTEL_BLUE)