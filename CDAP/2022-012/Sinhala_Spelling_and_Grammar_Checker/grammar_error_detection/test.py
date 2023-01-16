import pandas as pd

data = []
corpus = dict()

def assign_data_tolist():
    with open(
            'C:/Users/49176/Desktop/CDAP/2022-012/Sinhala_Spelling_and_Grammar_Checker/grammar_error_correction/test.txt', 'r', encoding="utf8") as corpusFile:
        for line in corpusFile:
            corpus[line.strip().split(' ')[0]] = line.strip().split(' ')[1]


def main():

    assign_data_tolist()

    for y in range(0, corpus.__len__()):
        if list(corpus.values())[y] == "VNN" or list(corpus.values())[y] == "VP" or list(corpus.values())[y] == "VFM" or list(corpus.values())[y] == "AU" or list(corpus.values())[y] == "VNF" or list(corpus.values())[y]=="RPCV" or list(corpus.values())[y] == "SVCV":
            data.append(list(corpus.keys())[y])
    
    print(data)


main()
