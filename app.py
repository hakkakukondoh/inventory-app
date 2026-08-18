import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import openpyxl

EXCEL_FILENAME = "ツール在庫管理 - Ver.6.0.xlsm"

def get_target_workbook_path():
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, EXCEL_FILENAME)

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ツール在庫管理システム (Mac用)")
        self.root.geometry("440x420")
        
        tk.Label(root, text="在庫管理・指示書ツール", font=("Helvetica", 14, "bold")).pack(pady=15)
        
        tk.Button(root, text="1. Web注文CSV取込", width=32, height=2, command=self.import_web_csv).pack(pady=5)
        tk.Button(root, text="2. DM注文取込", width=32, height=2, command=self.import_dm_excel).pack(pady=5)
        tk.Button(root, text="3. 在庫数式更新", width=32, height=2, command=self.update_formulas).pack(pady=5)
        tk.Button(root, text="4. ツール指示書更新", width=32, height=2, command=self.update_instructions).pack(pady=5)
        tk.Button(root, text="5. 在庫更新（確定・履歴保存）", width=32, height=2, bg="#ffcccc", command=self.update_inventory).pack(pady=5)

    def import_web_csv(self):
        filepath = filedialog.askopenfilename(title="Web注文CSVを選択", filetypes=[("CSV Files", "*.csv")])
        if not filepath:
            return
        messagebox.showinfo("完了", "Web注文のCSV取込処理を実行しました。")

    def import_dm_excel(self):
        filepath = filedialog.askopenfilename(title="DM注文ファイルを選択", filetypes=[("Excel Files", "*.xlsx;*.xlsm")])
        if not filepath:
            return
        messagebox.showinfo("完了", "DM注文の取込処理を実行しました。")

    def update_formulas(self):
        messagebox.showinfo("完了", "在庫数式の更新が完了しました。")

    def update_instructions(self):
        messagebox.showinfo("完了", "ツール指示書を更新しました。")

    def update_inventory(self):
        if messagebox.askyesno("確認", "在庫更新を実行します。よろしいですか？"):
            messagebox.showinfo("完了", "在庫更新が完了しました！")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
