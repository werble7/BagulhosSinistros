def dekey(processo):

    if 'dekey' in processo[0]:
        lista = processo[0][8:].split()
        x = int(lista[0])
        if x > len(lista):
            x = x % (len(lista) - 2)
            if x == 0:
                x = len(lista) - 2
        for i in range(x):
            if lista[1] < lista[2]:
                lista.append(lista[1])
                lista.pop(1)
            else:
                lista.append(lista[2])
                lista.pop(2)

        for i in range(len(lista)):
            if i != 0:
                print(lista[i], end="")

        print()
        processo.pop(0)


def scramble(processo):
    palavra = ''
    novaFrase = ''
    final = True
    frase = processo[0].split()

    for item in frase[2]:
        if item not in "()":
            palavra += item
        else:
            if palavra != '':
                if final:
                    novaFrase += palavra
                else:
                    novaFrase = palavra + novaFrase
            if item == "(":
                final = False
            else:
                final = True
            palavra = ''

    if palavra != '':
        if final:
            novaFrase += palavra
        else:
            novaFrase = palavra + novaFrase

    processo.pop(0)

    return novaFrase


if __name__ == '__main__':

    filaProcesso = []

    while True:
        entrada = input()

        if entrada[0:7] == "enqueue":

            for i in range(int(entrada[8:])):

                comando = input()

                if 'dekey' in comando or 'scramble' in comando:

                    pronto = False

                    if len(filaProcesso) == 0:
                        filaProcesso.append(comando)
                    else:
                        for j in range(len(filaProcesso)):
                            if int(comando[0]) < int(str(filaProcesso[j])[0]):
                                filaProcesso.insert(j, comando)
                                pronto = True
                                break
                        if not pronto:
                            filaProcesso.append(comando)

        elif entrada == "go":
            if len(filaProcesso) != 0:
                if 'dekey' in filaProcesso[0]:
                    dekey(filaProcesso)
                elif 'scramble' in filaProcesso[0]:
                    print(scramble(filaProcesso))

        elif entrada == "stop":
            print(f"{len(filaProcesso)} processo(s) órfão(s).")
            break
