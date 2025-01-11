from pytube import YouTube
import os

def converter_youtube_para_mp3(url_video, nome_arquivo_mp3):
    # Baixar o vídeo do YouTube como áudio
    youtube = YouTube(url_video)
    stream = youtube.streams.filter(only_audio=True).first()
    caminho_video = stream.download()

    # Renomear o arquivo para MP3
    novo_caminho = f"{nome_arquivo_mp3}.mp3"
    os.rename(caminho_video, novo_caminho)
    print(f"Áudio convertido para {novo_caminho}")

# Exemplo de uso
url = input("Digite a URL do Youtube: ")
nome_mp3 = "musica_convertida.mp3"
converter_youtube_para_mp3(url, nome_mp3)
