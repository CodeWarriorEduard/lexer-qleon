from lexer import *


class QleonLexer:
    # __HELPCOMMAND = "help()"
    # __EXITCOMMAND = "exit()" 
    # __VERSION = "1.0"
    # __DATECREATION = "Feb 4 2024, 1:41:20"
    # __HELPMESSAGE = f'Welcome to QLeon {__VERSION} help utility!.\n\nWe are still working on finalizing the language.\n\nTo exit this help utility and return to the Lexer,\nenter "ex" or "exit".\n'
    # __INTERPRETEROUTPUT = "---> "
    # __HELPOUTPUT = "help()---> "
    # __EXITCOMMANDSHELP = ["ex", "exit"]

    def __init__(self):
        pass

    def handleInput(self, userInput):
        return userInput

    def qLeonImpl(self, userCodeInput): ## Implementación Qleon Lexer.
        code = userCodeInput
        lex = Lexer(code)
        tokens = lex.tokenizer()
        return tokens


    def run(self, code):
        # Creamos instancia de nuestra shell.
        return self.qLeonImpl(code)
    
