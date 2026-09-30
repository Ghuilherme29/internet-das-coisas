import customtkinter as ctk
ctk.set_appearance_mode('dark')

# janela ----------------------------

janela = ctk.CTk()
janela.geometry('600x450')
janela.title('Calculadora de notas')
try:
    janela.iconbitmap("aula9/bus_icon-icons.com_76529.ico")
except:
    pass   
# ------------------------------------------------------

#Função do cálculo ----------------
def calcular_nota():
    try:
        nota1 = float(Nota1.get().replace(',', '.'))
        nota2 = float (Nota2.get().replace(',' , '.'))
        nota3 = float(Nota3.get().replace(',' , '.'))
        
        media = (nota1 + nota2 + nota3) / 3
        if media >= 5:
            resultado = (f"Sua média é: {media}\nAprovado" )
            cor = "green"
            
        else:
            resultado = (f"Sua média é: {media}\nReprovado")
            cor = "red"  
            
            
            
            resultado_label.configure(
                text = resultado,
                text_color = cor
                
            )
            
    except ValueError:
        resultado_label.configure(text = "Preencha todos os campos com número válidos!", text_color = "red")
                
# Corpo da janela ------------

titulo = ctk.CTkLabel(janela,
                      text = "Sistema Escolar",
                      text_color = "#EBF2FA",
                      font = ctk.CTkFont (family ='Verdana',size = 35, weight = "bold"))
titulo.pack(pady = 40)
# -----------------------------------------------


Nota1= ctk.CTkEntry(janela,
                     width = 400,
                     height = 40,
                     border_color = "#427AA1",
                     placeholder_text = "Digite a 1º nota")
Nota1.pack(pady = 20)

#-----------------------------------------------------------------

Nota2= ctk.CTkEntry (janela,
                               width = 400,
                               height = 40,
                               border_color = "#427AA1",
                               placeholder_text = "Digite a 2º nota")
Nota2.pack(pady = 20)
# ---------------------------------------------------------------------

Nota3 = ctk.CTkEntry (janela,
                                      width = 400,
                                      height = 40,
                                      border_color = "#427AA1",
                                      placeholder_text = "Digite a 3º nota")
Nota3.pack (pady = 20)
#---------------------------------------------------------------------------------------------------

butao = ctk.CTkButton (janela,
                       width = 200,
                       height = 40,
                       text = "Calcular nota",
                       fg_color = ("#064789"),
                       text_color = "white",
                       font =  ('Verdana', 15),
                       command = lambda :calcular_nota()
                       )

butao.pack(pady = 35)
#----------------------------------------------

resultado_label = ctk.CTkLabel(janela,
                               text = '',
                               font = ('Verdena', 16, 'bold'))
resultado_label.pack(pady = 1)

janela.mainloop()

