class Processo:
    def __init__(self, comando, prioridade):
        self.comando = comando
        self.prioridade = prioridade
        self.prox = None

    def __str__(self):
        return self.comando


class FilaDeProcessos:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def addProcesso(self, processo):
        if self.primeiro is None:

            self.primeiro = processo
            self.ultimo = processo

        elif self.primeiro == self.ultimo:

            if self.primeiro.prioridade <= processo.prioridade:
                self.ultimo.prox = processo
                self.ultimo = processo

            else:
                processo.prox = self.primeiro
                self.primeiro = processo

        elif processo.prioridade == 5:

            self.ultimo.prox = processo
            self.ultimo = processo

        else:

            anterior = None
            atualAdd = self.primeiro
            achado = False

            while True:
                if atualAdd.prioridade == processo.prioridade + 1:
                    processo.prox = atualAdd
                    if anterior is not None:
                        anterior.prox = processo
                    else:
                        self.primeiro = processo
                    break

                anterior = atualAdd
                if atualAdd.prox is not None:
                    atualAdd = atualAdd.prox

                else:
                    self.ultimo.prox = processo
                    self.ultimo = processo
                    break


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

    fila = FilaDeProcessos()

    while True:
        entrada = input()

        if entrada[0:7] == "enqueue":

            for i in range(int(entrada[8:])):

                comando = input()

                if 'dekey' in comando or 'scramble' in comando:

                    temp = Processo(comando, int(comando[0]))
                    fila.addProcesso(temp)

        elif entrada == "go":
            atual = fila.primeiro
            while True:
                print(atual)
                if atual.prox is not None:
                    atual = atual.prox
                else:
                    print("fim")
                    break

        elif entrada == "stop":
            break

        '''
        elif entrada == "go":
            if len(filaProcesso) != 0:
                if 'dekey' in filaProcesso[0]:
                    dekey(filaProcesso)
                elif 'scramble' in filaProcesso[0]:
                    print(scramble(filaProcesso))

        elif entrada == "stop":
            print(f"{len(filaProcesso)} processo(s) órfão(s).")
            break
        '''