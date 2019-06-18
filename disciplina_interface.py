from tkinter import * #IMPORTANDO INTERFACE GRÁFICA

class Aplicacao(): #CLASSE QUE DEFINE A INTERFACE

    #CRIANDO A JANELA
    jan= Tk()
    jan.title("Cadastro de Disciplinas") #título da janela

    #VARIÁVEIS QUE ARMAZENAM AS INFORMAÇÕES PREENCHIDAS PELO USUÁRIO
    txtNome= StringVar() #GUARDA O QUE É DIGITADO
    txtCOD= StringVar()

    #Itens que estarão na janela
    lblnome= Label(jan, text="Nome") #LOCALIZAÇÃO DO NOME NA JANELA
    lblcod= Label(jan, text="CÓDIGO") #LOCALIZAÇÃO DO CPF NA JANELA
    entNome= Entry(jan, textvariable=txtNome, width=30) #CAMPO DE ENTRADA DO NOME
    entCOD= Entry(jan, textvariable=txtCOD, width=30) #CAMPO DE ENTRADA DO CPF
    listaDisciplina= Listbox(jan, width=100) #LISTA DE ITENS CADASTRADOS
    scrollDisciplina = Scrollbar(jan) #ROLAGEM DE TELA
    #BOTÕES QUE ESTARÃO NA JANELA
    btnViewAll= Button(jan, text="Ver todos")
    btnBuscar= Button(jan, text="CONSULTAR DISCIPLINA")
    btnInserir= Button(jan, text="CADASTRAR DISCIPLINA")
    btnUpdate= Button(jan, text="ATUALIZAR DISCIPLINA")
    btnDel= Button(jan, text="DELETAR DISCIPLINA")
    btnClose= Button(jan, text="Fechar")

    #POSIÇÃO DOS ELEMTOS NA JANELA
    lblnome.grid(row=0,column=0)
    lblcod.grid(row=1, column=0)
    entNome.grid(row=0, column=1, padx=50, pady=50) #CAIXA DE ENTRADA
    entCOD.grid(row=1, column=1) #CAIXA DE ENTRADA
    listaDisciplina.grid(row=0, column=2, rowspan=10)
    scrollDisciplina.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)


    #ASSOCIANDO BARRA DE ROLAGEM E LISTA DE ALUNO
    listaDisciplina.configure(yscrollcommand=scrollDisciplina.set) #ROLAMENTO VERTICAL
    scrollDisciplina.configure(command=listaDisciplina.yview) #DEFINE QUAL FUNÇÃO SERÁ CHAMADA QUANDO A SCROLLBAR FOR ATIVADA

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
