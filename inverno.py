#Aluno: Gustavo Donato - Questão: "bem-vindos e bem-vindas ao inverno"

while True:

    #inputs que capituram as temperaturas de cada dia
    a = int(input("digite a temperatura do primeiro dia:"))
    b = int(input("digite a temperatura do segundo dia:"))
    c = int(input("digite a temperatura do terceiro dia:"))

    #aqui barra o usuario caso ele coloque uma temperatura maior que 100 graus ou menor que -100 graus
    if a > 100 or a < (-100) or b > 100 or b < (-100) or c > 100 or c < (-100):
        print("Um dos valores digitados é maior que 100 ou menor que -100, por favor digite novamente")

    #sequencia de elifs para a verificação das temperaturas e da felicidade das pessoaqs naqueles 3 dias

    #coloquei este primeiro pois ele entrava em conflito com os seus anteriores, quando passei para frente ele deu certo
    elif a < b and c > b:
        if (b-a) > (c-b):
            print(":(")
            break

    #os demais a maioria funcionou, somente um não caiu no que deveria cair, e não encontrei o motivo

    elif b < a and c < b :
        if (a-b) > (b-c):
            print(":)")
            break

    elif b < a and b == c or c > b:
        print(":)")
        break

    elif b > a and  b == c or c < b:
        print(":(")
        break

    elif a < b and b < c:
        if (b-a) <= (c-b):
            print(":(")
            break

    elif b < a and c < b :
        if (a-b) <= (b-c):
            print(":(")
            break

    elif a == b and b < c:
        print(":)")
        break

    elif a == b and b > c:
        print(":(")
        break

    #alguns eu cheguei a levar a um novo if apos a verificçã, já que eles possuiam uma outra condição para ocorrer.

    #por fim coloquei uma carinha triste pois havia um que não estava caindo em nehum dos ifs, então cloque a carinha triste para este caso
    print(":(")
    break

    #foi um certo desafio, era uma questão de muita interpretação e que confundiu muito minha cabeça, mas dei o maximo e fiz o maximo que pude pra que todos os valores batessem