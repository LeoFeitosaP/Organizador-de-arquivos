import os
import shutil

diretorio = r'C:\Users\leona\Desktop\Projetos Pessoais\Arquivos' # Altere para o diretório que você deseja organizar

#Definindo os arquivos que serão organizados
tipos_arquivos = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documentos': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Áudios': ['.mp3', '.wav', '.aac'],
    'Vídeos': ['.mp4', '.mov', '.avi'],
    'Compactados': ['.zip', '.rar', '.7z'],
    'Outros': []
}

#Criando pastas que ainda não existem
for pasta in tipos_arquivos.keys():
    caminho_pasta = os.path.join(diretorio, pasta)
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

#Percorrendo os arquivos no diretório
for arquivo in os.listdir(diretorio):
    caminho_arquivo = os.path.join(diretorio, arquivo)
    if os.path.isfile(caminho_arquivo):
        _, extensao = os.path.splitext(arquivo)
        movido = False
        for pasta, extensoes in tipos_arquivos.items():
            if extensao.lower() in extensoes:
                shutil.move(caminho_arquivo, os.path.join(diretorio, pasta, arquivo))
                movido = True
                break
        if not movido:
            shutil.move(caminho_arquivo, os.path.join(diretorio, 'Outros', arquivo))