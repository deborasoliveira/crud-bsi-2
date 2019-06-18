from tkinter import * #IMPORTANDO INTERFACE GRÁFICA

class Aplicacao(): #CLASSE QUE DEFINE A INTERFACE

    #CRIANDO A JANELA
    jan= Tk()
    jan.title("Sistema de Cadastro de Turmas") #TÍTULO DA JANELA

    #VARIÁVEIS QUE ARMAZENAM AS INFORMAÇÕES PREENCHIDAS PELO USUÁRIO
    txtCODT= StringVar() #GUARDA O QUE É DIGITADO
    txtCODD= StringVar()
    txtP= StringVar()
    txtCPFP= StringVar()
    txtCPFA= StringVar()

    #Itens que estarão na janela
    lblCODT= Label(jan, text="CÓDIGO DA TURMA") #LOCALIZAÇÃO DO NOME NA JANELA
    lblCODD= Label(jan, text="CÓDIGO DA DISCIPLINA") #LOCALIZAÇÃO DO CPF NA JANELA
    lblP= Label(jan, text="PERÍODO")
    lblPROF= Label(jan, text="CPF DO PROFESSOR")
    lblALUNO= Label(jan, text="CPF DO ALUNO")
    entcodt= Entry(jan, textvariable=txtCODT, width=30) #CAMPO DE ENTRADA DO NOME
    entcodd= Entry(jan, textvariable=txtCODD, width=30) #CAMPO DE ENTRADA DO CPF
    entp= Entry(jan, textvariable=txtP, width=30)
    entcpfp= Entry(jan, textvariable=txtCPFP, width=30)
    entcpfa= Entry(jan, textvariable=txtCPFA, width=30)
    listaTurma= Listbox(jan, width=100) #LISTA DE ITENS CADASTRADOS
    scrollTurma = Scrollbar(jan) #ROLAGEM DE TELA
    #BOTÕES QUE ESTARÃO NA JANELA
    btnViewAll= Button(jan, text="Ver todos")
    btnBuscar= Button(jan, text="CONSULTAR TURMA")
    btnInserir= Button(jan, text="CADASTRAR TURMA")
    btnUpdate= Button(jan, text="ATUALIZAR TURMA")
    btnDel= Button(jan, text="DELETAR TURMA")
    btnClose= Button(jan, text="Fechar")

    #POSIÇÃO DOS ELEMTOS NA JANELA
    lblCODT.grid(row=0,column=0)
    lblCODD.grid(row=1, column=0)
    lblP.grid(row=2, column=0)
    lblPROF.grid(row=3, column=0)
    lblALUNO.grid(row=4, column=0)
    entcodt.grid(row=0, column=1, padx=50, pady=60) #CAIXA DE ENTRADA
    entcodd.grid(row=1, column=1)
    entp.grid(row=2, column=1) #CAIXA DE ENTRADA
    entcpfp.grid(row=3, column=1)
    entcpfa.grid(row=4, column=1)
    listaTurma.grid(row=0, column=2, rowspan=10)
    scrollTurma.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=5, column=0, columnspan=2)
    btnBuscar.grid(row=6, column=0, columnspan=2)
    btnInserir.grid(row=7, column=0, columnspan=2)
    btnUpdate.grid(row=8, column=0, columnspan=2)
    btnDel.grid(row=9, column=0, columnspan=2)
    btnClose.grid(row=10, column=0, columnspan=2)


    #ASSOCIANDO BARRA DE ROLAGEM E LISTA DE ALUNO
    listaTurma.configure(yscrollcommand=scrollTurma.set) #ROLAMENTO VERTICAL
    scrollTurma.configure(command=listaTurma.yview) #DEFINE QUAL FUNÇÃO SERÁ CHAMADA QUANDO A SCROLLBAR FOR ATIVADA

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
        
