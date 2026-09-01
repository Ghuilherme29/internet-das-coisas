import os
os.system("cls")
tarefas=[] 

while True:
    print("\n=======Menu===========") 
    print("1- Adicionar tarefa")  
    print("2- Remover tarefa")
    print("3-Mostrar tarefas") 
    print("0-sair") 
    
    opcao=input("Escolha uma opçao:") 
    
    if opcao=="1":
        tarefa=input("Digite a tarefa") 
        tarefas.append(tarefa) 
        print("tarefa adicionada com sucesso") 
         
    elif opcao =="2":
        
        tarefa=input("Digite a tarefa ue quer remover") 
        if tarefa in tarefas:
            tarefas.remove(tarefa) 
            print("Tarefa removida com sucesso") 
        else: 
            print("Tarefa nao encontrada") 
            
    elif opcao =="3":
        if len (tarefas) ==0:
            print("Nao ha tarefas cadastrada") 
        else:
            print("\n === Tarefas=====") 
            
        for tarefa in tarefas: 
            print(tarefa) 
            
    elif opcao =="0":
        print("programa encerrado") 
        break 
    else:
        print("opçao invalida")