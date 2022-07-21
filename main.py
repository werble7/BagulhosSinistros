def dekey(processo):

    if "dekey" in processo[0]:
        lista = processo[0][8:].split()
        for i in range(int(lista[0])):
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
            dekey(filaProcesso)

        elif entrada == "stop":
            print(f"{len(filaProcesso)} processo(s) órfão(s).")
            break
