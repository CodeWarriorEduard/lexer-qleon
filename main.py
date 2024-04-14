from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from QleonLexerImpl import QleonLexer


app = FastAPI()


origins = [
    "https://frontendqleon.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  
    allow_methods=["GET", "POST", "OPTIONS"],  
    allow_headers=["Content-Type", "Authorization"],  
)

Qleon = QleonLexer() # Instancia de la implementación de nuestro lexer.

@app.get("/")
def test_connection():
    return {"Message":"Test ran successfully"}


@app.post("/code")
def get_code_from_user(code:str):
    tokens = Qleon.run(code)
    tokenList = []
    
    tokenData = ""
    maxLine = tokens[-1].getLine()
    tokenData += f"\nLEXEMA:[\n\n" 
    posLastTokenViewed = 0
    tab = "\t"
    for line in range(1,maxLine+1):
        tokenData += f"{tab}Content Line {line}:[\n" 
        listTokenLine = []
        for lineTokens in range(posLastTokenViewed, len(tokens)):
            posLastTokenViewed = lineTokens
            
            if tokens[lineTokens].getLine() == line:
                tokenData += f"{tab+tab}[{tokens[lineTokens].tokenComplete()}]\n"
                listTokenData = [tokenData]
                listTokenLine.append(listTokenData)
            else:
                break

        tokenList.append[listTokenLine]
        tokenData += f"{tab}]\n\n"           
    tokenData +="]"
 
    return tokenList