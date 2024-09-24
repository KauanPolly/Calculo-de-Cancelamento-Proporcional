import tkinter as tk
from tkinter import ttk

# Dicionário de planos com nome e valor mensal
planos = {
    1: {"nome": "400 Mega - R$ 89,90", "valor": 89.90},
    2: {"nome": "500 Mega - R$ 99,90", "valor": 99.90},
    3: {"nome": "600 Mega - R$ 109,90", "valor": 109.90},
    4: {"nome": "700 Mega - R$ 129,90", "valor": 129.90},
    5: {"nome": "800 Mega - R$ 159,90", "valor": 159.90},
    6: {"nome": "Rural - até 8 Mega - R$ 89,90", "valor": 89.90},
    7: {"nome": "Rural - até 15 Mega - R$ 119,90", "valor": 119.90},
    8: {"nome": "Plano Especial - R$ 69,90", "valor": 69.90},
    9: {"nome": "Rural - 340 Mega - R$ 159,00", "valor": 159.00},
    10: {"nome": "Rural - 500 Mega - R$ 199,90", "valor": 199.90}
}

# Dicionário com o valor dividido por dia
dividido = {
    1: {"nome": "400 Mega", "valor": 2.99},
    2: {"nome": "500 Mega", "valor": 3.33},
    3: {"nome": "600 Mega", "valor": 3.66},
    4: {"nome": "700 Mega", "valor": 4.33},
    5: {"nome": "800 Mega", "valor": 5.33},
    6: {"nome": "Rural - até 8 Mega", "valor": 2.99},
    7: {"nome": "Rural - até 15 Mega", "valor": 3.99},
    8: {"nome": "Plano Especial", "valor": 2.33},
    9: {"nome": "Rural - 340 Mega", "valor": 5.33},
    10: {"nome": "Rural - 500 Mega", "valor": 6.66}
}

# Dicionário de dias de vencimento
vencimento_dias = {
    1: {"Dia": 5},
    2: {"Dia": 10},
    3: {"Dia": 15},
    4: {"Dia": 20}
}

def calcular_valor_proporcional(valor_diario, dias):
    """Calcula o valor proporcional baseado no valor diário e dias."""
    return valor_diario * dias

def calcular_valor():
    """Calcula o valor total a ser pago com base nas opções escolhidas."""
    try:
        plano_escolhido_num = combobox_planos.current() + 1
        dia_vencimento = int(combobox_vencimentos.get())
        valor_diario = dividido[plano_escolhido_num]["valor"]
        valor_mensalidade = planos[plano_escolhido_num]['valor']
        dias_uso = int(entry_dias_uso.get())
        pagamento_realizado = combobox_pagamento.get().strip().lower()

        # Calcular o valor proporcional com base nos dias de uso
        valor_proporcional = calcular_valor_proporcional(valor_diario, dias_uso)

        if pagamento_realizado == "não":
            # Se não pagou, incluir a mensalidade completa + valor proporcional dos dias de uso
            valor_final = valor_mensalidade + valor_proporcional
        else:
            # Se já pagou, apenas o valor proporcional pelos dias de uso
            valor_final = valor_proporcional

        label_resultado.config(text=f"Valor total a ser pago: R$ {valor_final:.2f}")
    except Exception as e:
        label_resultado.config(text="Erro no cálculo. Verifique as entradas.")

# Criação da janela principal
root = tk.Tk()
root.title("Cálculo de Fatura de Internet")

# Frame principal
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill="x", expand=True)

# Label e Combobox para escolher o plano
label_plano = tk.Label(frame, text="Escolha o Plano:")
label_plano.pack(anchor="w")

combobox_planos = ttk.Combobox(frame, values=[planos[num]["nome"] for num in planos], state="readonly")
combobox_planos.pack(fill="x")
combobox_planos.set("Selecione um plano")

# Label e Combobox para escolher o dia de vencimento
label_vencimento = tk.Label(frame, text="Escolha o Dia de Vencimento:")
label_vencimento.pack(anchor="w")

combobox_vencimentos = ttk.Combobox(frame, values=[vencimento_dias[num]["Dia"] for num in vencimento_dias], state="readonly")
combobox_vencimentos.pack(fill="x")
combobox_vencimentos.set("Selecione o dia de vencimento")

# Label e Combobox para verificar se a mensalidade foi paga
label_pagamento = tk.Label(frame, text="Já pagou a mensalidade deste mês? (sim/não):")
label_pagamento.pack(anchor="w")

combobox_pagamento = ttk.Combobox(frame, values=["sim", "não"], state="readonly")
combobox_pagamento.pack(fill="x")
combobox_pagamento.set("Selecione sim ou não")

# Label e Entry para dias de uso
label_dias_uso = tk.Label(frame, text="Quantos dias utilizou o plano?")
label_dias_uso.pack(anchor="w")

entry_dias_uso = tk.Entry(frame)
entry_dias_uso.pack(fill="x")

# Botão para calcular o valor
botao_calcular = tk.Button(frame, text="Calcular Valor", command=calcular_valor)
botao_calcular.pack(pady=10)

# Label para exibir o resultado
label_resultado = tk.Label(frame, text="")
label_resultado.pack()

# Iniciar o loop principal do Tkinter
root.mainloop()
