import re 

# Padrão de Exemplo.
padrao = "[0-9][a-z][0-9]"
texto = "123 1a2 acc aa1"
resposta = re.search(padrao, texto)
# Group função que retorna o padrão encontrado.
print(resposta.group())

# Construindo Padrão de Email. 
# xxxxx@gmail.com.br
padrao_email = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}" # Generalização
padrao_email_dois = "\w{5,50}@[a-z]{3,10}.com.br"  # Especialização
email = "aaabbbccc rodrigo123@gmail.com.br gddfss ksksjd hdgdgd"
resposta = re.search(padrao_email_dois, email)
print(resposta.group())

# Construindo padrão de telefone.
# Molde (xx)aaaa-wwww
padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "eu gosto do número 2126451234 eu gosto também do 2136431234"
resposta = re.findall(padrao, texto)
print(resposta)
resposta = re.search(padrao, texto)
print(resposta.group())

# Agrupamento dos números com ().
# Molde (xx)aaaa-wwww
padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
texto = "552126481234"
resposta = re.findall(padrao, texto)
print(resposta)
resposta = re.search(padrao, texto).group()
print(resposta)

# Excercicio
email_um = 'rodrigo@gmail.com'
email_dois = 'rodrigao1993@4shared.org.uk'
email_tres = 'rodrigo@rodrigo.br'
email_quatro = 'rodrigo123@python.py.br'
lista_email = [email_um, email_dois, email_tres, email_quatro]
padrao = "(\w{2,50})(@)(\w{2,15})(\.)([a-z]{2,3})(\.)?([a-z]{2,3})?"

for ele in lista_email:
    resposta = re.search(padrao, ele)
    print(resposta.group())
    resposta = re.findall(padrao, ele)
    print(resposta)