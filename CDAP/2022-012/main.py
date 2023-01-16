from typing import List
from fastapi import FastAPI
import Sinhala_Spelling_and_Grammar_Checker.grammar_error_detection.error_detection as getRequest

from Sinhala_Spelling_and_Grammar_Checker.grammar_error_detection.models.grammar_model import GrammarModel

# create a instance
app = FastAPI()

app.add_middleware(
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# get api call for subject analysis
#code to run : python -m uvicorn main:app --reload

@app.post("/sentence/detect/")
def grammar_error_detection(grammar: GrammarModel):
    # print(grammar_errors.grammar)
    #print(len(grammar.grammar))
    return (getRequest.grammar_detection(grammar.grammar))
