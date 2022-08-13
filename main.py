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
        self.tamanho = 0

    def addProcesso(self, processo):
        # vazio
        if self.primeiro is None:

            self.primeiro = processo
            self.ultimo = processo

        # prioridade do ultimo menor ou igual ao processo
        elif self.ultimo.prioridade <= processo.prioridade:
            self.ultimo.prox = processo
            self.ultimo = processo

        # um elemento
        elif self.primeiro == self.ultimo:

            # prioridade do processo de dentro menor ou igual
            if self.primeiro.prioridade <= processo.prioridade:
                self.primeiro.prox = processo
                self.ultimo = processo

            # prioridade do processo de fora menor
            else:
                self.primeiro = processo
                processo.prox = self.ultimo

        # dois ou mais
        else:
            anterior = None
            atual = self.primeiro

            while True:

                # se a prioridade atual for maior, processo adicionado antes deste
                if atual.prioridade > processo.prioridade:

                    # se o anterior for o primeiro
                    if anterior is None:
                        self.primeiro = processo
                        processo.prox = atual

                    # se não
                    else:
                        anterior.prox = processo
                        processo.prox = atual

                    break

                # se a prioridade for menor ou igual, continua o loop
                else:
                    anterior = atual

                    if atual.prox is not None:
                        atual = atual.prox

                    else:
                        break

        self.tamanho += 1

    def removeProcesso(self):
        # verifica se está vazio
        if self.primeiro is not None:

            # verifica se tem apenas um item
            if self.primeiro.prox is not None:
                self.primeiro = self.primeiro.prox

            else:
                self.primeiro = None

            self.tamanho -= 1


def dekey(fila):

    processo = fila.primeiro.comando

    lista = processo[8:].split()
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

    for j in range(len(lista)):
        if j != 0:
            print(lista[j], end="")

    print()
    fila.removeProcesso()


def scramble(fila):

    palavra = ''
    novaFrase = ''
    final = True
    frase = fila.primeiro.comando.split(" ", 2)

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

    fila.removeProcesso()

    print(novaFrase)


if __name__ == '__main__':

    fila = FilaDeProcessos()

    while True:
        entrada = input()

        if entrada[0:7] == "enqueue":

            for i in range(int(entrada[8:])):

                comando = input()

                if comando != 'go' and comando != 'stop':
                    partes = comando.split()

                    if ('dekey' in partes[1] or 'scramble' in partes[1]) and 0 <= int(partes[0]) <= 5:

                        temp = Processo(comando, int(comando[0]))
                        fila.addProcesso(temp)

                else:
                    entrada = comando
                    break

        if entrada == "go":
            if fila.primeiro is not None:
                if 'scramble' in fila.primeiro.comando:
                    scramble(fila)
                elif 'dekey' in fila.primeiro.comando:
                    dekey(fila)

        if entrada == "stop":
            print(f"{fila.tamanho} processo(s) órfão(s).")
            break
