import customtkinter as ctk
ctk.set_appearance_mode("dark")



def calcular():
    quantidade_diarias_value = float(quantidade_diarias.get())
    valor_diarias_value = float(valor_diarias.get())
    
    
    valor_hospedagem = quantidade_diarias_value * float(valor_diarias_value)
        
        
    if quantidade_diarias_value >= 5.0:
            desconto = quantidade_diarias_value * 0.10
            total_a_pagar = valor_hospedagem - desconto
            resultado.configure(text=f" Hospedagem:{valor_hospedagem:.2f} R$ \n Desconto: {desconto:.2f} R$ \n Total a pagar: {total_a_pagar:.2f} R$")
            
    else:
        resultado.configure(text=f" Hospedagem:{valor_hospedagem:.2f} R$")
        
        
    texto_resultado = (
            f"  Hospedagem:               R$ {valor_hospedagem:.2f}\n"
            f"  Desconto:                  R$ {desconto:.2f}\n"
            f"___________________________________\n\n"
            f"  Total a Pagar:             R$ {total_a_pagar:.2f}"
        )
        
    resultado.configure(text=texto_resultado, text_color="#22c55e")
        
            
        
            









janela = ctk.CTk(fg_color="#131924")
janela.geometry("700x600")
janela.resizable(False, False)
janela.title("Reserva de hotel")
janela.iconbitmap("circle_icon_191833.ico")







hospede = ctk.CTkEntry(janela,
                    width=400,
                    height=50,
                    border_color="gray",
                    placeholder_text="Digite o nome do hóspede",
                    )
hospede.pack(pady=35)



quantidade_diarias= ctk.CTkEntry(janela,
                    width=400,
                    height=50,
                    border_color="gray",
                    placeholder_text="Digite a quantidade de diárias",
                    
                    )
quantidade_diarias.pack()

valor_diarias = ctk.CTkEntry(janela,
                    width=400,
                    height=50,
                    border_color="gray",
                    placeholder_text="Digite o valor da diária",
                    
                    )
valor_diarias.pack(pady=35)




botao = ctk.CTkButton(
    janela, 
    width=400, 
    height=45, 
    text="CALCULAR HOSPEDAGEM", 
    fg_color="#1d4ed8", 
    text_color="white", 
    font=("Arial", 14, "bold"), 
    command=calcular, 
    hover_color="#2563eb"
)
botao.pack(pady=(0, 25))


resultado = ctk.CTkLabel(
    janela, text="", width=400, height=150,
    bg_color="#111827", font=("Courier New", 15, "bold"),
    justify="left", anchor="w",  text_color="white"
)
resultado.pack(padx=25, pady=10)

janela.mainloop()