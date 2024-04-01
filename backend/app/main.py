from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from QleonLexerImpl import QleonLexer


app = FastAPI()


origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

Qleon = QleonLexer() # Instancia de la implementación de nuestro lexer.

@app.get("/")
def test_connection():
    return {"Message":"Test ran successfully"}


@app.post("/code")
def get_code_from_user(code:str):
    output = Qleon.run(code)
    o = []
    for i in output:
        o.append([i._Token__tokenValue,i._Token__tokenType])
    return o