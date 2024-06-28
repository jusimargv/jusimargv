import os
import shutil
from pathlib import Path
ROOT_PATH = Path(__file__).parent
#os.mkdir(ROOT_PATH / "novo_diretorio")
arquivo = open(ROOT_PATH / "novo_arquivo.txt", "w")
arquivo.write("Só um teste")
arquivo.close()

os.rename(ROOT_PATH / "novo_arquivo.txt", ROOT_PATH / "Test.txt")

shutil.move(ROOT_PATH / "Test.txt", ROOT_PATH / "novo_diretorio" / "Test.txt")

os.remove(ROOT_PATH / "Test.txt")
