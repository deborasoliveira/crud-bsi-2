from tkinter import * #IMPORTANDO INTERFACE GRÁFICA

class Aplicacao(): #CLASSE QUE DEFINE A INTERFACE

    #CRIANDO A JANELA
    jan= Tk()
    jan.title("Sistema de Cadastro de Alunos") #título da janela

    #VARIÁVEIS QUE ARMAZENAM AS INFORMAÇÕES PREENCHIDAS PELO USUÁRIO
    txtNome= StringVar() #GUARDA O QUE É DIGITADO
    txtcpf= StringVar()

    #Itens que estarão na janela
    lblnome= Label(jan, text="Nome") #LOCALIZAÇÃO DO NOME NA JANELA
    lblcpf= Label(jan, text="CPF") #LOCALIZAÇÃO DO CPF NA JANELA
    entNome= Entry(jan, textvariable=txtNome, width=30) #CAMPO DE ENTRADA DO NOME
    entcpf= Entry(jan, textvariable=txtcpf, width=30) #CAMPO DE ENTRADA DO CPF
    listaAluno= Listbox(jan, width=100) #LISTA DE ITENS CADASTRADOS
    scrollAluno = Scrollbar(jan) #ROLAGEM DE TELA
    #BOTÕES QUE ESTARÃO NA JANELA
    btnViewAll= Button(jan, text="Ver todos")
    btnBuscar= Button(jan, text="CONSULTAR ALUNO")
    btnInserir= Button(jan, text="CADASTRAR ALUNO")
    btnUpdate= Button(jan, text="ATUALIZAR ALUNO")
    btnDel= Button(jan, text="DELETAR ALUNO")
    btnClose= Button(jan, text="Fechar")

    #POSIÇÃO DOS ELEMTOS NA JANELA
    lblnome.grid(row=0,column=0)
    lblcpf.grid(row=1, column=0)
    entNome.grid(row=0, column=1, padx=50, pady=50) #CAIXA DE ENTRADA
    entcpf.grid(row=1, column=1) #CAIXA DE ENTRADA
    listaAluno.grid(row=0, column=2, rowspan=10)
    scrollAluno.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)


    #ASSOCIANDO BARRA DE ROLAGEM E LISTA DE ALUNO
    listaAluno.configure(yscrollcommand=scrollAluno.set) #ROLAMENTO VERTICAL
    scrollAluno.configure(command=listaAluno.yview) #DEFINE QUAL FUNÇÃO SERÁ CHAMADA QUANDO A SCROLLBAR FOR ATIVADA

    #LARGURA E POSICIONAMENTO DOS WIDGETS
    for child in jan.winfo_children(): #PERCORRE A LISTA
        widget_class = child.__class__.__name__ #NOME DA CLASSE DO ELEMENTO
        if widget_class == "Button": #SE O WIDGET FOR DO TIPO BOTÃO
            child.grid_configure(sticky='WE', padx=5, pady=3) #DEFININDO ESPAÇOS E BORDAS
        elif widget_class == "Listbox": #SE O WIDGET FOR DO TIPO LISTBOX
            child.grid_configure(padx=5, pady=3, sticky='NS')
        elif widget_class == "Scrollbar": #SE O WIDGET FOR DO TIPO SCROLLBAR
            child.grid_configure(padx=5, pady=3, sticky='NS')
        else:
            child.grid_configure(padx=5, pady=3, sticky='N')


    def run(self): #JANELA QUE ESTAMOS UTILIZANDO
        Aplicacao.jan.mainloop() #CHAMANDO A CLASSE
        
