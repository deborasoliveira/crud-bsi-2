from aluno_intrfc import *
import aluno_bancod as comando

app = None

def ver(): #CONSULTA DE TODOS OS USUÁRIOS
    rows = comando.listar()
    app.listaAluno.delete(0, END)
    for r in rows:
        app.listaAluno.insert(END, r)

def procurar(): #BUSCA DE USUÁRIO ESPECÍFICO
    app.listaAluno.delete(0, END)
    rows = comando.buscar(app.txtNome.get(), app.txtcpf.get()) #UTILIZAÇÃO DA FUNÇÃO DE "BUSCAR" DO BANCO E UTILIZANDO AS INFORMAÇÕES DAS VARIÁVEIS
    for r in rows:
        app.listaAluno.insert(END, r)

def inserir():
    comando.cadastrar(app.txtNome.get(), app.txtcpf.get()) #CADASTRANDO
    ver() #CONFERIR O CADASTRO

def update():
    comando.atualizacao(selected[0],app.txtNome.get(), app.txtcpf.get()) #ALTERANDO O CADASTRO
    ver() #CONSULTAR A ATUALIZAÇÃO

def exclusao(): #EXCLUSÃO DE CADASTRO
    id = selected[0]
    comando.deletar(id)
    ver() #CONFERIR A EXCLUSÃO


def getSelectedRow(event): #PREENCHER OS CAMPOS DE ENTRADA COM AS INFORMAÇÕES DAS PESSOAS JA CADASTRADAS
    global selected
    index = app.listaAluno.curselection()[0] #RECUPERAR O INDEX DOS ITENS SELECIONADOS, PRIMEIRA POSIÇÃO RETORNADA POR CURSERELATION
    selected = app.listaAluno.get(index) #ARMAZENAMENTO NA VARIÁVEL GLOBAL
    app.entNome.delete(0, END) #DELETAR E PREENCHER NOVAMENTE OS CAMPOS DE ENTRADA
    app.entNome.insert(END, selected[1])
    app.entcpf.delete(0, END)
    app.entcpf.insert(END, selected[2])

    return selected

#RELACIONANDO OS COMANDOS À INTERFACE
if __name__ == "__main__":
    app = Aplicacao()
    app.listaAluno.bind('<<ListboxSelect>>', getSelectedRow) #ASSOCIANDO A FUNÇÃO GETSELECTED AO LISTBOX, SEMPRE QUE O ITEM FOR SELECIONADO, ESSA FUNÇÃO SERÁ ATIVADA.
    #UTILIZANDO AS VARIÁVEIS PARA ACESSAR OS ELEMENTOS DA JANELA
    app.btnViewAll.configure(command=ver)
    app.btnBuscar.configure(command=procurar)
    app.btnInserir.configure(command=inserir)
    app.btnUpdate.configure(command=update)
    app.btnDel.configure(command=exclusao)
    app.btnClose.configure(command=app.jan.destroy)
    app.run() #RODAR A INTERFACE
