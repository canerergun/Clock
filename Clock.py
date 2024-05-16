from tkinter import Tk, Label
from time import strftime

# Ana pencere oluşturuluyor
root = Tk()
root.title("CE Saat")

def clock():
    """
    Saatin güncellenmesi için kullanılan fonksiyon.
    Her 100 milisaniyede bir çağrılarak saati günceller.
    """
    # Geçerli zamanı 'saat:dakika:saniye' formatında al
    text = strftime('%H:%M:%S')
    # Label widget'ını yeni zaman ile güncelle
    label.config(text=text)
    # Fonksiyonu 100 milisaniye sonra tekrar çalıştır
    label.after(100, clock)

# Saatin görüntüleneceği Label widget'ı oluşturuluyor
label = Label(root, font=('DS-DIGIT', 100), background='black', foreground='white')
label.pack(anchor='center')

# Saat güncellemeyi başlat
clock()

# Ana döngüyü başlat
root.mainloop()
