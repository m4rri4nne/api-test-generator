from colorama import  init
import assets.theme as theme
import functions.read_swagger as read_swagger
import functions.test_generator as test_generator
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
    clear_screen()
    title_box(theme.MENU_TITLE, theme.PASTEL_PINK)
    type_effect(theme.WELCOME_MESSAGE, 0.04, theme.PASTEL_BLUE)
    while True:
        main_menu()
        option = input(theme.PASTEL_PINK + "\n→ ")
        if option == "5":
            clear_screen()
            type_effect(theme.GOODBYE_MESSAGE, 0.04, theme.PASTEL_GREEN)
            break
        else:
            option_selector(option)




def swagger_load_message(orientation_type = "file"):
    if orientation_type == "file":
        file_path = input(theme.SWAGGER_FILE_PATH_ORIENTATION)
        type_effect("Loading swagger file and parsing the file... Please wait a moment. ⏳", 0.035, theme.PASTEL_YELLOW)
        swagger_data = read_swagger.read_and_parse_swagger(file_path, "file")
    elif orientation_type == "link":
        file_path = input(theme.SWAGGER_LINK_ORIENTATION)
        type_effect("Loading swagger file and parsing the file... Please wait a moment. ⏳", 0.035, theme.PASTEL_YELLOW)
        swagger_data = read_swagger.read_and_parse_swagger(file_path, "link")
    elif orientation_type == "manual":
        type_effect(theme.MANUAL_SPECIFICATION_ORIENTATION, 0.035, theme.PASTEL_BLUE)
        swagger_data = {}
    path_selector(swagger_data)



def path_selector(swagger_data):
    type_effect("✅ Swagger file parsed successfully! Here are the available paths: ", 0.035, theme.PASTEL_GREEN)
    for path in swagger_data["paths"]:
        print(f"Path: {path}")    
    type_effect("Type the path of the endpoint that you want to generate the tests(default: all methods and paths) ", 0.035, theme.PASTEL_PINK)
    selected_path = input(theme.PASTEL_PINK + " → ")
    if selected_path.strip() == "":
        type_effect("You chose to generate tests for all paths and methods.", 0.035, theme.PASTEL_GREEN)
    else:
        methods_available = read_swagger.get_path_info(selected_path, swagger_data)
        for methods in methods_available:
            print()
            print(f"\nMethods available : {methods.upper()}")
        selected_method = method_selector(methods_available) # Select the method available 
        test_generator.test_generator(selected_path, selected_method.lower(), swagger_data) # Generate the tests based on the specifications

def method_selector(methods_available):
    type_effect("Type the method of the endpoint that you want to generate the tests (default: all methods) ", 0.035, theme.PASTEL_PINK)
    selected_method = input(theme.PASTEL_PINK + " → ")
    if selected_method.strip() == "":
        type_effect("You chose to generate tests for all methods.", 0.035, theme.PASTEL_GREEN)
        return selected_method
    else:
        if selected_method.lower() in methods_available:
            type_effect(f"You chose to generate tests for the method: {selected_method.upper()}.", 0.035, theme.PASTEL_GREEN)
            return selected_method
        else:
            type_effect(f"❌ The method '{selected_method.upper()}' is not available for the selected path.", 0.035, theme.PASTEL_RED)
            return