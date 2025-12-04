Conversor de Temperaturas — Python

Este projeto foi desenvolvido com o objetivo de praticar lógica de programação em Python, criando um sistema simples, mas organizado, para converter temperaturas entre diferentes escalas. O foco foi trabalhar funções, boas práticas e estruturação de um programa limpo e fácil de entender.

Objetivo do Projeto

O sistema permite converter valores de temperatura entre Celsius e Fahrenheit, retornando resultados precisos e formatados. A ideia é oferecer uma aplicação direta, funcional e que possa ser facilmente expandida.

As conversões disponíveis são:

Celsius para Fahrenheit

Fahrenheit para Celsius

Cada conversão utiliza sua fórmula específica e retorna o valor já arredondado.

Lógica Aplicada
Estrutura do Cálculo

O programa utiliza as fórmulas tradicionais de conversão entre as escalas:

Celsius → Fahrenheit:
(C × 9/5) + 32

Fahrenheit → Celsius:
(F − 32) × 5/9

A função identifica o tipo de conversão escolhido pelo usuário e aplica a fórmula correspondente.

Organização do Código

A lógica está concentrada em uma função responsável por receber a escolha e o valor, calcular o resultado e retornar o número já tratado. O código foi escrito de forma clara para facilitar sua leitura e manutenção.

Estrutura do Projeto
app_conversor_temperatura/
│
└── conversor_temperatura.py

Exemplo de Uso
from conversor_temperatura import conversor_temperatura

print(conversor_temperatura("C", 100))  # Converte Fahrenheit para Celsius
print(conversor_temperatura("F", 30))   # Converte Celsius para Fahrenheit

O que aprendi desenvolvendo este projeto

Como estruturar pequenos programas em Python de forma clara e funcional.

Importância de usar funções bem definidas para evitar repetição de código.

Diferenças entre cálculos matemáticos simples e tratamento de entradas.

Como aplicar fórmulas reais dentro de um código de maneira limpa.

A importância de organizar projetos mesmo quando eles são pequenos.

Tecnologias Utilizadas

Python 3

VS Code

Próximos Passos

Quero evoluir o projeto futuramente adicionando:

Conversão para Kelvin

Interface gráfica simples

Versão web utilizando Gradio

Validação de entrada do usuário

Criação de uma pequena API de conversão


Fique à vontade para abrir uma issue ou entrar em contato. Estou sempre buscando melhorar meus projetos e aprender novas abordagens.
