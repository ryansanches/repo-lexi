import tkinter
from tkinter import *
from PIL import Image, ImageTk
import edge_tts
import asyncio


#def app_iniciado():
#criar uma função com o código, para que seja possivel carregar o código inteiro a partir do NOME da FUNÇÃO
#usando apenas "uma linha de código"

    #texto_iniciando['text'] = 'iniciando...'


def mostrar_texto():
    texto: str = nome.get()
    fala = ('Olá {}'.format(texto))
    erro = ('!ERRO!\nDigite apenas letras.')
    digite_algo = ('Digite seu nome para proseguir a próxima etapa.')

    #texto_enviado['text'] = fala                             #caixa de alerta
                                                              #if texto == "":
    if texto.strip() == "":                                   #   messagebox.showwarning("Campo vazio", "Digite seu nome para continuar.")
        texto_enviado['text'] = digite_algo                   #   return

    elif not all(parte.isalpha() for parte in texto.split()): #isalpha() não aceita alguns caracteres comuns, especialmente letras acentuadas dependendo do ambiente, e também porque pode haver quebras de linha/caracteres invisíveis
        texto_enviado['text'] = erro                          #replace() tira espaços internos, mas strip() remove espaços escondidos no começo/fim.
                                                              #o split() separa: / ["Ryan", "Sanches"] / Depois verifica se cada parte contém só letras.
    else:
        texto_enviado['text'] = fala


#Criar a tela do app
janela = Tk()
janela.title('LEXI')
janela.geometry('300x580')

#usado para colocar imagens na tela

#img = PhotoImage(file='novo_back.png')
#Label(janela, image=img).grid(row=0, column=0)


#mudar a cor da janela
janela.configure(bg='#C598CA')


#Inserir um texto na tela
texto_boasvindas = Label(janela, text= 'Seja bem-vindo(a)')
texto_boasvindas.grid(column= 15, row= 0, padx= 100, pady= 20)
texto_boasvindas.configure(background='#C44F10')


texto_digite = Label(janela, text= 'Qual é o seu nome?')
texto_digite.grid(column= 15, row= 4, padx= 100, pady= 0)
texto_digite.configure(background='#C598CA')
nome = tkinter.Entry(janela)
nome.grid(column= 15, row= 5, padx= 100, pady= 20)





#inserir um botão na tela
#botao = Button(janela, text ='Iniciar APP', command= app_iniciado)
#botao.grid(column= 15, row= 7, padx= 10, pady= 10)
#texto_iniciando = Label(janela, text='')
#texto_iniciando.grid(column= 15, row= 8, padx= 10, pady= 10)
#.configure(background='#C598CA')


botao_enviar = Button(janela, text = 'Enviar', command= mostrar_texto)
botao_enviar.grid(column= 15, row= 9, padx= 10, pady= 10)
botao_enviar.configure(background='#7F7F7F')
texto_enviado = Label(janela, text= '')
texto_enviado.grid(column= 15, row= 10, padx= 10, pady= 10)
texto_enviado.configure(background='#C598CA')




#manter a janela aberta
janela.mainloop()
