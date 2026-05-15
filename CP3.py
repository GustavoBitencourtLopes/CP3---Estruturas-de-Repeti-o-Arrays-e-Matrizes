temperaturas = [
   [28, 31, 34, 33],
   [25, 27, 29, 28],
   [32, 35, 36, 34],
   [24, 26, 25, 27]
]
# Função para encontrar a sala com maior risco
def sala_maior_risco(temperaturas):
   maior_risco = -1
   numero_sala = 0
   for i in range(len(temperaturas)):
       registros_criticos = 0
       for temperatura in temperaturas[i]:
           if temperatura >= 33:
               registros_criticos += 1
       # Verifica qual sala possui mais registros críticos
       if registros_criticos > maior_risco:
           maior_risco = registros_criticos
           numero_sala = i + 1
   return numero_sala, maior_risco

# Exibição das informações de cada sala
for i in range(len(temperaturas)):
   print(f'Sala {i + 1}')
   soma = 0
   quantidade_total = len(temperaturas[i])
   registros_criticos = 0
   for temperatura in temperaturas[i]:
       soma += temperatura
       if temperatura >= 33:
           registros_criticos += 1
   media = soma / quantidade_total
   print(f'Média: {media}')
   print(f'Registros críticos: {registros_criticos}\n')

# Chamada da função
sala, risco = sala_maior_risco(temperaturas)
print(f'A sala com maior risco é a Sala {sala}')
print(f'Quantidade de registros críticos: {risco}')
