import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
# print(caminho)

lista_arquivos = os.listdir(caminho)
# print(lista_arquivos)

locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".JPG", ".HEIC", ".PNG", ".JPEG", ".heic", ".GIF"],
    "planilhas": [".xlsx", ".csv"],
    "PDF": [".pdf"],
    "ZIP": [".zip", ".rar"],
    "audio": [".mp3", ".ogg"],
    "video": [".mp4", ".mov"],
    "documentos": [".docx"],
    "executaveis": [".exe"],
    "json": [".json"],
    "bd": [".sql"],
    "txt": [".txt"],
    "php": [".php"],
    "slides": [".pptx"]
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")