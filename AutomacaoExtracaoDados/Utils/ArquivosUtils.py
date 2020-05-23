import os

import pandas as pd
import requests


class ArquivosUtils:
    def verificar_diretorio(self, caminho):
        if not os.path.exists(caminho):
            print("Diretorio nao encontrado. Criando diretório...")
            os.makedirs(caminho)

    def requisitar_arquivo(self, url_arquivo, caminho_destino, nome_arquivo, extencao_arquivo):
        try:
            self.verificar_diretorio(caminho_destino)
            novo_arquivo_nome = nome_arquivo + "." + extencao_arquivo
            novo_arquivo_caminho = caminho_destino + novo_arquivo_nome
            response_novo_arquivo = requests.get(url_arquivo, allow_redirects=True)
            open(novo_arquivo_caminho, 'wb').write(response_novo_arquivo.content)
            print("Request Artigo - OK")
        except:
            print("Erro na requisicao do arquivo {0}".format(url_arquivo))

    @staticmethod
    def nomear_artigo(lista_artigos_mapeados, ano_edicao, tipo_artigo):
        indice = str(len(lista_artigos_mapeados))
        return indice + "_" + str(ano_edicao) + "_" + tipo_artigo

    def criar_mapeamento_csv(self, lista_mapeamento_artigos, caminho_destino):
        try:
            self.verificar_diretorio(caminho_destino)
            mapa_artigos = pd.concat(lista_mapeamento_artigos, ignore_index=True)
            mapa_artigos.to_csv(caminho_destino + 'mapeamento_Corpus.csv', encoding='utf-8')
            print("Arquivo de mapeamento do corpus foi criado com sucesso.")
        except:
            print ("Erro na criação do csv de mapeamento")


