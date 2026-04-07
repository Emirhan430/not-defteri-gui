import tkinter as tk
from tkinter import messagebox

# Not ekleme
def not_ekle():
    not_text = entry.get()
    if not_text == "":
        messagebox.showwarning("Uyarı", "Boş not eklenemez!")
        return

    listbox.insert(tk.END, not_text)
    entry.delete(0, tk.END)

# Not silme
def not_sil():
    try:
        secili = listbox.curselection()
        listbox.delete(secili)
    except:
        messagebox.showwarning("Uyarı", "Lütfen bir not seç!")

# Notları kaydet
def kaydet():
    with open("notlar.txt", "w", encoding="utf-8") as f:
        for i in listbox.get(0, tk.END):
            f.write(i + "\n")
    messagebox.showinfo("Bilgi", "Notlar kaydedildi!")

# Notları yükle
def yukle():
    try:
        with open("notlar.txt", "r", encoding="utf-8") as f:
            for satir in f:
                listbox.insert(tk.END, satir.strip())
    except:
        pass

# Pencere
root = tk.Tk()
root.title("Not Defteri")
root.geometry("400x400")

# Giriş alanı
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Butonlar
btn_ekle = tk.Button(root, text="Not Ekle", command=not_ekle)
btn_ekle.pack()

btn_sil = tk.Button(root, text="Not Sil", command=not_sil)
btn_sil.pack()

btn_kaydet = tk.Button(root, text="Kaydet", command=kaydet)
btn_kaydet.pack()

# Liste
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

# Başlangıçta notları yükle
yukle()

root.mainloop()
