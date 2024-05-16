# CE Saat - Python ile Dijital Saat Uygulaması

Bu doküman, Python programlama dili ve Tkinter kütüphanesi kullanılarak oluşturulan bir dijital saat uygulamasının nasıl yapıldığını adım adım açıklamaktadır. Kod örneği, gerçek zamanlı olarak güncellenen bir saat göstermek için kullanılabilir.

## Gerekli Kütüphaneler

Bu uygulamayı oluşturmak için aşağıdaki kütüphanelere ihtiyacınız olacak:

### tkinter: Python'un standart GUI (grafik kullanıcı arayüzü) kütüphanesi.
### time: Zamanla ilgili fonksiyonlar sağlayan standart Python kütüphanesi.

## Kodun Açıklaması

### 1. Ana Pencere Oluşturulması

İlk olarak, Tkinter kütüphanesi kullanılarak ana pencere oluşturulur ve pencereye bir başlık atanır.

from tkinter import Tk, Label
from time import strftime

# Ana pencere oluşturuluyor
root = Tk()
root.title("CE Saat")

### 2. Saat Güncelleme Fonksiyonu

Saatin her 100 milisaniyede bir güncellenmesi için bir fonksiyon tanımlanır. Bu fonksiyon, strftime fonksiyonunu kullanarak geçerli zamanı alır ve bu zamanı Label widget'ına günceller. Ardından, fonksiyon kendini 100 milisaniye sonra tekrar çağırır.

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

### 3. Label Widget'ının Oluşturulması

Saatin görüntüleneceği bir Label widget'ı oluşturulur. Bu widget, dijital saat görünümü vermek için belirli bir font, arka plan rengi ve yazı rengi ile ayarlanır.

# Saatin görüntüleneceği Label widget'ı oluşturuluyor
label = Label(root, font=('DS-DIGIT', 100), background='black', foreground='white')
label.pack(anchor='center')

### 4. Saat Güncellemeyi Başlatma

Saatin güncellenmeye başlanması için clock fonksiyonu çağrılır.

# Saat güncellemeyi başlat
clock()

### 5. Ana Döngünün Başlatılması

Tkinter ana döngüsü başlatılarak GUI'nin çalışması sağlanır.

# Ana döngüyü başlat
root.mainloop()

# Sonuç
Bu doküman, Tkinter ve Python kullanarak basit bir dijital saat uygulaması yapmayı göstermektedir. Uygulamayı geliştirerek farklı özellikler ekleyebilir veya görsel olarak daha çekici hale getirebilirsiniz.


