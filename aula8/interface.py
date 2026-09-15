import customtkinter as ctk
ctk.set_appearance_mode('dark')

#janela ---------------

janela = ctk.CTk()
janela.geometry('500x500')
janela.title('Sistema de Acesso - 2026')
janela.iconbitmap('aula8/code_lock_cryptocurrency_trader_bitcoin_security_key_digital_icon_251737.ico')
#-------------------------------------------------------------------------------------------------------

# Corpo da janela --------------------------

titulo = ctk.CTkLabel(janela,
                      text = "Sistema de login",
                      text_color = '#9BD1E5',
                      font = ('Dalton', 35))
titulo.pack()
#---------------------------------------------------


login = ctk.CTkEntry(janela,
                     width = 400,
                     height = 40,
                     border_color = "#114B5F",
                     placeholder_text = "Digite seu login")

login.pack(pady = 20)
#---------------------------------------------------------------

senha = ctk.CTkEntry(janela,
                     width = 400,
                     height = 40,
                     border_color = "#114B5F",
                     placeholder_text = "Digite sua senha",
                     show = ' ')

senha.pack()
#----------------------------------------------------------



botao = ctk.CTkButton(janela,
                     width = 400,
                     height = 40,
                     text = 'Acessar',
                     text_color = 'black',
                     fg_color = ("#114B5F"),
                     cursor = 'mouse',
                     )

botao.pack(pady = 35)

janela.mainloop()