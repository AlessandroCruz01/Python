try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from tkinter import messagebox as mb
save = []
class TelaPrincipal():
    def __init__(self,root):
        self.root = root
        self.root['bg'] = 'grey'
        self.root.title('Tela Principal')
        self.root.geometry('400x150')

        #NÃO GOSTO MUITO DE USAR BOTÕES EM TELA PRICIPAL, MAS FIZ O MAXIMO PRA ESTETICA FICAR AGRADAVEL
        self.b1 = Button(self.root,width=50,text='CADASTRAR USUÁRIO',fg='green', command=self.cadPessoa)
        self.b1.pack()
        self.b2 = Button(self.root,width=40,text='REMOVER USUÁRIO',fg='blue', command=self.remover)
        self.b2.pack()
        self.b3 = Button(self.root,width=30,text='LIMPAR LISTA',fg='black', command=self.limpa)
        self.b3.pack()
        self.b4 = Button(self.root,width=10,text='SAIR',fg='red', command=self.root.destroy)
        self.b4.pack()

        self.Nid = 1

        #AQUI COMEÇAM AS FUNÇÕES
    def cadPessoa(self):
        self.cadf = Toplevel(self.root)
        self.cadf.title('Cadastro')
        self.cadf.grid()
        self.cadf.focus_force()  # serve para manter o foco nesta area
        self.cadf.grab_set()  #
        self.cadf.geometry('600x150')
        self.cadf.resizable(width=False, height=False)# nao deixa a tela ser expandida

        self.lin = Label(self.cadf, text='-' * 150)
        self.lin.place(x=0, y=5)
        self.tt1 = Label(self.cadf, text='CADASTRO')
        self.tt1["font"] = ("Calibri", "13", "bold")
        self.tt1.place(x=0, y=5)

        self.nome = Label(self.cadf, text='Nome: ')
        self.nome.place(x=10, y=50)

        self.n_nome = Entry(self.cadf, width=80)
        self.n_nome.focus_force()
        self.n_nome.place(x=70, y=50)

        self.b_save = Button(self.cadf, text='Salvar', command=self.save)
        self.b_save["font"] = ("Arial", "10", "bold")
        self.b_save.place(x=10, y=100)

        self.b_sair = Button(self.cadf, text='Sair', command=self.cadf.destroy)
        self.b_sair["font"] = ("Arial", "10", "bold")
        self.b_sair.place(x=80, y=100)

        self.cadf.mainloop()

    def save(self):
        global save
        try:
            if self.n_nome.get() != '':
                self.nomeMem= self.n_nome.get().lstrip().strip().capitalize()
                save.append({self.Nid: self.nomeMem})
                self.Nid += 1
                self.n_nome.delete(0, END)
            else:
                mb.showerror('Campo vazio','Campo nome nao pode ser vazio')

            print("OK")
            print(save)

        except:

            mb.showerror('ERROR! DESCULPE NÃO FOI POSSIVEL SALVAR!', sys.exc_info()[1:])
            print(sys.exc_info())

    def remover(self):
        self.rem = Toplevel(self.root)
        self.rem.title('Remover')
        self.rem.grid()
        self.rem.focus_force()  # serve para manter o foco nesta area
        self.rem.grab_set()  #
        self.rem.geometry('300x150')
        self.rem.resizable(width=False, height=False)  # nao deixa a tela ser expandida

        self.lin = Label(self.rem, text='-' * 150)
        self.lin.place(x=0, y=5)
        self.dados = Label(self.rem, text='ID')
        self.dados["font"] = ("Calibri", "13", "bold")
        self.dados.place(x=0, y=5)

        self.rid = Entry(self.rem, width=15)
        self.rid.focus_force()
        self.rid.place(x=100, y=35)

        self.bOk = Button(self.rem, text='OK', command=self.remove)
        self.bOk["font"] = ("Arial", "10", "bold")
        self.bOk.place(x=90, y=60)

        self.bSair = Button(self.rem, text='Sair', command=self.rem.destroy)
        self.bSair["font"] = ("Arial", "10", "bold")
        self.bSair.place(x=160, y=60)

        self.rem.mainloop()

    def remove(self):
        global save
        pos = 0
        dado = 0
        try:
            if self.rid.get() != '':
                self.remo = int(self.rid.get())
            else:
                mb.showerror('Campo vazio', 'Campo nome nao pode ser vazio')
        except ValueError:
            mb.showerror("Aviso", "Precisamos que digite o ID que consiste em um numero inteiro!\nA tela será fechada. Observe o ID que deseja remover e tente novamente!")
            print(sys.exc_info()[1:])
            self.rem.destroy()

        if save == []:
            mb.showinfo('Vazio', 'Não há cadastros no momento')
        else:
            for i in save:
                a = self.remo in i.keys()
                if a == True:
                    save.remove(i)
                    mb.askquestion("Remover", "O usuário {} será removido\nTem certeza que deseja remove-lo?".format(i))
                    break

        print(save)

    def limpa(self):
        mb.askokcancel("Remover", "tem certeza de que quer limpar sua lista?")
        save.clear()
        self.Nid = 1
        print(save)

a = Tk()
TelaPrincipal(a)
a.mainloop()