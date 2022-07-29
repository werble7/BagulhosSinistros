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
            atual = self.primeiro
            achado = False

            while True:
                if atual.prioridade == processo.prioridade + 1:
                    processo.prox = atual
                    if anterior is not None:
                        anterior.prox = processo
                    else:
                        self.primeiro = processo
                    break

                anterior = atual
                if atual.prox is not None:
                    atual = atual.prox

                else:
                    self.ultimo.prox = processo
                    self.ultimo = processo
                    break

    def removeProcesso(self):
        if self.primeiro is not None:
            if self.primeiro.prox is not None:
                self.primeiro = self.primeiro.prox
            else:
                self.primeiro = None

    def count(self):
        cont = 0
        atual = self.primeiro
        if atual is not None:
            while True:
                cont += 1
                if atual.prox is not None:
                    atual = atual.prox
                else:
                    break
        return cont


def dekey(fila):

    processo = fila.primeiro.comando

    if 'dekey' in processo:
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

        for i in range(len(lista)):
            if i != 0:
                print(lista[i], end="")

        print()
        fila.removeProcesso()


def scramble(fila):
    palavra = ''
    novaFrase = ''
    final = True
    frase = fila.primeiro.comando.split()

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
                partes = comando.split()

                if ('dekey' in partes[1] or 'scramble' in partes[1]) and 0 <= int(partes[0]) <= 5:

                    temp = Processo(comando, int(comando[0]))
                    fila.addProcesso(temp)

        elif entrada == "go":
            if fila.primeiro is not None:
                if 'scramble' in fila.primeiro.comando:
                    scramble(fila)
                elif 'dekey' in fila.primeiro.comando:
                    dekey(fila)

        elif entrada == "stop":
            print(f"{fila.count()} processo(s) órfão(s).")
            break
