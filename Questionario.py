import os
import platform

#Valor das Questões
lista_q = [4,2,3,2,3,3,2,2,3,4]

#Equipes
MER = [] #mudar para tudo minusculo
POR = []
AUD = []
DS  = []
NIS = []
BMW = []
JAG = []
VEN = []
MAH = []
NIO = []

Equipes = [MER,POR,AUD,DS,NIS,BMW,JAG,VEN,MAH,NIO]

Mer = " Mercedes-Benz " #mudar para tudo maiusculo
Por = " Porsche " 
Aud = " Audi "
Ds = " DS Automobil "
Nis = " Nissan "
Bmw = " BMW " 
Jag = " Jaguar "
Ven = " Venturi "
Mah = " Mahindra "
Nio = " NIO "


Pontos = [0,0,0,0,0,0,0,0,0,0,0]
Valor = [0,0,0,0,0,0,0,0,0,0]


#sistema de repetcao para utilizar variaveis de um array, que serão utilizadas para realizar um loop, loop qual faz com que o usuario insira uma alternativa valida

Q = ["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10"]

#Histórico de perguntas e respostas
historico = []

#definir função para limpar a tela
def limpar_tela():
    sistema = platform.system()

    if sistema == "Windows":
        os.system("cls")  # Para Windows
    else:
        os.system("clear")  # Para Unix-based (Linux, macOS)

#Boas-vindas
limpar_tela()
print("Bem-vindo ao jogo de Fórmula E!")
print("A Fórmula E é um campeonato de corridas de carros elétricos que reúne as principais equipes do mundo.")
print("Neste jogo, você irá responder a uma série de perguntas para descobrir qual equipe é a mais compatível com você.")
print("\nAs equipes participantes são: Mercedes-benz, Porsche, Audi, DS Automobil, Nissan, BMW, Jaguar, Venturi, Mahindra, NIO")
iniciar = int(input('\nDigite "1" para iniciar: '))
if iniciar == 1:
    Quiz_Realizado = True





while Quiz_Realizado:
    for j in range(0,10):
        Q[j] = True

    #Q1
    limpar_tela()

    while Q[0]:
        print("Questão 1 - Qual dessas atividades você mais gosta de fazer?")
        print(" 1- Cozinhar e experimentar novas receitas","\n 2- Jogar vídeo games e maratonar séries","\n 3- Explorar atividades ao ar livre, como andar de bicicleta","\n 4- Ler livros e assistir documentários")
        questão1 = int(input("Digite um número: "))

        if questão1 == 1:
            if lista_q [0] in lista_q:
                NIS.append(lista_q[0])
                JAG.append(lista_q[0])
                break

        elif questão1 == 2:
            if lista_q [0] in lista_q:
                MER.append(lista_q[0])
                AUD.append(lista_q[0])
                BMW.append(lista_q[0])
                break

        elif questão1 == 3:
            if lista_q [0] in lista_q:
                DS.append(lista_q[0])
                VEN.append(lista_q[0])
                NIO.append(lista_q[0])
                break

        elif questão1 == 4:
            if lista_q [0] in lista_q:
                POR.append(lista_q[0])
                MAH.append(lista_q[0])
                break

        else:
            print("\n Numero invalido")
    historico.append({"Questão": "Questão 1", "Resposta": questão1})
    #Q2
    limpar_tela()

    while Q[1]:
        print("Questão 2 - O que mais te instigaria na Fórmula E?")
        print(" 1- A Inovação tecnológica envolvida no campeonato","\n 2- A Sustentabilidade ambiental","\n 3- A Competição acirrada entre as equipes","\n 4- A História e tradição do campeonato","\n 5- Velocidade e desempenho")
        questão2 = int(input("Digite um número: "))

        if questão2 == 1:
            if lista_q [1] in lista_q:
                NIS.append(lista_q[1])
                JAG.append(lista_q[1])
                break

        elif questão2 == 2:
            if lista_q [0] in lista_q:
                MER.append(lista_q[1])
                AUD.append(lista_q[1])
                BMW.append(lista_q[1])
                break

        elif questão2 == 3:
            if lista_q [0] in lista_q:
                DS.append(lista_q[1])
                VEN.append(lista_q[1])
                NIO.append(lista_q[1])
                break

        elif questão2 == 4:
            if lista_q [1] in lista_q:
                POR.append(lista_q[1])
                MAH.append(lista_q[1])
                break

        elif questão2 == 5:
            if lista_q [1] in lista_q:
                BMW.append(lista_q[1])
                break
        else:
            print("\n Numero invalido\n")
    historico.append({"Questão": "Questão 2", "Resposta": questão2})

    #Q3
    limpar_tela()
    while Q[2]:

        print("Questão 3 - Qual é o seu estilo de vida?") 
        print(" 1- Urbano e Moderno","\n 2- Aventureiro ","\n 3- Sofisticado e Elegante ","\n 4- Consciente")
        questão3 = int(input("Digite um número: "))

        if questão3 == 1:
            if lista_q [2] in lista_q:
                DS.append(lista_q[2])
                NIS.append(lista_q[2])
                break
            
        elif questão3 == 2:
            if lista_q [2] in lista_q:
                VEN.append(lista_q[2])
                NIO.append(lista_q[2])
                break

        elif questão3 == 3:
            if lista_q [2] in lista_q:
                JAG.append(lista_q[2])
                AUD.append(lista_q[2])
                BMW.append(lista_q[2])
                break

        elif questão3 == 4:
            if lista_q [2] in lista_q:
                MAH.append(lista_q[2])
                MER.append(lista_q[2])
                break

        else:
            print("\n Numero Invalido")
    historico.append({"Questão": "Questão 3", "Resposta": questão3})


    #Q4
    while Q[3]:
        limpar_tela()
        print("Questão 4 - Alem da Formula E, qual outro tipo de modalidade que você acompanha?")
        print(" 1- Equipes da Fórmula 1", "\n 2- Equipes de endurance (WEC, Le Mans)", "\n 3- Equipes de rali (WRC, Dakar)","\n 4- Outros")
        questão4 = int(input("Digite um número: "))

        if questão4 == 1:
            if lista_q [3] in lista_q:
                MER.append(lista_q[3])
                POR.append(lista_q[3])
                break
            
        elif questão4 == 2:
            if lista_q [3] in lista_q:
                AUD.append(lista_q[3])
                NIS.append(lista_q[3])
                break

        elif questão4 == 3:
            if lista_q [3] in lista_q:
                DS.append(lista_q[3])
                BMW.append(lista_q[3])
                break

        elif questão4 == 4:
            if lista_q [3] in lista_q:
                JAG.append(lista_q[3])
                VEN.append(lista_q[3])
                NIO.append(lista_q[3])
                MAH.append(lista_q[3])
                break

        else:
            print("\n Numero Invalido")
    historico.append({"Questão": "Questão 4", "Resposta": questão4})

    #Q5
    
    while Q[4]:
        limpar_tela()
        print("Questão 5 - Quais tipos de veículos elétricos mais te atraem?")
        print(" 1- Os com tecnologia mais avançada","\n 2- Os que priorizam a redução da pegada de carbono","\n 3- Os com mais Desempenho e potência","\n 4- Os Economicos")
        questão5 = int(input("Digite um número: "))

        if questão5 == 1:
            if lista_q [4] in lista_q:
                MER.append(lista_q[4])
                POR.append(lista_q[4])
                AUD.append(lista_q[4])
                break
            
        elif questão5 == 2:
            if lista_q [4] in lista_q:
                MAH.append(lista_q[4])
                NIS.append(lista_q[4])
                break

        elif questão5 == 3:
            if lista_q [4] in lista_q:
                DS.append(lista_q[4])
                BMW.append(lista_q[4])
                break

        elif questão5 == 4:
            if lista_q [4] in lista_q:
                JAG.append(lista_q[4])
                VEN.append(lista_q[4])
                NIO.append(lista_q[4])
                break

        else:
            print("\n Numero Invalido")
    historico.append({"Questão": "Questão 5", "Resposta": questão5})
    #Q6
    while Q[5]:
        limpar_tela()
        print("Questão 6 - Você se identificaria mais com equipes mais pioneiras e tradicionais ou com novas equipes em ascensão?") 
        print(" 1- Equipes Pioneiras","\n 2- Novas equipes em ascensão")
        questão6 = int(input("Digite um número: "))

        if questão6 == 1:
            if lista_q [5] in lista_q:
                MER.append(lista_q[5])
                POR.append(lista_q[5])
                AUD.append(lista_q[5])
                JAG.append(lista_q[5])
                VEN.append(lista_q[5])
                DS.append(lista_q[5])
                BMW.append(lista_q[5])
                NIS.append(lista_q[5])
                break
            
        elif questão6 == 2:
            if lista_q [5] in lista_q:
                NIO.append(lista_q[5])
                MAH.append(lista_q[5])
                break

        else:
            print("\n Numero Invalido")
    historico.append({"Questão": "Questão 6", "Resposta": questão6})
        
    #Q7

    while Q[6]:
        limpar_tela()
        print("Questão 7 - Que tipo de patrocinadores das equipes você mais reconheceria?")
        print(" 1- Empresas Tecnologicas","\n 2- Marcas Automotivas","\n 3- Empresas Sustentáveis","\n 4- Outros")
        
        questão7 = int(input("Digite um número: "))

        if questão7 == 1:
            if lista_q [6] in lista_q:
                MER.append(lista_q[6])
                POR.append(lista_q[6])
                AUD.append(lista_q[6])
                break
            
        elif questão7 == 2:
            if lista_q [6] in lista_q:
                JAG.append(lista_q[6])
                BMW.append(lista_q[6])
                break

        elif questão7 == 3:
            if lista_q [6] in lista_q:
                MAH.append(lista_q[6])
                NIS.append(lista_q[6])
                break

        elif questão7 == 4:
            if lista_q [6] in lista_q:
                DS.append(lista_q[6])
                VEN.append(lista_q[6])
                NIO.append(lista_q[6])
                break

        else:
            print("\n Numero Invalido")
    historico.append({"Questão": "Questão 7", "Resposta": questão7})
    #Q8

    while Q[7]:
        limpar_tela()
        print("Questão 8 - Para qual tipo de equipe você torceria?")
        print(" 1- As equipes que ganham tudo","\n 2- Geralmente apoio equipes subestimadas ou azaradas","\n 3- Acompanho várias equipes, independentemente do desempenho")
        
        questão8 = int(input("Digite um número: "))

        if questão8 == 1:
            if lista_q [7] in lista_q:
                MER.append(lista_q[7])
                AUD.append(lista_q[7])
                break

        elif questão8 == 2:
            if lista_q [7] in lista_q:
                MAH.append(lista_q[7])
                DS.append(lista_q[7])
                break

        elif questão8 == 3:
            if lista_q [7] in lista_q:
                JAG.append(lista_q[7])
                BMW.append(lista_q[7])
                NIS.append(lista_q[7])
                POR.append(lista_q[7])
                NIO.append(lista_q[7])
                VEN.append(lista_q[7])
                break

            else:
                print("\n Numero Invalido")
    historico.append({"Questão": "Questão 8", "Resposta": questão8})
    #Q9
    while Q[8]:
        limpar_tela()
        print("Questão 9 - Qual é a sua visão de sucesso na Fórmula E?")
        print(" 1- Vitórias e títulos de campeonato","\n 2- Desenvolvimento de tecnologia inovadora","\n 3- Contribuição para a conscientização dos veículos elétricos")
        questão9 = int(input("Digite um número: "))

        if questão9 == 1:
            if lista_q [8] in lista_q:
                MER.append(lista_q[8])
                POR.append(lista_q[8])
                AUD.append(lista_q[8])
                break
            
        elif questão9 == 2:
            if lista_q [8] in lista_q:
                MAH.append(lista_q[8])
                DS.append(lista_q[8])
                BMW.append(lista_q[8])
                break
            

        elif questão9 == 3:
            if lista_q [8] in lista_q:
                JAG.append(lista_q[8])
                NIS.append(lista_q[8])
                NIO.append(lista_q[8])
                VEN.append(lista_q[8])
                break

        else:
            print("\n Numero Invalido")
    historico.append({"Questão": "Questão 9", "Resposta": questão9})
    #Q10
    while Q[9]:
        limpar_tela()
        print("Questão 10 -Qual o estilo de música que você mais gosta?")
        print(" 1- Rock ou Alternativa","\n 2- Pop ou Eletrônica","\n 3- Clássica ou Jazz","\n 4- Hip Hop ou Reggae")
        questão10 = int(input("Digite um número: "))

        if questão10 == 1:
            if lista_q [9] in lista_q:
                MER.append(lista_q[9])
                POR.append(lista_q[9])
                AUD.append(lista_q[9])
                break
            
        elif questão10 == 2:
            if lista_q [9] in lista_q:
                MAH.append(lista_q[9])
                DS.append(lista_q[9])
                BMW.append(lista_q[9])
                break
            

        elif questão10 == 3:
            if lista_q [9] in lista_q:
                JAG.append(lista_q[9])
                NIS.append(lista_q[9])
                NIO.append(lista_q[9])
                VEN.append(lista_q[9])
                break
            
        elif questão10 == 4:
            if lista_q [9] in lista_q:
                VEN.append(lista_q[9])
                MAH.append(lista_q[9])
                break

        else:
            print("\n Numero Invalido")
    historico.append({"Questão": "Questão 10", "Resposta": questão10})

    #Transferindo os valores das questões para os pontos totais das equipes
    for i in range (0,9):
        Pontos[i] = 0
        for Valor[i] in Equipes[i]:
            Pontos[i] += Valor[i]

    #Realizando a soma dos pontos, para assim utilizarmos porcentagem em nosso projeto
    soma = 0
    PontosSoma = []
    for i in range (0,9):
        PontosSoma.append(lista_q[i])
    for PontosSoma in lista_q:
        soma += PontosSoma

    #Montando o Esquema das equipes com os retrospectivos nomes e pontos por meio de um novo array
    EquipesNomes = [Mer, Por, Aud, Ds , Nis, Bmw, Jag, Ven, Mah, Nio] 
    Marcas = []
    for i in range (0, 10):
        Marcas.append((EquipesNomes[i], round((Pontos [i] / soma)*100)))

    Maior_Marca = None #uso para criar uma variavel vazia, assim como no for
    Maior_Pontuacao = -1 #uso do -1 para evitar erro de resposta caso todos os valores sejam = 0

    #condicional feita para que apareca a marca com maior valor
    for EquipesNomes, Pontos in Marcas:
        if Pontos > Maior_Pontuacao:
            Maior_Marca = EquipesNomes
            Maior_Pontuacao = Pontos
    limpar_tela()
    print("A Equipe que você tem mais afinidade é a Equipe do(a):",Maior_Marca,"com",Maior_Pontuacao,"% de afinidade")

    if Maior_Marca == Mer:
        print('\n Você é uma pessoa que valoriza a precisão, o foco e a excelência em tudo o que faz. Assim como a Mercedes-Benz, você busca sempre o melhor desempenho e está sempre pronto para competir e vencer. E existem influenciadores que pensaram igual você, como: Henry Cavill (ator e gamer), Tom Ford (designer de moda e cineasta), e Calvin Harris (DJ e produtor musical).')
    elif Maior_Marca == Por:
        print('\n Você é inovador e adora explorar novas fronteiras, seja em tecnologia ou em aventuras. Assim como a Porsche, você busca sempre desafiar os limites e pensar fora da caixa. \n Os Influenciadores que compartilham desses valores são: Elon Musk (CEO da Tesla e SpaceX), Billie Eilish (cantora e compositora).')
    elif Maior_Marca == Aud:
        print('\n Você adora se divertir e manter a competitividade em alta. Para você, a vida é melhor quando está rodeado de amigos e aproveitando momentos únicos. \n Alguns Influencers que compartilham desse mesmo aspectos são: Ryan Reynolds (ator e empresário), Logan Paul (criador de conteúdo), e Dave Grohl (músico e vocalista).')
    elif Maior_Marca == Ds:
        print('\n Você valoriza o equilíbrio e a harmonia em sua vida. Assim como a DS, você acredita que a sofisticação e a elegância são essenciais. \n Influenciadores que pensam igual você: Emma Watson (atriz e ativista), Norah Jones (cantora e compositora), e Oprah Winfrey (apresentadora de TV e empresária).')
    elif Maior_Marca == Nis:
        print('\n Você é versátil e sempre está pronto para se adaptar a novas situações. Assim como a Nissan, você busca eficiência e inovação em tudo o que faz. \n As celebridades que pensam como você são: Stanley Tucci (ator e entusiasta da culinária), Keanu Reeves (Ator e Celebridade), e Tame Impala (projeto musical de Kevin Parker).')
    elif Maior_Marca == Bmw:
        print('\n Você aprecia a perfeição e a atenção aos detalhes. Para você, a qualidade é essencial, e você não se contenta com menos do que o melhor. Influenciadores que pensam como você: David Beckham (Ex-jogador de futebol e ícone da moda), Neil Patrick Harris (ator e entusiasta das artes), e Daniel Craig (Ator).')
    elif Maior_Marca == Jag:
        print('\n Você é aventureiro e adora descobrir novas experiências. Assim como a Jaguar, você valoriza a elegância e a emoção em tudo o que faz. \n Influenciadores que tem essas características:  Taylor Swift (cantora e compositora), e Tom Holland (ator e aventureiro), Chris Hemsworth (ator e entusiasta de esportes e aventura).')
    elif Maior_Marca == Ven:
        print('\n Você é criativo e adora explorar novas ideias e projetos. Assim como a Venturi, você está sempre buscando maneiras de inovar e se expressar. \n Influenciadores que pensam igual:  Kendrick Lamar (rapper e compositor), e Rich Roll (atleta e autor de fitness), Adam Savage (criador de MythBusters).')
    elif Maior_Marca == Mah:
        print('\n Você é um defensor do meio ambiente e acredita que a sustentabilidade é o caminho para o futuro. Assim como a Mahindra, você está comprometido em fazer a diferença no mundo.  \n Influencers que também são assim: Leonardo DiCaprio (ator e ativista ambiental), Greta Thunberg (ativista ambiental), e Damian Marley (cantor e músico).')
    elif Maior_Marca == Nio:
        print('\n Você é inovador e gosta de pensar fora da caixa. Assim como a NIO, você busca soluções criativas e está sempre pronto para enfrentar desafios. \n Influenciadores que compartilham desses valores incluem Johnny Depp (ator e músico), Mark Rober (engenheiro e criador de conteúdo), Hans Zimmer (compositor de trilhas sonoras).')
    else:
        print('deu bolete')

    print('')
    ver_historico = int(input('Para visualizar o histórico digite "1": '))
    if ver_historico == 1:
        limpar_tela()
        print("\nHistórico de perguntas e respostas:")
        for item in historico:
            print(f"Questão: {item['Questão']}")
            print(f"Resposta: {item['Resposta']}")
            print("------------------------")
    else:
        limpar_tela()
        print('Obrigado por jogar! Fim de jogo!')

    Quiz_Realizado = False
