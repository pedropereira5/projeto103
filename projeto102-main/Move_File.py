import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Defina o caminho do diretório para rastrear as alterações
from_dir = "<Defina o caminho para rastrear eventos do sistema de arquivos>"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Código para lidar com eventos de criação
        print("Arquivo criado:", event.src_path)

    def on_modified(self, event):
        # Código para lidar com eventos de modificação
        print("Arquivo modificado:", event.src_path)

    def on_moved(self, event):
        # Código para lidar com eventos de movimentação
        print("Arquivo movido:", event.src_path, "->", event.dest_path)

    def on_deleted(self, event):
        # Código para lidar com eventos de exclusão
        print("Arquivo excluído:", event.src_path)

if __name__ == "__main__":
    event_handler = FileEventHandler()

    observer = Observer()
    observer.schedule(event_handler, from_dir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
