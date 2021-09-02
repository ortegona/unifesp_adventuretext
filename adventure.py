inventario = {"chave pequena": False, "chave mestra": False}

#Funções
def mostrar_inventario():
    for itens in inventario:
        print(itens)
def cls():
    print("\n" * 2)

def historia():
    print('''Em uma ensolarada manhã de verão, você e seus amigos notam nas redes sociais da prefeitura local
    que havia acabado de começar uma exposição no museu municipal de grandes nomes da arte, como Picasso e da Vinci. 
    Como bons amantes da arte, vocês decidem ir imediatamente ao local para garantir os seus ingressos. O dia estava feito! 
    Ao comprarem suas entradas, aproveitaram a exposição com muito encanto e diversão, sempre discutindo sobre suas obras favoritas
    e conversando por horas a fio. O dia foi se estendendo, a noite chegando... Você se sente exausto após caminhar por todo esse museu! 
    Ao fim da exposição, você e seus companheiros se preparam para regressarem às suas casas. Enquanto espera seus amigos voltarem do 
    banheiro para que todos se despeçam e partam, você decide encostar em um dos bancos da exposição para relaxar. Mente nublada, olhos 
    pesados e sentindo aquele frio de fim de tarde chegando, você cochila. Um cochilo rápido, certo? Errado! Ao acordar depois deste descanso,
    você se depara no mesmo lugar que encostou, porém com o museu completamente em silêncio e com quase todas as luzes apagadas! Te deixaram
    para trás com apenas sua mochila! Você deve encontrar a saída o mais rápido o possível! ''')

def intro02():
    cls()
    intro_opções = ["1", "2", "3", "4"]
    escolha = ""
    while escolha not in intro_opções:
        print(''' \nVocê voltou ao salão principal do museu! Ao analisar seus arredores, você se depara com 3 caminhos possíveis a se seguirem. Qual será sua escolha?
                    1. Seguir à frente, em direção à um longo corredor;
                    2. Seguir à direita, em direção à um corredor estreito;
                    3. Seguir à esquerda, em direção à uma porta azul para abri-la. 
               ''')

        escolha = str(input("Selecionar opção número: "))
    print("Você selecionou o caminho " + escolha)
    if escolha == intro_opções[0]:
        room01()
    elif escolha == intro_opções[1]:
        room02()
    elif escolha == intro_opções[2]:
        room03()
    elif escolha == intro_opções[3]:
        intro02()
        mostrar_inventario()


def intro():
    historia()
    intro_opções = ["1","2","3","4"]
    escolha =""
    while escolha not in intro_opções:
        print(''' \nAparentemente, você está no salão principal do museu! Ao analisar seus arredores, você se depara com 3 caminhos possíveis a se seguirem. Qual será sua escolha?
            1. Seguir à frente, em direção à um longo corredor;
            2. Seguir à direita, em direção à um corredor estreito;
            3. Seguir à esquerda, em direção à uma porta azul para abri-la. 
       ''')

        escolha = str(input("Selecionar opção número: "))
    print("Você selecionou o caminho " + escolha)
    if escolha == intro_opções[0]:
        room01()
    elif escolha == intro_opções[1]:
        room02()
    elif escolha == intro_opções[2]:
        room03()
    elif escolha == intro_opções[3]:
        intro02()
        mostrar_inventario()


def room03():
    cls()
    opçoes3 = ["uhul"]
    escolha03 =""
    while escolha03 not in opçoes3:
        print("Você se dirige à porta azul e pega em sua maçaneta. Girando-a aos poucos, percebe que a porta não está trancada. \nAproveitando disso, você entra na sala cuidadosamente, causando um alto som arranhado ao abrir a porta.")
        print("Em questão de momentos após abrir a porta, a sala que você acabou de entrar é subitamente iluminada e a porta é fechada, revelando várias monstruosidades infestando a área!")
        print("Não foi necessário mais do que segundos para que você percebesse que estas criaturas saíram diretamente das obras de arte expostas! Elas ganharam vida à noite!")
        print("Em choque diante do que você está presenciando, você se torna imóvel, dominado pelo medo! As criaturas se aproveitam de sua vulnerabilidade e te atacam impiedosamente!")
        print("\n --------> G A M E      O V E R <--------")
        escolha03 = str(input('''Digite "uhul" para recomeçar o game!'''))
    print("Reiniciando o game!")
    if escolha03 == opçoes3[0]:
        intro()


def room01():
    cls()
    room01_opção = ["sim","s","SIM","Sim"]
    escolha01 =""
    while escolha01 not in room01_opção:
        print("Você caminha até o fim do corredor. \nTrata-se apenas de um corredor cheio de estátuas antigas e pouco iluminadas por pequenos focos de luzes, mas não há saída! \nPorém, você nota que há uma chave pequena jogada no chão! Talvez seja útil?")
        print("--> Você adicionou chave pequena à sua mochila.")

        escolha01 = str(input("Voltar ao salão principal? "))
    print("Você decidiu voltar ao salão principal")
    if escolha01 == room01_opção[0]:
        inventario['chave pequena'] = True
        intro02()
    elif escolha01 == room01_opção[1]:
        inventario['chave pequena'] = True
        intro02()
    elif escolha01 == room01_opção[2]:
        inventario['chave pequena'] = True
        intro02()
    elif escolha01 == room01_opção[3]:
        inventario['chave pequena'] = True
        intro02()


def room02():
    cls()
    room02_opções = ["1","2","3","4"]
    escolha02 =""
    while escolha02 not in room02_opções:
        print("\nVocê segue à direita, atravessando por várias pinturas macabras ao longo do estreito corredor! \nSinto que elas estão me olhando... Parecem até vivas!")
        print("Ao fim do caminho, você se depara com 3 novas opções de passagem! O que você fará agora? \n 1. Seguir à direita, em direção à um novo corredor; \n 2. Seguir à frente, em direção à uma porta preta; \n 3. Seguir à esquerda, em direção à uma porta laranja; \n 4. Voltar ao salão principal.")
        escolha02 = str(input("Selecionar opção número: "))
    print("Você selecionou caminho " + escolha02)
    if escolha02 == room02_opções[0]:
        room04()
    elif escolha02 == room02_opções[1]:
        room05()
    elif escolha02 == room02_opções[2]:
        room06()
    elif escolha02 == room02_opções[3]:
        intro02()
def room06():
    cls()
    room06_opções = ["1","2","3"]
    escolha06 =""
    while escolha06 not in room06_opções:
        print('''Ao se dirigir à porta laranja, você se depara com uma placa nesta escrita "Sala de Funcionários".''')
        print("Afim de verificar se a porta estava aberta, você pressiona contra a maçaneta, mas sem sucesso! A porta está trancada!\nSinto que há algo importante dentro dessa sala...")
        print("Como você vai prosseguir agora? ")
        print(" 1. Utilizar uma chave pequena para abrir a porta.")
        print(" 2. Tentar forçar a entrada da sala com o seu corpo.")
        print(" 3. Voltar ao corredor estreito anterior")
        escolha06 = str(input("Selecionar opção número: "))
    print("Você selecionou a opção " + escolha06)
    if escolha06 == room06_opções[0]:
        if inventario['chave pequena']:
            funcionario()
        else:
            print("\nOps! Parece que você ainda não tem a chave necessária para abrir essa sala...")
            room06()
    elif escolha06 == room06_opções[1]:
        semsucesso2()
    elif escolha06 == room06_opções[2]:
        room02()

def funcionario():
    cls()
    opçoesfunc = ["sim","s","SIM","Sim"]
    escolhafuncionario =""
    while escolhafuncionario not in opçoesfunc:
        print("Ufa! A chave pequena funcionou!")
        print("Você adentra a sala dos funcionários lentamente, deparando-se com uma típica área de escritório vazia. Há computadores espalhados, cadeiras e uma grande mesa.")
        print("Analisando atentamente cada detalhe da sala, você percebe que há uma grande chave mestra apoiada na mesa! Talvez seja a chave da saída!")
        print("Num piscar de olhos, você agarra a chave e a guarda com muito cuidado.")
        print('''--> Você adicionou"Chave Mestra" à sua mochila''')
        escolhafuncionario = str(input("Voltar ao à entrada da porta laranja? "))
    print("Você voltou para a entrada da porta laranja.")
    if escolhafuncionario == opçoesfunc[0]:
        inventario['chave mestra'] = True
        room06()
    if escolhafuncionario == opçoesfunc[1]:
        inventario['chave mestra'] = True
        room06()
    if escolhafuncionario == opçoesfunc[2]:
        inventario['chave mestra'] = True
        room06()
    if escolhafuncionario == opçoesfunc[3]:
        inventario['chave mestra'] = True
        room06()

def room05():
    cls()
    opçoes5 = ["uhul"]
    escolha05 = ""
    while escolha05 not in opçoes5:
        print("Ao se direcionar à porta preta e pegar em sua maçaneta, você percebe que essa porta está aberta!")
        print("Abrindo-a cuidadosamente, você adentra aos poucos em uma sala repleta de estátuas gregas antigas! Elas são lindas mas não há nada de útil no quarto além delas!")
        print("Frustado, você decide voltar ao local que estava antes, mas, ao tentar abrir a porta para sair, percebe que ela se trancou sozinha!")
        print("Em questão de segundos, todas as luzes do quarto se apagaram e sons de mármore se movendo ecoaram pelo local. As estátuas estavam vivas!")
        print("Apesar de seus esforços para tentar abrir a porta desesperadamente, tudo foi em vão! As estátuas te atacaram violentamente.")
        print("\n --------> G A M E      O V E R <--------")
        escolha05 = str(input('''Digite "uhul" para recomeçar o game!'''))
    print("Reiniciando o game!")
    if escolha05 == opçoes5[0]:
        intro()

def room04():
    cls()
    room04_opções = ["1","2","3"]
    escolha04 =""
    while escolha04 not in room04_opções:
        print("Um pouco amedrontado, você segue ao corredor à direita.\nApós poucos segundos caminhando pela área de pobre iluminação, você se depara com uma grande porta. É a porta da saída!\nNum ato de desespero, você agarra à maçaneta da porta e a gira, mas sem sucesso! A porta está trancada.")
        print("E agora, o que você gostaria de fazer?\n1.Utilizar uma chave mestra para abrí-la.\n2.Tentar empurrar a porta com toda a força que conseguir!\n3.Voltar ao corredor estreito.")
        escolha04 = str(input("Selecionar opção número: "))
    print("Você selecionou a opção" + escolha04)
    if escolha04 == room04_opções[0]:
        if inventario['chave mestra']:
            room08()
        else:
            print("Ops! Parece que você não tem a chave mestra para abrir a saída do museu...")
            room04()
    elif escolha04 == room04_opções[1]:
        semsucesso()
    elif escolha04 == room04_opções[2]:
        room02()
def room08():
    cls()
    print('''Ao ouvir o clique da chave mestra assim que a porta da saída é destrancada, o seu coração dispara!''' )
    print('''Você não se segura de emoção e escancara a porta de saída, empurrando-a de uma vez. "Finalmente livre!", você pensa.''')
    print('''E é no meio de toda essa emoção que você acorda. Isso mesmo, acorda no mesmo lugar que havia cochilado no museu!
    Tudo não havia passado de um sonho! 
    Ao abrir os olhos, você se depara com todos os seus amigos rindo da sua cara de sono e assustada, sem entender o que estava acontecendo mas absolutamente
    aliviado que tudo isso havia sido apenas um pesadelo resultado de um rápido cochilo.''')
    print("\n \n ------------> GOOD ENDING! FIM DO JOGO! <------------ ")

def semsucesso():
    cls()
    opçoessucesso1 = ["sim","s","SIM","Sim"]
    escolhasucesso1 =""
    while escolhasucesso1 not in opçoessucesso1:
        print("Essa ação não teve efeito algum! Que pena.")
        escolhasucesso1 = str(input("Voltar a analisar as outras opções? "))
    print("Você decidiu voltar a analisar as outras opções.")
    if escolhasucesso1 == opçoessucesso1[0]:
        room04()
    if escolhasucesso1 == opçoessucesso1[1]:
        room04()
    if escolhasucesso1 == opçoessucesso1[2]:
        room04()
    if escolhasucesso1 == opçoessucesso1[3]:
        room04()

def semsucesso2():
    cls()
    opçõessucesso = ["sim","s","SIM","Sim"]
    escolhasucesso2 =""
    while escolhasucesso2 not in opçõessucesso:
        print("Essa ação não teve efeito algum! Que pena.")
        escolhasucesso2 = str(input("Voltar a analisar as outras opções? "))
    print("Você decidiu voltar a analisar as outras opções.")
    if escolhasucesso2 == opçõessucesso[0]:
        room06()
    if escolhasucesso2 == opçõessucesso[1]:
        room06()
    if escolhasucesso2 == opçõessucesso[2]:
        room06()
    if escolhasucesso2 == opçõessucesso[3]:
        room06()
#Programa primário
intro()

