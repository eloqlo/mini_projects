import random
import tkinter as tk
from tkinter import messagebox

def show_random_quote():
    file_path = r"C:\Users\jaeng\Desktop\VSC\mini_project\quote_popup_program\quotes.txt"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            quotes = file.readlines()
        
        if quotes:
            quote = random.choice(quotes).strip()
            
            # 팝업 창 생성
            root = tk.Tk()
            root.withdraw()  # 메인 창 숨기기
            messagebox.showinfo("오늘의 명언", quote)
            root.destroy()
        else:
            print("명언 파일이 비어 있습니다.")
    
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")

if __name__ == "__main__":
    show_random_quote()
    # input()