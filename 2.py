def contar_as(string: str = "Assim sendo, trabalho na Target Sistemas, e você?"):
    qtd = {"A": 0, "a": 0}
    for item in string:
        if item in qtd:
            qtd[item] += 1
    return 'Aqui está a quantidade de vezes que a letra "A/a" aparece: ' + str(qtd)


if __name__ == "__main__":
    TEXTO = "Apois, colega, trabalho na Target Sistemas, e você?"
    print(contar_as(TEXTO))
