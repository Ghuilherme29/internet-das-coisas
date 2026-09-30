import customtkinter as ctk
ctk.set_appearance_mode('dark')

# janela ----------------------------

janela = ctk.CTk()
janela.geometry('500x500')
janela.title('Calculadora de Viagem')
try:
    janela.iconbitmap("aula9/bus_icon-icons.com_76529.ico")
except:
    pass   
# ------------------------------------------------------

#Função do cálculo ----------------
def calcular_gasto():
    try:
        distancia = float(Distancia_ViagemKM.get().replace(',', '.'))
        consumo = float (ConsumoVeiculo.get().replace(',' , '.'))
        preco = float(PrecoAtualCombustivel.get().replace(',' , '.'))
        
        if consumo > 0:
            litros = distancia / consumo
            custo_total = litros * preco
            
            resultado_label.configure(
                text =f"Gasto total: R$ {custo_total:.2f}\nCombustivel: {litros:.2f} Litros",
                text_color = "#00FF7F"
            )
        else:
            resultado_label.configure(text = "O consumo deve ser maior que zero!", text_color = "red")
            
    except ValueError:
        resultado_label.configure(text = "Preencha todos os campos com número válidos!", text_color = "red")
                
# Corpo da janela ------------

titulo = ctk.CTkLabel(janela,
                      text = "APP VIAGEM",
                      text_color = "#EBF2FA",
                      font = ctk.CTkFont (family ='Verdana',size = 35, weight = "bold"))
titulo.pack(pady = 40)
# -----------------------------------------------


Distancia_ViagemKM = ctk.CTkEntry(janela,
                     width = 400,
                     height = 40,
                     border_color = "#427AA1",
                     placeholder_text = "Digite a distância da viagem em KM")
Distancia_ViagemKM.pack(pady = 20)

#-----------------------------------------------------------------

ConsumoVeiculo = ctk.CTkEntry (janela,
                               width = 400,
                               height = 40,
                               border_color = "#427AA1",
                               placeholder_text = "Digite o consumo do seu veículo")
ConsumoVeiculo.pack(pady = 20)
# ---------------------------------------------------------------------

PrecoAtualCombustivel = ctk.CTkEntry (janela,
                                      width = 400,
                                      height = 40,
                                      border_color = "#427AA1",
                                      placeholder_text = "Digite o preço atual do combustivel")
PrecoAtualCombustivel.pack (pady = 20)
#---------------------------------------------------------------------------------------------------

butao = ctk.CTkButton (janela,
                       width = 200,
                       height = 40,
                       text = "Calcular gasto",
                       fg_color = ("#064789"),
                       text_color = "white",
                       font =  ('Verdana', 15),
                       command = calcular_gasto
                       )

butao.pack(pady = 35)
#----------------------------------------------

resultado_label = ctk.CTkLabel(janela,
                               text = '',
                               font = ('Verdena', 16, 'bold'))
resultado_label.pack(pady = 10)

janela.mainloop()

