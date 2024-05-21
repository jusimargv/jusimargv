
# Old style %

nome = "Jusimar"

idade = 42

profissao ="Programador"

linguagem = "Python"

print(" Olá, eu me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}." .format( nome, idade, profissao, linguagem))
print("  ")
print(" Olá, eu me chamo {0}. Eu tenho {1} anos de idade, trabalho com {2} e estou matriculado no curso de {3}." .format( nome, idade, profissao, linguagem))
print("  ")
print(" Olá, eu me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." % ( nome, idade, profissao, linguagem))
print("  ")
print(" Olá, eu me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}." .format( nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print("  ")
print(f" Olá, eu me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")

# formatar strings com f-string

PI = 3.14159

print(f"Valor de PI:  {PI: .2f}")

print(f" Valor de PI:  {PI:10.2f}")