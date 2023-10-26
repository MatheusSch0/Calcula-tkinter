import tkinter as tk

#função e calculo
def cadastro():
    name = entry_name.get()
    email = entry_email.get()
    senha = entry_senha.get()





root = tk.Tk()  #janela
root.title('CADASTRO')    #titulo


label_name = tk.Label(root, text="NOME")
entry_name = tk.Entry(root)   #INPUT



label_email = tk.Label(root, text="EMAIL")
entry_email = tk.Entry(root)


label_senha = tk.Label(root, text="SENHA")
entry_senha = tk.Entry(root)

#botão


btn = tk.Button(root, text='Clique aqui' , command=cadastro)
btn.pack()


label_name.pack()
entry_name.pack()


label_email.pack()
entry_email.pack()


label_senha.pack()
entry_senha.pack()


root.mainloop()