import datetime as dt
import sqlite3
import tkinter as tk
from tkinter import ttk
import uuid

lista_tipos = ["Galão", "Caixa", "Saco", "Unidade"]  #lista de apoio para o combobox (a posição facilita a manutenção).
lista_codigos = [] 


def inserir_codigo(): #Armazena os dados iseridos dentro de variáveis e cria um sequência de dicionários.
    global lista_codigos #Acesso da variavel fora da função.
    print("Antes da adição:", lista_codigos)
    
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quantidade = entry_quantidade.get()
    data_criacao = dt.datetime.now().strftime("%d/%m/%y %H:%M") #Define o formato de data e hora que serão acressentados ao banco de dados.
    id_produto = str(uuid.uuid4()) #criação de um ID aleatório para cada entrada.
    lista_codigos.append({"id_produto": id_produto, "descricao": descricao, "tipo": tipo, "quantidade": quantidade, "data_criacao": data_criacao})
    print(lista_codigos) #Essa saída de dados tem o intuito de controlar o fluxo de dados e entender possíveis erros na função.

    try: #O uso da estrutura "try" ajuda a previnir erros e a trata-los caso ocorram.
        conn = sqlite3.connect('produto.db') 
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS produto (id_produto TEXT, descricao TEXT, tipo TEXT, quantidade TEXT, data_criacao DATE)")
        #estabelecendo conexção com o banco de dados e/ou criando a a tabela no caso de ela não existir.

        for item in lista_codigos:
            cursor.execute("INSERT INTO produto VALUES (?, ?, ?, ?, ?)", (item["id_produto"], item["descricao"], item["tipo"], item["quantidade"], item["data_criacao"]))
            #Iteirando pelos valores da sequência de dicionários criada pela primeira função e incerindo cada valor dentro da tabela.

        conn.commit() #salvando cada alteração.

    except sqlite3.Error as e:
        print(f"Ocorreu um erro no banco de dados: {e}")
        #Conforme a utilização da estrutura "try" temos o tratamento de exceções, a variável "e" guardará o tipo de erro ocorrido.

    finally:
        conn.close() #Esse bloco acontece independente do erro, ele fecha a conexção com o banco de dados.
        lista_codigos = [] #Atribuindo o valor 0 a lista para poder receber novos valores.



def exibir_database(): #função que mostra ao usuário quais são os dados cadastrados na tabela.
    exibir_data = tk.Tk() #Criação da interface gráfica da tabela
    exibir_data.title('Tabela de Produtos') #título
        
    conn = sqlite3.connect('produto.db')
    cursor = conn.cursor()
    #Reestabelecendo a conexção com o banco de dados.

    cursor.execute("SELECT * FROM produto") #Retendo todos os dados dentro do banco de dados
    resultado = cursor.fetchall() #guardando todos os dados dentro da variável "resultado"

    #Definição da quantidade de colunas e posicionsmento dos valores
    tree = ttk.Treeview(exibir_data, columns=('ID', 'Produto', 'Unidade de Medida', 'Quantidade', 'Data'))
    tree.heading('#1', text='ID')
    tree.heading('#2', text='Produto')
    tree.heading('#3', text='Unidade de Medida')
    tree.heading('#4', text='Quantidade')
    tree.heading('#5', text='Data')

    tree.column('#0', anchor=tk.CENTER, width=80)
    tree.column('#1', anchor=tk.CENTER, width=120)
    tree.column('#2', anchor=tk.CENTER, width=120)
    tree.column('#3', anchor=tk.CENTER, width=100)
    tree.column('#4', anchor=tk.CENTER, width=120)

    for row in resultado:
        tree.insert('', 'end', values=row)

    tree.pack()
    #iterando os valores dentro da variavel "resultado" e introduzindo dentro dos espaços indicados.

    conn.close() #fechando a conexção com o banco de dados.


#Criação da interface gráfica biblioteca tkinter.
janela = tk.Tk()  #A variável "janela" guarda a função tkinter que cria a interface dentro do Python.
janela.title('Ferramenta de Cadastro de Materais')   #title é uma ferramenta dentro de tk que está sendo asociada ao objeto janela.

#incerção de campos para obter e descrever dados.
label_descricao = tk.Label(text="Nome do Produto") #campo descritivo.
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4) #posicionando o campo de descrição dentro da janela principal.

entry_descricao = tk.Entry()  #campo de entrada de dados
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_tipo_unidade = tk.Label(text="Classificação do Produto")
label_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_quantidade = tk.Label(text="Quantidade do Produto")
label_quantidade.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_quantidade = tk.Entry()
entry_quantidade.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

#Criação e posicionamento do botão "enviar" (associação da função "inserir_código")
botao_criar_codigo = tk.Button(text="Cadastrar produto", command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

#Criação e posicionamento do botão "Ver Tabela" (associação da função "exibir_database")
botao_verdata = tk.Button(text="Ver Tabela de Cadastros", command=exibir_database)
botao_verdata.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

janela.mainloop()  #fechamento da chamada de abertura das janelas de representação gráfica.