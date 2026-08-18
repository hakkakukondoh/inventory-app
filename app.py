import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import openpyxl

# 設定: ここを適宜調整してください
EXCEL_FILENAME = "ツール在庫管理 - Ver.6.0.xlsm"

def get_target_workbook_path():
    # ファイル選択ダイアログを表示
    root = tk.Tk()
    root.withdraw()  # メインウィンドウを非表示にする
    file_path = filedialog.askopenfilename(
        title="在庫管理Excelファイルを選択してください",
        filetypes=[("Excel files", "*.xlsx *.xlsm")]
    )
    return file_path

def main():
    # 簡単なGUIアプリの開始
    root = tk.Tk()
    root.title("在庫管理アプリ")
    root.geometry("300x200")

    label = tk.Label(root, text="在庫管理ツールへようこそ")
    label.pack(pady=20)

    def on_click():
        path = get_target_workbook_path()
        if path:
            messagebox.showinfo("選択完了", f"以下のファイルを選択しました:\n{os.path.basename(path)}")
            # ここに実際の在庫管理ロジック（openpyxl等）を記述します
        else:
            messagebox.showwarning("警告", "ファイルが選択されませんでした。")

    button = tk.Button(root, text="Excelファイルを選択", command=on_click)
    button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
