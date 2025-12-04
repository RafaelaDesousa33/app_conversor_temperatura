import gradio as gr

"""
Conversor de temperatura

Permita que o usuário escolha:

Celsius → Fahrenheit

Fahrenheit → Celsius

"""

def conversor_temperatura(escolha,temperatura):
    if escolha == "F" :
        return round(temperatura * 9 / 5 + 32, 2)
    elif escolha == "C" :
        return round((temperatura - 32) * 5/9 , 2)
    else:
        return "Opcão invalida"
    
interface = gr.Interface(
    fn=conversor_temperatura,
    inputs=[
        gr.Dropdown(["F" , "C"], label="Converter para:"),
        gr.Number(label="Digite  a temperatura:"),
    ],

    outputs="text",
    description="Escolha o tipo de conversão e insira uma temperatura.",
    title="Conversor de Temperaturas"

)

interface.launch()