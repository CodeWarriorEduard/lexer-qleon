class Token:
    
    def __init__(self,  tokenType, tokenValue):
        self.__tokenType = tokenType
        self.__tokenValue = tokenValue
        self.__line = -1
        
    
    def __repr__(self) -> str:
        return type(self).__name__   #alternativa self.__tokenValue

    def tokenValue(self) -> str:
        return self.__tokenValue
    
    def tokenComplete(self) -> str:
        return  f"TokenType: {type(self).__name__} || TokenValue: {self.__tokenValue} || TokenLine: {self.__line}"

    def getLine(self) ->int:
        return self.__line
    
    def setLine(self,line):
        self.__line = line

    def getTokenType(self):
        return self.__tokenType
    
    def getTokenValue(self):
        return self.__tokenValue


##NUMBERS
class Integer(Token):
    def __init__(self, tokenValue):
        super().__init__("INTEGER", tokenValue)
class Float(Token):
    def __init__(self, tokenValue):
        super().__init__("FLOAT", tokenValue)


##OPERATIONS
class Plus(Token):
    def __init__(self, tokenValue):
        super().__init__("PLUS", tokenValue)
class Minus(Token):
    def __init__(self, tokenValue):
        super().__init__("MINUS", tokenValue) 
class Slash(Token):
    def __init__(self, tokenValue):
        super().__init__("SLASH", tokenValue)
class Asterisk(Token):
    def __init__(self, tokenValue):
        super().__init__("ASTERISK", tokenValue)
class LeftParen(Token):
    def __init__(self, tokenValue):
        super().__init__("LEFT_PAREN", tokenValue)
class RightParen(Token):
    def __init__(self, tokenValue):
        super().__init__("RIGHT_PAREN", tokenValue)
class LeftBrace(Token):
    def __init__(self, tokenValue):
        super().__init__("LEFT_BRACE", tokenValue)
class RightBrace(Token):
    def __init__(self, tokenValue):
        super().__init__("RIGHT_BRACE", tokenValue)
class Semicolon(Token):
    def __init__(self, tokenValue):
        super().__init__("SEMICOLON", tokenValue)


##RESERVED
class Declaration(Token):
    def __init__(self, tokenValue):
        super().__init__("DECLARATION", tokenValue)
class If(Token):
    def __init__(self, tokenValue):
        super().__init__("IF", tokenValue)
class Elif(Token):
    def __init__(self, tokenValue):
        super().__init__("ELIF", tokenValue)
class Else(Token):
    def __init__(self, tokenValue):
        super().__init__("ELSE", tokenValue)
class While(Token):
    def __init__(self, tokenValue):
        super().__init__("WHILE", tokenValue)
class For(Token):
    def __init__(self, tokenValue):
        super().__init__("FOR", tokenValue)
class Show(Token):
    def __init__(self, tokenValue):
        super().__init__("SHOW", tokenValue)
class Blank(Token):
    def __init__(self, tokenValue):
        super().__init__("BLANK", tokenValue)
             
             
##BOLEANS             
class And(Token):
    def __init__(self, tokenValue):
        super().__init__("AND", tokenValue)
class Or(Token):
    def __init__(self, tokenValue):
        super().__init__("OR", tokenValue)

class Truee(Token):
    def __init__(self, tokenValue):
        super().__init__("TRUE", tokenValue)
class Falsee(Token):
    def __init__(self, tokenValue):
        super().__init__("FALSE", tokenValue)


##VARIABLES
class Variable(Token):
    def __init__(self, tokenValue):
        super().__init__("VARIABLE", tokenValue)


##COMPARISONS
class Comparison(Token):
    def __init__(self, tokenValue):
        super().__init__("COMPARISON", tokenValue)
class Greater(Token):
    def __init__(self, tokenValue):
        super().__init__("GREATER", tokenValue)
class Less(Token):
    def __init__(self, tokenValue):
        super().__init__("LESS", tokenValue)
class GreaterEqual(Token):
    def __init__(self, tokenValue):
        super().__init__("GREATER_EQUAL", tokenValue)
class LessEqual(Token):
    def __init__(self, tokenValue):
        super().__init__("LESS_EQUAL", tokenValue)
class EqualEqual(Token):
    def __init__(self, tokenValue):
        super().__init__("EQUAL_EQUAL", tokenValue)
class BangEqual(Token):
    def __init__(self, tokenValue):
        super().__init__("BANG_EQUAL", tokenValue)
class Assign(Token):
    def __init__(self, tokenValue):
        super().__init__("ASSIGN", tokenValue)


##COMMENT
class Comment(Token):
    def __init__(self, tokenValue):
        super().__init__("COMMENT", tokenValue)


##STRINGS
class String(Token):
    def __init__(self, tokenValue):
        super().__init__("STRING", tokenValue)

##UNKNOW
class Unknown(Token):
    def __init__(self, tokenValue):
        super().__init__("UNKNOWN", tokenValue)       