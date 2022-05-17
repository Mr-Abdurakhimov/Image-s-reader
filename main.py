from rich.prompt import Prompt
import pytesseract
from pathlib import Path
from PIL import Image
from art import tprint

pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract\tesseract.exe'


def GetTextFromImage(path, language):
    if Path(path).exists():
        print(f"--> Your origin file: {Path(path).name}")
        try:
            with Image.open(path) as text:
                outtext = pytesseract.image_to_string(text, lang=language)
            name = Path(path).stem
            print('Processing...')
            with open(f"{name}.txt", 'w', encoding='utf-8') as file:
                file.write(outtext)
                print(f"{name}.txt was successfully saved")
        except:
            raise Exception("Something went wrong")


def main():
    tprint("Image's reader")
    file_path = input("Enter the path to your Image: ")
    language = Prompt.ask("Choose the language: ",choices=["eng","rus"],default="eng")
    GetTextFromImage(file_path, language)


if __name__ == "__main__":
    main()
