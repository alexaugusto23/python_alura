from contatos_utils import csv_para_contatos, write_contatos_para_pickle, read_pickle_para_contatos, write_contatos_para_json, read_json_para_contatos

path_main = r'C:\Users\alexsandro.ignacio\OneDrive - WCA Soluções de Inteligência Comercial\Documentos\Docs\Git\python_alura\Python parte 11 IO'
path = path_main +'/dados/contatos.csv'
path_pickle = path_main +'/dados/contatos.pickle'
path_json = path_main +'/dados/contatos.json'

try:
    # contatos = csv_para_contatos(path)
    # write_contatos_para_pickle(contatos, path_pickle)

    # contatos = read_pickle_para_contatos(path_pickle)
    # write_contatos_para_json(contatos, path_json) 

    contatos = read_json_para_contatos(path_json) 

    for contato in contatos:
        print(f"{contato.id} - {contato.nome} - {contato.email}")

except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem prermissão de escrita')

