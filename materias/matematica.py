from utils.lines import *
import random
from menus.quiz import *


# Dados
def matematica():
    title = f"{b}Matemática{rt}"
    data = {
        f"{g}Cálculo Básico{rt}": calculoBasico,
        f"{b}Porcentagem{rt}": porcentagem,
        f"{r}Média{rt}": "media",
        f"{m}Logaritmo{rt}": "logaritmo",
        f"{m}Fatorial{rt}": "fatorial",
    }
    return title, data


# Assuntos
def porcentagem():
    title = f"{b}Porcentagem{rt}"
    texto = [
        f"{b}Porcentagem{rt} é uma forma de expressar uma parte de um todo em termos percentuais.\n\n{r}Macete{rt}: Para calcular a porcentagem de um valor, {r}multiplique o valor pela porcentagem{rt} e {g}mova a vírgula duas posições para a frente{rt}.\nPor exemplo, {r}20 alunos{rt},{g}35% são mulheres{rt}. 20 x 35 = 700.\nPortanto, 35% de 20 alunos são 7 alunas.",
        f"Para encontrar a {r}parte complementar{rt} (porcentagem restante),\nsubtraia a porcentagem conhecida de 100%. Por exemplo, se 35% são mulheres,\n\n100% - 35% = 65% são homens.\n20 x 65 = 1300\n\nAssim, em 20 alunos, 65% são homens, o que equivale a 13 alunos.",
        f"{r}Para encontrar o valor original{rt} de um numero com aumento em porcentagem.\n\n{r}[Valor com aumento]{g}/{r}(100+x%){rt}\n\nExemplo:\nSe um trabalhador tivesse {g}7% de aumento{rt} do seu {r}salario atual{rt} receberia {b}R$ 2.675,00{rt}.\n\n2675/(100+7)\n2675/107 = 2500\nValor do salario atual = 2500",
    ]

    q = quizporcentagem

    return (title, texto, q)


def quizporcentagem():
    title = f"{b}Porcentagem{rt}"
    x = random.randint(1, 101)
    y = random.randint(1, 101)

    r_correta = (x * y) / 100

    quiz = {
        f"{r}{x}%{rt} de {g}{y}{rt} é?": f"{x} X {y} = {x*y}\n{x*y}/{100} = {(r_correta):.2f}",
        f"{g}{x}{rt} é quanto de {r}{y}%{rt}?": f"{x} X {y} = {x*y}\n{x*y}/{100} = {(r_correta):.2f}",
    }

    return (title, quiz, x, y, r_correta)


####
def calculoBasico():
    title = f"{g}Cálculo Básico{rt}"
    texto = [
        f"{g}P: P{rt}arênteses (resolva as operações dentro dos {g}parênteses{rt} primeiro)\n{c}E: E{rt}xpoente (realize as operações com {c}expoentes{rt})\n{r}M: M{rt}ultiplicação (efetue as {r}multiplicações{rt})\n{r}D: D{rt}ivisão (faça as {r}divisões{rt})\n{m}A: A{rt}dição (realize as {m}adições{rt})\n{m}S: S{rt}ubtração (efetue as {m}subtrações){rt}\n",
        f"Macetes para Frações Decimais\nConverter para Fração: Coloque o número decimal sobre uma potência de 10 apropriada\n(por exemplo, 0,25 = 25/100 = 1/4)",
    ]
    q = quizcbasico

    return (title, texto, q)


def quizcbasico():
    title = f"{g}Cálculo Básico{rt}"

    x = round(random.uniform(1, 101), 2)
    y = round(random.uniform(1, 101), 2)

    operadores = ["+", "-", "*", "/"]
    operador = random.choice(operadores)

    def calcular(x, y, operador):
        if operador == "+":
            r_correta = x + y
        elif operador == "-":
            r_correta = x - y
        elif operador == "*":
            r_correta = x * y
        elif operador == "/":
            r_correta = x / y

        return r_correta, operador

    r_correta, operador = calcular(x, y, operador)

    quiz = {
        f"{r}{x}{rt} {operador} {g}{y}{rt} é?": f"{r}{x}{rt} {operador} {g}{y}{rt} = {r_correta}",
    }

    return title, quiz, x, y, r_correta
