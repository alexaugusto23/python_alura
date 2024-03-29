path_main = r'C:\Users\alexsandro.ignacio\OneDrive - WCA Soluções de Inteligência Comercial\Documentos\Docs\Git\python_alura\Python parte 11 IO'

# mode r leitura.
# mode w+ escrita + leitura.
# mode w sobrescreve os dados existentes.
# mode a adiciona o dado aos daods existentes.

arquivo_contatos = open(file= path_main +'/dados/contatos-escrita.csv', encoding='latin_1', mode='w+', )

contatos = ['11,Carol,carol@carol.com.br\n',
            '12,Ana,ana@ana.com.br\n',
            '13,Tais,tais@tais.com.br\n',
            '14,Felipe,felipe@felipe.com.br\n']

# função para escrita de dados
for contato in contatos: 
    arquivo_contatos.write(contato)

arquivo_contatos.flush() # força a escrita ao mesmo tempo com o arquivo aberto.

# força o ponteiro voltar no primeiro caractere passado como parâmetro. 
arquivo_contatos.seek(29)
arquivo_contatos.write('12,Ana,ana@ana.com.br\n'.upper())
arquivo_contatos.flush()
arquivo_contatos.seek(0)

for linha in arquivo_contatos:
    print(linha)

# input('Pressione <Enter> para encerrar o programa')
# arquivo_contatos.close() encerra o arquivo