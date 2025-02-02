### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

'''
try:
    quantidade = 10
    preco = -10

    if quantidade > 0 and preco > 0:
        print(f"Quantidade = {quantidade}.")
        print(f"Preço = {preco}.")

    elif quantidade == 0 and preco == 0:
            print("Estoque e Preço zerados!")

    elif quantidade < 0 and preco < 0:
        print(f"Favor verificar estoque e tabela de preços, pois estão negativos, acusando quantidade = {quantidade} e {preco}.")

    elif quantidade == 0:
            print("Estoque zerado!")
            print("preço: ", preco)

    elif quantidade < 0:
            print(f"Favor verificar tabela de preços, pois está acusando valor negativo = {preco}.")
            print("preço: ", preco)

    elif preco == 0:
            print(f"Quantidade = {quantidade}.")
            print("Preço zerado!")

    elif preco < 0:
            print(f"Quantidade = {quantidade}.")
            print(f"Favor verificar tabela de preços, pois está acusando valor negativo = {preco}.")

except NameError as a:
    print("Erro: Você tentou usar uma variável não definida.")  # Mensagem mais clara
    print("Detalhes do erro:", a)  # Exibe a mensagem real do erro

# except SyntaxError as b:  # Este erro não funciona porque ele é avaliado antes do código rodar, então não entra no try-except
#    print("Erro: Você tentou usar uma variável não definida.")  # Mensagem mais clara
#    print("Detalhes do erro:", b)  # Exibe a mensagem real do erro
'''



### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# o que vou fazer:
# - entrar temperatura
# - verificar se temperatura está em cada faixa
# - printar como temperatura foi classificada
'''
temp = 14

if temp < 15:
    print("temperatura está baixa:", temp, "oC.")

elif temp <= 30:
    print("temperatura está normal:", temp, "oC.")

else:
    print("temperatura está alta:", temp, "oC.")
'''

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

'''
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level'] == 'ERROR':
    print("Log de ERRO encontrado!")
    print("Ocorrência em:", log['timestamp'])
    print("Mensagem:", log['message'])
else:
    print("Nenhum log de ERRO encontradO.")
'''


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# usuarios = {'nome' : 'Paulo', 'idade' : '35'}
'''
nome = "Paulo"
email = "paulo@seuemail.com"
idade = 66

if "@" not in email or "." not in email:
    print("email inválido")
# elif not 18 <= idade <= 65:
elif idade < 18 or idade > 65:
    print("idade fora do intervalo válido")
else:
    print("Dados válidos.")
'''


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {'valor': 12000, 'hora': 20}
if transacao["valor"] > 10000 and not 9 <= transacao["hora"] <= 18:
    print("Transação suspeita. Valor acima do limite de R$ 10.000 e Horário fora do intevalo entre 9h e 18h.")
elif transacao["valor"] > 10000:
    print("Transação suspeita. Valor acima do limite de R$ 10.000.")
elif not 9 <= transacao["hora"] <= 18:
    print("Transação suspeita. Horário fora do intevalo entre 9h e 18h.")
else:
    print("Transação válida.")


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.