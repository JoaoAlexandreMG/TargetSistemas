def pesquisar_elemento(target: int):
    try:
        target = int(target)
    except ValueError:
        raise Exception("O parâmetro passado para a função não é um número!")
    pertence = False
    if target in (0, 1, 2):
        pertence = True
    a = 1
    b = 2
    while b < target:
        a, b = b, a + b

    if target == b:
        pertence = True
    return (
        f"{target} pertence a sequência"
        if pertence
        else f"{target} não pertence a sequência!"
    )


if __name__ == "__main__":
    NUMERO = 377
    print(pesquisar_elemento(NUMERO))
