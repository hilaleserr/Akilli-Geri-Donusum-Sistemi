# ♻️ Akıllı Geri Dönüşüm ve Atık Tespit Sistemi

Bu proje, görüntü işleme ve derin öğrenme algoritmaları kullanarak bilgisayar kamerası üzerinden gerçek zamanlı atık tespiti yapan yapay zeka tabanlı bir sistemdir. Geri dönüşüm süreçlerini otomatize etmek ve çevre bilincini teknolojiyle birleştirmek amacıyla geliştirilmiştir.

## 🚀 Projenin Özellikleri
* **Gerçek Zamanlı Tespit:** Kamera üzerinden anlık olarak atıkların algılanması ve sınıflandırılması.
* **Modern Kullanıcı Arayüzü (Dashboard):** Streamlit tabanlı, kullanıcı dostu ve istatistikleri canlı gösteren web arayüzü.
* **Dinamik Hassasiyet Ayarı:** Arayüz üzerinden modelin algılama güven eşiğinin (confidence threshold) anlık olarak değiştirilebilmesi.
* **Canlı İstatistikler:** O an ekranda tespit edilen atık türlerinin sayılarının eşzamanlı olarak takip edilebilmesi.

---

## 🧠 Geliştirme Süreci: Neler Yaptık, Nasıl Çalışıyor?

Bu sistem sıfırdan, veri mühendisliğinden başlayarak son kullanıcı arayüzüne kadar titiz bir süreçle inşa edilmiştir.

### 1. Veri Seti ve Sınıflar (Veri Mühendisliği)
Sistemin atıkları doğru tanıyabilmesi için **Roboflow** üzerinden zenginleştirilmiş özel bir veri seti kullanıldı. Veri seti, modelin atıkları farklı açılardan, ışık koşullarından ve arka planlardan öğrenebilmesi için artırma (augmentation) teknikleriyle çoğaltılarak yaklaşık **8.150 fotoğrafa** çıkarıldı. 
Model şu an 4 ana atık sınıfını tanımaktadır:
* `Glass` (Cam Atıklar)
* `Metal` (Metal Kutular/Atıklar)
* `Plastic` (Plastik Şişeler ve Ambalajlar)
* `Vinyl` (Vinil/Poşet Atıklar)

### 2. Yapay Zeka Modelinin Eğitimi (Model Training)
Projenin "beynini" oluşturmak için Ultralytics'in en güncel ve hızlı mimarilerinden biri olan **YOLOv8s (YOLOv8 Small)** tercih edilmiştir. 
* Eğitim, donanımsal kısıtlamaları aşmak ve en yüksek verimi almak adına **Google Colab** üzerinde, NVIDIA Tesla T4 GPU kullanılarak gerçekleştirilmiştir.
* Model toplamda **50 Epoch** (tur) boyunca eğitilmiş ve nesneleri ayırt etme yeteneği (mAP50) adım adım yükseltilmiştir. 
* **Eğitim Sonuçları ve Başarı Oranları:**
  Eğitim sonucunda modelimiz, özellikle ana atık türlerinde yüksek doğruluk oranlarına ulaşmıştır:
  * **Plastik:** %86.8 Başarı
  * **Cam:** %77.8 Başarı
  * **Metal:** %74.3 Başarı

### 3. Sistem Entegrasyonu ve Arayüz
Eğitilen modelin ağırlıkları (`best.pt`), yerel bilgisayardaki Python projesine entegre edilmiştir. Sadece siyah bir terminal ekranı yerine, sistemin görselleştirilmesi için `Streamlit` ve `OpenCV` kullanılarak modern bir gösterge paneli (Dashboard) programlanmıştır. BGR'den RGB'ye renk dönüşümleri optimize edilerek yüksek FPS'de akıcı bir görüntü sağlanmıştır.

---

## 🛠️ Kullanılan Teknolojiler
* **YOLOv8 (Ultralytics):** Nesne tespiti (Object Detection) ve model eğitimi.
* **Python:** Ana programlama dili.
* **OpenCV:** Kamera erişimi, görüntü okuma ve kare çizimleri.
* **Streamlit:** Web tabanlı canlı dashboard (arayüz) geliştirme.
* **Roboflow:** Veri seti etiketleme, versiyonlama ve çoğaltma.
* **Google Colab:** Bulut tabanlı GPU ile derin öğrenme eğitimi.

---

## 📂 Dosya Yapısı
Proje klasörü, karmaşadan uzak ve temiz bir mimariyle tasarlanmıştır:
* `best.pt`: 50 epoch boyunca eğitilmiş, sistemin nesneleri tanımasını sağlayan yapay zeka ağırlık dosyası.
* `dashboard_app.py`: Streamlit kullanarak canlı kamera görüntüsünü ve istatistikleri ekrana yansıtan ana arayüz kodumuz.
* `kamera_test.py`: Kameranın ve modelin temel seviyede çalışıp çalışmadığını test eden geliştirici betiği.
* `Sistemi_Baslat.bat`: Windows kullanıcılarının projeyi kod yazmadan tek tıkla başlatmasını sağlayan otomasyon dosyası.
* `requirements.txt`: Projenin çalışması için gereken Python kütüphanelerinin listesi.

---

## 💻 Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

**1. Projeyi Klonlayın**
```bash
git clone [https://github.com/KULLANICI_ADIN/Akilli-Geri-Donusum-Sistemi.git](https://github.com/KULLANICI_ADIN/Akilli-Geri-Donusum-Sistemi.git)
cd Akilli-Geri-Donusum-Sistemi
2. Gerekli Kütüphaneleri Kurun
Projenin çalışması için gereken bağımlılıkları yükleyin:

Bash
pip install -r requirements.txt
3. Uygulamayı Başlatın
Streamlit arayüzünü ayağa kaldırmak için terminale şu komutu girin:

Bash
streamlit run dashboard_app.py
(Alternatif olarak Windows ortamında doğrudan Sistemi_Baslat.bat dosyasına çift tıklayarak sistemi başlatabilirsiniz.)

"Bu proje, sürdürülebilir bir gelecek için teknolojik çözümler üretme motivasyonuyla geliştirilmiştir." 🌍♻️