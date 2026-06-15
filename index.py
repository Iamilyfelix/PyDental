import os
resposta = ""
pacientes = {
    '123.456.789-10' : ["Homer Simpson", "99999-9999", "homer@springfield.com"],
    '234.456.456-71' : ["Marge Simpson", "88888-8888", "marge@springfield.com"]
}
dentistas = {
    '11111111111': ['Edna Krabappel', '(84) 99988-8777', 'krabappel@springfield.com'], 
    '22222222222': ['Elizabeth Hoover', '(83) 99900-0111', 'hoover@springfield.com']
}
consultas = {}
resposta = ""
while resposta != "0":
    os.system("cls")
    print("""
          
     ┌────────────────────────────────────┐
     │             PyDental               │      
    🦷───────────────────────────────────🦷
    🦷                                   🦷
    🦷     [1] Pacientes                 🦷
    🦷     [2] Dentistas                 🦷                         
    🦷     [3] Consultas                 🦷 
    🦷     [4] Relatórios                🦷 
    🦷     [5] Informações               🦷 
    🦷                                   🦷
    🦷     [0] Sair                      🦷 
    🦷                                   🦷 
     └─────────────────🦷─────────────────┘                                  
    """)

    resposta = input("👉 Escolha uma opção: ")

    if resposta == "1":
        respostaMod1 = ""
        while respostaMod1 != "0":
            
            os.system("cls")
            print("""
            
                ┌────────────────────────────────────┐
                │            Pacientes               │     
                👥───────────────────────────────────👥
                👥                                   👥
                👥     [1] Cadastrar                 👥
                👥     [2] Buscar                    👥
                👥     [3] Atualizar                 👥
                👥     [4] Excluir                   👥
                👥                                   👥
                👥     [0] Voltar                    👥
                👥                                   👥
                └─────────────────👥─────────────────┘
            
            """)
            
            respostaMod1 = input("👉 Escolha uma opção: ")
            
            if respostaMod1 == "1":
                os.system("cls")
                print("""
                ┌────────────────────────────────────┐
                │        CADASTRAR PACIENTE          │
                👥───────────────────────────────────👥
                👥                                   👥
                👥      Informe os dados para        👥
                👥      realizar o cadastro.         👥
                👥                                   👥
                └────────────────👥──────────────────┘
                """)

                cpfPaciente = input("🪪 CPF: ")
                nomePaciente = input("👤 Nome: ")
                telefonePaciente = input("📞 Telefone: ")
                emailPaciente = input("📧 E-mail: ")
                
                pacientes[cpfPaciente] = [nomePaciente, telefonePaciente, emailPaciente,]
                print("Pacientes:", pacientes)  
                
                #função cadastrarPaciente aqui
                
                print("""
                ┌────────────────────────────────────┐
                │           NOTIFICAÇÃO              │
                🔔───────────────────────────────────🔔
                🔔     Paciente cadastrado           🔔
                🔔     com sucesso!                  🔔
                🔔                                   🔔
                └────────────────🔔──────────────────┘
                """)
            elif respostaMod1 == "2":
                os.system("cls")
                print("""
                 ┌────────────────────────────────────┐
                 │          BUSCAR PACIENTE           │
                🔍───────────────────────────────────🔍
                🔍                                   🔍
                🔍     Informe o CPF do paciente     🔍
                🔍                                   🔍
                 └─────────────────🔍─────────────────┘
                """)
                cpfBusca = input("🪪 CPF: ")
                print()
                
                if cpfBusca in pacientes:
                    print("👤 Nome: ", pacientes[cpfBusca][0])
                    print("📞 Telefone: ", pacientes[cpfBusca][1])
                    print("📧 E-mail: ", pacientes[cpfBusca][2])
                    print()
                    input("Tecle <ENTER> para continuar...")
                
                else:
                    print("""
                     ┌────────────────────────────────────┐
                     │           NOTIFICAÇÃO              │
                    🔔───────────────────────────────────🔔
                    🔔                                   🔔
                    🔔      Paciente não encontrado      🔔
                    🔔                                   🔔
                     └────────────────🔔──────────────────┘
                    """)
                    
                
            elif respostaMod1 == "3":
                os.system("cls")
                print("""
                 ┌────────────────────────────────────┐
                 │       ATUALIZAR PACIENTE           │
                ✏️───────────────────────────────────✏️
                ✏️      informe o CPF para           ✏️
                ✏️      localizar o paciente         ✏️
                ✏️                                   ✏️
                 └─────────────────✏️─────────────────┘
            """)
                cpfBusca = input("🪪 CPF: ")
                print()
                
                if cpfBusca in pacientes:
                    print("DADOS ATUAIS DO PACIENTE")
                    print("👤 Nome: ", pacientes[cpfBusca][0])
                    print("📞 Telefone: ", pacientes[cpfBusca][1])
                    print("📧 E-mail: ", pacientes[cpfBusca][2])
                    print()
                
                    print("""
                    ┌────────────────────────────────────┐
                    │       Digite os novos dados        │
                    │       do paciente                  │
                    ✏️───────────────────────────────────✏️
                        
                    """)
                    
                    nomeNovo = input("👤 Nome: ")
                    telefoneNovo = input("📞 Telefone: ")
                    emailNovo = input("📧 E-mail: ")
                    
                    pacientes[cpfBusca] = [nomeNovo, telefoneNovo, emailNovo]
                    
                    print("""
                    ┌────────────────────────────────────┐
                    │           NOTIFICAÇÃO              │
                    🔔───────────────────────────────────🔔
                    🔔     Dados editados com            🔔
                    🔔     sucesso!                      🔔
                    🔔                                   🔔
                    └────────────────🔔──────────────────┘
                    """)
                    
                    print(pacientes)
                    
                else:
                    print("""
                     ┌────────────────────────────────────┐
                     │           NOTIFICAÇÃO              │
                    🔔───────────────────────────────────🔔
                    🔔                                   🔔
                    🔔      Paciente não encontrado      🔔
                    🔔                                   🔔
                     └────────────────🔔──────────────────┘
                    """) 
                          
                input("Tecle <ENTER> para continuar...") 
            elif respostaMod1 == "4":
                os.system("cls")
                print("""
                 ┌────────────────────────────────────┐
                 │         EXCLUIR PACIENTE           │
                🗑️───────────────────────────────────🗑️
                🗑️                                   🗑️
                🗑️     Informe o CPF do paciente     🗑️
                🗑️     que deseja excluir.           🗑️
                🗑️                                   🗑️
                 └─────────────────🗑️─────────────────┘
                """)

                cpfExcluir = input("🪪 CPF: ")
                
                if cpfExcluir in pacientes:
                    print("👤 Nome: ", pacientes[cpfExcluir][0])
                    print("📞 Telefone: ", pacientes[cpfExcluir][1])
                    print("📧 E-mail: ", pacientes[cpfExcluir][2])
                    print()
                    confirma = input("Tecle 's' para confirmar exclusão...")
                    if confirma.lower() == 's':
                        del pacientes[cpfExcluir]
                        print("""
                         ┌────────────────────────────────────┐
                         │           NOTIFICAÇÃO              │
                        🔔───────────────────────────────────🔔
                        🔔     Paciente excluído             🔔
                        🔔     com sucesso!                  🔔
                        🔔                                   🔔
                         └────────────────🔔──────────────────┘
                        """)
                        print()
                        print("pacientes: ", pacientes)    #conferir exclusão
                    else:
                        print("""
                         ┌────────────────────────────────────┐
                         │           NOTIFICAÇÃO              │
                        🔔───────────────────────────────────🔔
                        🔔                                   🔔
                        🔔      Paciente não encontrado      🔔
                        🔔                                   🔔
                         └────────────────🔔──────────────────┘
                        """)
                    
                        
            
            
    elif resposta == "2":
        respostaMod2 = ""
        while respostaMod2 != "0":            
            os.system("cls")
            print("""
            
             ┌────────────────────────────────────┐
             │            Dentistas               │      
            👨‍⚕️───────────────────────────────────👨‍⚕️
            👨‍⚕️                                   👨‍⚕️
            👨‍⚕️     [1] Cadastrar                 👨‍⚕️
            👨‍⚕️     [2] Buscar                    👨‍⚕️
            👨‍⚕️     [3] Atualizar                 👨‍⚕️
            👨‍⚕️     [4] Excluir                   👨‍⚕️
            👨‍⚕️                                   👨‍⚕️
            👨‍⚕️     [0] Voltar                    👨‍⚕️
            👨‍⚕️                                   👨‍⚕️
             └─────────────────👨‍⚕️─────────────────┘
            """)
            
            respostaMod2 = input("👉 Escolha uma opção: ")
            
            if respostaMod2 == "1":
                os.system("cls")
                print("""
                 ┌────────────────────────────────────┐
                 │        CADASTRAR DENTISTA          │
                👨‍⚕️───────────────────────────────────👨‍⚕️
                👨‍⚕️                                   👨‍⚕️
                👨‍⚕️      Informe os dados para        👨‍⚕️
                👨‍⚕️      realizar o cadastro.         👨‍⚕️
                👨‍⚕️                                   👨‍⚕️
                 └────────────────👨‍⚕️──────────────────┘
                """)
                cro = input("👨‍⚕️ CRO: ")
                nomeDentista = input("👤 Nome: ")
                telefoneDentista = input("📞 Telefone: ")
                emailDentista = input("📧 E-mail: ")
                
                #função cadastrarDentista aqui 
                
                dentistas[cro] = [nomeDentista, telefoneDentista, emailDentista]
                print("Dentistas:", dentistas)  
                    
                print("""
                 ┌────────────────────────────────────┐
                 │           NOTIFICAÇÃO              │
                🔔───────────────────────────────────🔔
                🔔     Dentista cadastrado           🔔
                🔔     com sucesso!                  🔔
                🔔                                   🔔
                 └────────────────🔔──────────────────┘
                """)
                
            elif respostaMod2 == "2":
                os.system("cls")
                print("""
                ┌────────────────────────────────────┐
                │          BUSCAR DENTISTA           │
                🔍───────────────────────────────────🔍
                🔍                                   🔍
                🔍     Informe o CRO do dentista     🔍
                🔍                                   🔍
                └─────────────────🔍─────────────────┘
                """)
                buscarDentista = input("🪪 CRO: ")
                
                #função buscarCro aqui
                
            elif respostaMod2 == "3":
                os.system("cls")
                print("""
                ┌────────────────────────────────────┐
                │       ATUALIZAR DENTISTA           │
                ✏️───────────────────────────────────✏️
                ✏️      informe o CPF para           ✏️
                ✏️      localizar o dentista         ✏️
                ✏️                                   ✏️
                └─────────────────✏️─────────────────┘
            """)
                
                buscarDentista = input("🪪 CPF: ")
                
                #função bucsar dentista fica aqui
                #if existir dentista passe os novos dados e chamar função atualizar paciente
                
                print("""
                ┌────────────────────────────────────┐
                │       Digite os novos dados        │
                │       do paciente                  │
               ✏️───────────────────────────────────✏️
                    
                """)
                
                nomeNovo = input("👤 Nome: ")
                croNovo = input("🪪 CRO:")
                telefoneNovo = input("📞 Telefone: ")
                emailNovo = input("📧 E-mail: ")
                
                #função atualizar fica aqui 
                
                print("""
                ┌────────────────────────────────────┐
                │           NOTIFICAÇÃO              │
                🔔───────────────────────────────────🔔
                🔔     Dados atualizados com         🔔
                🔔     sucesso!                      🔔
                🔔                                   🔔
                └────────────────🔔──────────────────┘
                """)
            
            elif respostaMod2 == "4":
                os.system("cls")
                print("""
                ┌────────────────────────────────────┐
                │         EXCLUIR DENTISTA           │
                🗑️───────────────────────────────────🗑️
                🗑️                                   🗑️
                🗑️     Informe o CPF do dentista     🗑️
                🗑️     que deseja excluir.           🗑️
                🗑️                                   🗑️
                └─────────────────🗑️─────────────────┘
                """)

                cpf_excluir = input("🪪 CPF: ")
                
                #função buscar cpf fica aqui
                #if existir paciente função excluir é chamada
                
                #função excluir paciente fica aqui 
                
                print("""
                ┌────────────────────────────────────┐
                │           NOTIFICAÇÃO              │
                🔔───────────────────────────────────🔔
                🔔     Dentista excluído             🔔
                🔔     com sucesso!                  🔔
                🔔                                   🔔
                └────────────────🔔──────────────────┘
                """)
            
                
    elif resposta == "3":
        respostaMod3 = ""
        while respostaMod3 != "0":          
            os.system("cls")
            print("""
            
            ┌────────────────────────────────────┐
            │            Consultas               │      
            📅───────────────────────────────────📅
            📅                                   📅
            📅     [1] Cadastrar                 📅
            📅     [2] Buscar                    📅
            📅     [3] Atualizar                 📅 
            📅     [4] Mudar status              📅
            📅     [5] Excluir                   📅
            📅                                   📅
            📅     [0] Voltar                    📅
            📅                                   📅
            └─────────────────📅─────────────────┘
            """)
            respostaMod3 = input("👉 Escolha uma opção: ")
            
            if respostaMod3 == "1":
                os.system("cls")
                print("""
                ┌────────────────────────────────────┐
                │        CADASTRAR CONSULTA          │
               📅───────────────────────────────────📅
               📅                                   📅
               📅      Informe os dados para        📅
               📅      realizar o cadastro.         📅
               📅                                   📅
                └────────────────📅──────────────────┘
                """)
                
                cpfPaciente = input("🪪👤 CPF Paciente: ")
                croDentista = input("🪪👨‍⚕️ CRO Dentista: ")
                data = input("Data (dd/mm/aaaa): ")
                hora = input("Hora (hh:mm): ")
                status = input("Status (Realizada ou Não realizada): ")
                
                consultas[cpfPaciente] = [croDentista, data, hora, status]
                print("consultas:", consultas) 
                
                print("""
                 ┌────────────────────────────────────┐
                 │           NOTIFICAÇÃO              │
                🔔───────────────────────────────────🔔
                🔔     Consulta cadastrada           🔔
                🔔     com sucesso!                  🔔
                🔔                                   🔔
                 └────────────────🔔──────────────────┘
                """)
                
            if respostaMod3 == "2":
                os.system("cls")
                print("""
                 ┌────────────────────────────────────┐
                 │          BUSCAR CONSULTA           │
                🔍───────────────────────────────────🔍
                🔍                                   🔍
                🔍     Informe o CPF do Paciente     🔍
                🔍                                   🔍
                 └─────────────────🔍─────────────────┘
                """)
                buscarConculta = input("🪪 CPF: ")
                
                #função buscarcpf aqui e mostrar consultas cadastradas nesse cpf 
            if respostaMod3 == "3":
                os.system("cls")
                print("""
                ┌────────────────────────────────────┐
                │       ATUALIZAR CONSULTAS          │
               ✏️───────────────────────────────────✏️
               ✏️     informe o CPF do paciente     ✏️
               ✏️     para localizar a consulta     ✏️
               ✏️                                   ✏️
                └─────────────────✏️─────────────────┘
            """)
                
                buscarCpf = input("🪪 CPF: ")
                
                #função bucsar dentista fica aqui
                #if existir dentista passe os novos dados e chamar função atualizar paciente
                
                print("""
                ┌────────────────────────────────────┐
                │       Digite os novos dados        │
                │       da consulta                  │
               ✏️───────────────────────────────────✏️
                    
                """)
                
                cpfPacienteNovo = input("🪪👤 CPF Paciente: ")
                croDentistaNovo = input("🪪👨‍⚕️ CRO Dentista: ")
                dataNova = input("Data (dd/mm/aaaa): ")
                horaNova = input("Hora (hh:mm): ")
                statusNovo = input("Status (Realizada ou Não realizada): ")
                
                #função atualizar fica aqui 
                
                print("""
                 ┌────────────────────────────────────┐
                 │           NOTIFICAÇÃO              │
                🔔───────────────────────────────────🔔
                🔔     Dados atualizados com         🔔
                🔔     sucesso!                      🔔
                🔔                                   🔔
                 └────────────────🔔──────────────────┘
                """)
                
                #FUNÇÃO MUDAR STATUS VAI FICAR AQUI (TENHO QUE PENSAR COMO VAI SER AINDA)
                
                #FUNÇÃO EXCLUIR VAI FICAR AQUI MAS NÃO SEI QUAL MELHOR FORMA DE FAZER ISSO
            
    elif resposta == "4":
        respostaMod4 = ""
        while respostaMod4 != "0":
            
            #os.system("cls")
            print("""
            
             ┌────────────────────────────────────┐
             │           Relatórios               │      
            📊───────────────────────────────────📊
            📊                                   📊
            📊     [1] Listar Pacientes          📊
            📊     [2] Listar Dentistas          📊
            📊     [3] Listar Consultas          📊
            📊                                   📊
            📊     [0] Voltar                    📊
            📊                                   📊
             └─────────────────📊─────────────────┘
            """)
            respostaMod4 = input("")
            if respostaMod4 == "1":
                os.system("cls")
                print("""
                    ####### LISTA COM TODOS OS PACIENTES + SEUS DADOS ######
                    """)
                print(pacientes)
            elif respostaMod4 == "2":
                os.system("cls")
                print("""
                    ####### LISTA COM TODOS OS DENTISTAS + SEUS DADOS ######
                    """)
                print(dentistas)
            elif respostaMod4 == "3":
                os.system("cls")
                print("""
                    ####### LISTA COM TODOS AS CONSULTAS + SEUS DADOS ######
                    """)
                print(consultas)
    elif resposta == "5":
        os.system("cls")
        print("""
        
         ┌────────────────────────────────────┐
         │          Informações               │
        ℹ️───────────────────────────────────ℹ️
        ℹ️                                   ℹ️
        ℹ️  Projeto: PyDental                ℹ️
        ℹ️  Sistema de Gestão para           ℹ️
        ℹ️  Clínicas Dentárias               ℹ️
        ℹ️                                   ℹ️
        ℹ️  Desenvolvedora:                  ℹ️
        ℹ️  Iamily Felix                     ℹ️
        ℹ️                                   ℹ️
        ℹ️  Versão: 1.0                      ℹ️
        ℹ️                                   ℹ️
        ℹ️  [0] Voltar                       ℹ️
        ℹ️                                   ℹ️
         └─────────────────ℹ️─────────────────┘
        """)
        
    elif resposta == "":
        os.system("cls")
        print("""
        
         ┌────────────────────────────────────┐
         │               Saindo               │
        🚪───────────────────────────────────🚪
        🚪                                   🚪
        🚪  Programa encerrado com sucesso!  🚪
        🚪          Até logo!                🚪
        🚪                                   🚪
         └─────────────────🚪─────────────────┘
        """)
    else:
        os.system("cls")
        print("""
              
         ┌────────────────────────────────────┐
         │               Erro                 │
        ❌───────────────────────────────────❌
        ❌                                   ❌
        ❌     Digite uma opção válida!      ❌
        ❌                                   ❌
         └─────────────────❌─────────────────┘
        """)