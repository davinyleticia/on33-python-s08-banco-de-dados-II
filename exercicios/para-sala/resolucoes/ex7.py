import csv

with open('produtos.csv', newline='', encoding='utf-8') as csvfile:
    linhas = csv.reader(csvfile)
    for linha in linhas:
        print(linha)

