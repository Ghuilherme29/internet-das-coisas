import customtkinter as ctk

ctk.set_appearance_mode('dark')


janela = ctk.CTk(fg_color="#131924")

janela.geometry('500x600') 
janela.resizable(False, False)
janela.title('Resultado Acadêmico')

try:
    janela.iconbitmap("circle_icon_191833.ico")
except Exception:
    pass   
# ------------------------------------------------------

# Função do cálculo ----------------
def calcular_nota():
    try:
        val_nota1 = Nota1.get().replace(',', '.')
        val_nota2 = Nota2.get().replace(',', '.')
        nome = Nome.get().strip()

      
        if not val_nota1 or not val_nota2 or not nome:
            resultado_label.configure(
                text="Preencha todos os campos antes de calcular!", 
                text_color="orange"
            )
            return
        
        nota1 = float(val_nota1)
        nota2 = float(val_nota2)
        
        media = (nota1 + nota2) / 2
        

        if media >= 7.0:
            resultado = f"A média de {nome} é: {media:.1f}\nStatus: Aprovado"
            cor = "#00FF7F"  # Verde
        elif media >= 5.0:
            resultado = f"A média de {nome} é: {media:.1f}\nStatus: Recuperação"
            cor = "orange"
        else:
            resultado = f"A média de {nome} é: {media:.1f}\nStatus: Reprovado"
            cor = "red"  
            

        resultado_label.configure(
            text=resultado,
            text_color=cor
        )
            
    except ValueError:
        resultado_label.configure(
            text="Digite apenas números válidos nas notas!", 
            text_color="red"
        )
                


titulo = ctk.CTkLabel(
    janela, 
    text="RESULTADO ACADÊMICO", 
    font=('Arial', 22, 'bold'), 
    text_color="#EBF2FA"
)
titulo.pack(pady=20)

Nome = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    border_color="#4C6A8B",
    placeholder_text="Digite o nome do aluno"
)
Nome.pack(pady=10)

Nota1 = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    border_color="#4C6A8B",
    placeholder_text="Digite a 1ª nota"
)
Nota1.pack(pady=10)

Nota2 = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    border_color="#4C6A8B",
    placeholder_text="Digite a 2ª nota"
)
Nota2.pack(pady=10)

butao = ctk.CTkButton(
    janela,
    width=400,
    height=45,
    text="Calcular nota",
    fg_color="#2B7ED1",
    text_color="white",
    font=('Arial', 18, 'bold'),
    command=calcular_nota
)
butao.pack(pady=20)

resultado_label = ctk.CTkLabel(
    janela,
    border_width=1,
    border_color="#4C6A8B",
    text="",
    width=400,
    height=100,
    corner_radius=10,
    text_color="#EBF2FA",
    font=('Verdana', 15, 'bold')
)
resultado_label.pack(pady=10)

janela.mainloop()