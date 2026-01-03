from colorama import Fore, Style

# Colors: 
PASTEL_PINK   = Fore.LIGHTMAGENTA_EX
PASTEL_BLUE   = Fore.LIGHTCYAN_EX
PASTEL_YELLOW = Fore.LIGHTYELLOW_EX
PASTEL_GREEN  = Fore.LIGHTGREEN_EX
PASTEL_RED   = Fore.LIGHTRED_EX
TYPE_COLOR = Fore.WHITE

# Text Styles:
RESET = Style.NORMAL
BOLD = Style.BRIGHT
UNDERLINE = '\033[4m'   

# Texts: 

WELCOME_MESSAGE = "Welcome to API Test Generator✨"
MENU_TITLE = ("🌸 API Test Generator - by: Alicia de Paula 🌸") 
OPTION_PROMPT = "Chose your option:\n"
OPTION_6 = "Returning to the main menu..."
GOODBYE_MESSAGE = "Thank you for using the API Test Generator! See you later!"
ERROR_MESSAGE = "❌ An error occurred. Please try again."
INSTRUCTION_MESSAGE = "Please follow the instructions to provide the necessary information."
LOADING_MESSAGE = "Loading... Please wait a moment. ⏳"
SUCCESS_MESSAGE = "✅ Operation completed successfully!"
HELP_MESSAGE = (
    "\nThis application helps you generate API tests based on Swagger specifications. "
    "\nYou can provide a Swagger file in JSON format, a link to a Swagger file, or manually specify the API details."
    "\nTo contribute, visit: https://github.com/m4rri4nne/api-test-generator"
    "\nFeel free to open issues or submit pull requests!\n\n"
)

SWAGGER_FILE_PATH_ORIENTATION = "You chose to generate tests using a file, please provide the path to your Swagger JSON file: "
SWAGGER_LINK_ORIENTATION = "You chose to generate tests using an url, please provide a valid URL to the Swagger JSON file: "
MANUAL_SPECIFICATION_ORIENTATION = "You chose to generate tests using manual specification, please provide the necessary details as prompted: "


LIST_OF_OPTIONS={
    "1": "Understanding the application 🎀",
    "2": "Generate tests using a swagger file - JSON format",
    "3": "Generate tests using a swagger link - URL format",
    "4": "Generate tests using manual specification",
    "5": "Exit ❌"
}

PROMPT_TEMPLATE = ("GET /users/{id} "
                   "✔ Scenario: Retrieve a user with a valid ID   "
                   "✔ Scenario: Validate 404 for user not found  "
                   "✘ Scenario: Missing ID parameter  "
                   "✘ Scenario: Invalid format for ID ")
