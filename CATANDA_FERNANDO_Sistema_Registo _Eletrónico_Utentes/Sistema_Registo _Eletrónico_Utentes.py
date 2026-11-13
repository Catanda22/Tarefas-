
# QUESTAO 2
# SISTEMA DE REGISTO ELETRONICO DE UTENTES

# Lista para guardar os utentes
utentes = []

def registar_utente():

    print("\n REGISTO DE UTENTE")

    nome = input("Digite o nome completo: ")
    data = input("Digite a data de nascimento: ")
    genero = input("Digite o genero (M/F): ")
    nif = input("Digite o NIF: ")
    telefone = input("Numero de telefone: ")

    numero = len(utentes) + 1
    codigo = "UT" + str(numero).zfill(5)

    # Guardar os dados do utente
    utente = {
        "codigo": codigo,
        "nome": nome,
        "data": data,
        "genero": genero,
        "nif": nif,
        "telefone": telefone,
        "consultas": []
    }

    utentes.append(utente)

    print("\nUtente registado com sucesso!")
    print("Numero de registo:", codigo)

# Funcao para procurar um utente
def procurar_utente():

    codigo = input("Digite o numero de registo: ")

    for utente in utentes:

        if utente["codigo"] == codigo:
            return utente

    return None

# consultar os dados do utente
def consultar_utente():

    print("\n--- CONSULTA DE UTENTE ---")

    utente = procurar_utente()

    if utente == None:

        print("Utente nao encontrado!")

    else:

        print("\nNumero:", utente["codigo"])
        print("Nome:", utente["nome"])
        print("Data de nascimento:", utente["data"])
        print("Genero:", utente["genero"])
        print("NIF:", utente["nif"])
        print("Telefone:", utente["telefone"])

        print("\n--- HISTORICO CLINICO ---")

        if len(utente["consultas"]) == 0:

            print("Nao existem consultas registadas.")

        else:

            for consulta in utente["consultas"]:

                print("Data:", consulta["data"])
                print("Diagnostico:", consulta["diagnostico"])
                print("Medico:", consulta["medico"])
                print("------------------------")

# registar uma consulta
def registar_consulta():

    print("\n--- REGISTAR CONSULTA ---")

    utente = procurar_utente()

    if utente == None:

        print("Utente nao encontrado!")

    else:

        data = input("Data da consulta: ")
        diagnostico = input("Diagnostico: ")
        medico = input("Nome do medico: ")

        consulta = {
            "data": data,
            "diagnostico": diagnostico,
            "medico": medico
        }

        utente["consultas"].append(consulta)

        print("Consulta registada com sucesso!")

# listar todos os utentes
def listar_utentes():

    print("\n--- LISTA DE UTENTES ---")

    if len(utentes) == 0:

        print("Nao existem utentes registados.")

    else:

        for utente in utentes:

            print(utente["codigo"], "-", utente["nome"])

# MENU PRINCIPAL

opcao = ""

while opcao != "0":

    print("\n===== SISTEMA DE REGISTO DE UTENTES =====")
    print("1 - Registar utente")
    print("2 - Consultar utente")
    print("3 - Registar consulta")
    print("4 - Listar utentes")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":

        registar_utente()

    elif opcao == "2":

        consultar_utente()

    elif opcao == "3":

        registar_consulta()

    elif opcao == "4":

        listar_utentes()

    elif opcao == "0":

        print("Programa encerrado!")

    else:

        print("Opcao invalida!")
