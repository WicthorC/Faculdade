import tkinter as tk
from tkinter import ttk
import datetime
import sqlite3

#banco = sqlite3.connect('cadevents.db')

#cursor = banco.cursor()

#cursor.execute("CREATE TABLE user (nome text, idade text, doc text, email text, tel text)")
#cursor.execute("INSERT  INTO user VALUES ('Wictor', 40, '05811435746', 'wicthorgabryel15@gamil.com', '2195853947')")

#banco.commit()
#banco.close()


def cadastrar_usuario():
   
  banco = sqlite3.connect('cadastros.db')

  cursor = banco.cursor()

  cursor.execute(" INSERT INTO usuarios  VALUES (:nome, :idade, :doc, :email, :tel)",
                 {
                   'nome' :entry_nome.get(),
                   'idade' :entry_idade.get(),
                   'doc' :entry_doc.get(),
                   'email' :entry_email.get(),
                   'tel' :entry_tel.get(),
                   
                 }
                 )
  

  banco.commit()
  banco.close()

  entry_nome.delete(0, "end")
  entry_idade.delete(0, "end")
  entry_doc.delete(0, "end")
  entry_email.delete(0, "end")
  entry_tel.delete(0, "end")

pass

def cadastrar_eventos():
   
  banco = sqlite3.connect('cadastros.db')

  cursor = banco.cursor()

  cursor.execute(" INSERT INTO eventos VALUES (:nome_evento, :endereco, :categoria, :horario)",
                 {
                   'nome_evento' :entry_nome_evento.get(),
                   'endereco' :entry_endereco.get(),
                   'categoria' :combobox_categoria.get(),
                   'horario' :entry_horario.get(),
                 }
                 )
  

  banco.commit()
  banco.close()

  entry_nome_evento.delete(0, "end")
  entry_endereco.delete(0, "end")
  combobox_categoria.delete(0, "end")
  entry_horario.delete(0, "end")


pass

lista_categorias = ["Show", "evento esportivo", "Matine"]

janela = tk.Tk()

janela.title("Events.Rio")

#LABEL

label_usuarios = tk.Label(janela, text= 'Participar de um evento')
label_usuarios.grid(row=0, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

label_nome = tk.Label(janela, text= 'Nome')
label_nome.grid(row=1, column=0, padx=10, pady=10)

label_idade = tk.Label(janela, text= 'Idade')
label_idade.grid(row=2, column=0, padx=10, pady=10)

label_doc = tk.Label(janela, text= 'Documento')
label_doc.grid(row=3, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text= 'E-mail')
label_email.grid(row=4, column=0, padx=10, pady=10)

label_tel = tk.Label(janela, text= 'Telefone')
label_tel.grid(row=5, column=0, padx=10, pady=10)

label_eventos = tk.Label(janela, text= 'Cadastrar novo evento')
label_eventos.grid(row=7, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

label_nome_evento = tk.Label(janela, text= 'Nome do evento')
label_nome_evento.grid(row=8, column=0, padx=10, pady=10)

label_endereco = tk.Label(janela, text= 'Endereço')
label_endereco.grid(row=9, column=0, padx=10, pady=10)

label_categoria = tk.Label(janela, text= 'Categoria')
label_categoria.grid(row=10, column=0, padx=10, pady=10)

label_horario = tk.Label(janela, text= 'Horário')
label_horario.grid(row=11, column=0, padx=10, pady=10)


#ENTRYS

entry_nome = tk.Entry(janela, text= 'Nome', width= 30)
entry_nome.grid(row=1, column=1, padx=10, pady=10)

entry_idade = tk.Entry(janela, text= 'Idade', width= 30)
entry_idade.grid(row=2, column=1, padx=10, pady=10)

entry_doc = tk.Entry(janela, text= 'Documento', width= 30)
entry_doc.grid(row=3, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, text= 'E-mail', width= 30)
entry_email.grid(row=4, column=1, padx=10, pady=10)

entry_tel = tk.Entry(janela, text= 'Telefone', width= 30)
entry_tel.grid(row=5, column=1, padx=10, pady=10)

entry_nome_evento = tk.Entry(janela, text= 'Nome do evento', width= 30)
entry_nome_evento.grid(row=8, column=1, padx=10, pady=10)

entry_endereco = tk.Entry(janela, text= 'Endereço', width= 30)
entry_endereco.grid(row=9, column=1, padx=10, pady=10)

combobox_categoria = ttk.Combobox(values= lista_categorias, width= 30)
combobox_categoria.grid(row=10, column=1, padx=10, pady=10)

entry_horario = tk.Entry(janela, text= 'Horário', width= 30)
entry_horario.grid(row=11, column=1, padx=10, pady=10)

#BOTÕES

botao1_cadastrar = tk.Button(janela, text= 'Cadastrar usuario', command = cadastrar_usuario)
botao1_cadastrar.grid(row=6, column=0, padx=10, pady=10, columnspan=2, ipadx=80)


botao2_cadastrar = tk.Button(janela, text= 'Cadastrar evento', command = cadastrar_eventos)
botao2_cadastrar.grid(row=12, column=0, padx=10, pady=10, columnspan=2, ipadx=80)


janela.mainloop()