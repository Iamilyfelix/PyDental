import os
resposta = ""

while resposta != "0":
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

            nomePaciente = input("👤 Nome: ")
            cpfPacientre = input("🪪 CPF: ")
            telefonePaciente = input("📞 Telefone: ")
            emailPaciente = input("📧 E-mail: ")
            
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
            print("""
              ┌────────────────────────────────────┐
              │          BUSCAR PACIENTE           │
             🔍───────────────────────────────────🔍
             🔍                                   🔍
             🔍     Informe o CPF do paciente     🔍
             🔍                                   🔍
              └─────────────────🔍─────────────────┘
            """)
            buscarPaciente = input("🪪 CPF: ")
            
            #função buscarcpf aqui
            
        elif respostaMod1 == "3":
            print("""
            ┌────────────────────────────────────┐
            │       ATUALIZAR PACIENTE           │
           ✏️───────────────────────────────────✏️
           ✏️      informe o CPF para           ✏️
           ✏️      localizar o paciente         ✏️
           ✏️                                   ✏️
            └─────────────────✏️─────────────────┘
           """)
            
            #função bucsar paciente fica aqui
            #if existir paciente passe os novos dados e chamar função atualizar paciente
            
            buscarPaciente = input("🪪 CPF: ")
            print("""
            ┌────────────────────────────────────┐
            │       Digite os novos dados        │
            │       do paciente                  │
           ✏️───────────────────────────────────✏️
                  
            """)
            
            nomeNovoPaciente = input("👤 Nome: ")
            cpfNovoPaciente = input("🪪 CPF: ")
            telefoneNovoPaciente = input("📞 Telefone: ")
            emailNovoPaciente = input("📧 E-mail: ")
            
            #função atualizar paciente fica aqui 
            
            print("""
             ┌────────────────────────────────────┐
             │           NOTIFICAÇÃO              │
            🔔───────────────────────────────────🔔
            🔔     Dados editados com            🔔
            🔔     sucesso!                      🔔
            🔔                                   🔔
             └────────────────🔔──────────────────┘
            """)
        
        elif respostaMod1 == "4":
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

            cpf_excluir = input("🪪 CPF: ")
            
            #função buscar cpf fica aqui
            #if existir paciente função excluir é chamada
            
            #função excluir paciente fica aqui 
            
            print("""
             ┌────────────────────────────────────┐
             │           NOTIFICAÇÃO              │
            🔔───────────────────────────────────🔔
            🔔     Paciente excluído             🔔
            🔔     com sucesso!                  🔔
            🔔                                   🔔
             └────────────────🔔──────────────────┘
            """)
            
            
    elif resposta == "2":
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
            nomeDentista = input("👤 Nome: ")
            cpfDentista = input("🪪 CPF: ")
            cro = input("👨‍⚕️ CRO: ")
            telefoneDentista = input("📞 Telefone: ")
            emailDentista = input("📧 E-mail: ")
                
            #função cadastrarDentista aqui 
                
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
            print("""
              ┌────────────────────────────────────┐
              │          BUSCAR DENTISTA           │
             🔍───────────────────────────────────🔍
             🔍                                   🔍
             🔍     Informe o CPF do dentista     🔍
             🔍                                   🔍
              └─────────────────🔍─────────────────┘
            """)
            buscarDentista = input("🪪 CPF: ")
            
            #função buscarcpf aqui
                
    elif resposta == "3":
        os.system("cls")
        print("""
        
         ┌────────────────────────────────────┐
         │            Consultas               │      
        📅───────────────────────────────────📅
        📅                                   📅
        📅     [1] Cadastrar                 📅
        📅     [2] Buscar                    📅
        📅     [3] Atualizar                 📅
        📅     [4] Excluir                   📅
        📅                                   📅
        📅     [0] Voltar                    📅
        📅                                   📅
         └─────────────────📅─────────────────┘
        """)
    elif resposta == "4":
        os.system("cls")
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