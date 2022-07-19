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
            continue
        elif entrada == "stop":
            break

    print(filaProcesso)
