♻️ Akıllı Geri Dönüşüm ve Atık Tespit Sistemi
Bu proje, görüntü işleme ve derin öğrenme algoritmaları kullanarak bilgisayar kamerası üzerinden gerçek zamanlı veya yüklenen fotoğraflar üzerinden statik atık tespiti yapan yapay zeka tabanlı bir sistemdir. Geri dönüşüm süreçlerini otomatize etmek ve çevre bilincini teknolojiyle birleştirmek amacıyla uçtan uca (end-to-end) tasarlanmıştır.

🚀 Projenin Özellikleri
Çoklu Tespit Modu: Sistem hem bilgisayar kamerasından gerçek zamanlı (real-time) video akışını hem de dışarıdan yüklenen (.jpg, .png) fotoğrafları analiz edebilmektedir.

Modern Kullanıcı Arayüzü (Dashboard): Streamlit tabanlı, kullanıcı dostu ve iki farklı sekmeyle (Upload ve Live Camera) çalışan modern web arayüzü.

Dinamik Hassasiyet Ayarı: Arayüzdeki yan menü üzerinden modelin algılama güven eşiğinin (confidence threshold) anlık olarak değiştirilebilmesi.

Yüksek Çıkarım Hızı: Modelin BGR-RGB dönüşümleri optimize edilerek görsel başına ortalama 4.5ms hızında akıcı bir tespit performansı sağlanmıştır.

🧠 Geliştirme Süreci: Neler Yaptık, Nasıl Çalışıyor?
Bu sistem sıfırdan, veri mühendisliğinden başlayarak son kullanıcı arayüzüne kadar titiz bir süreçle ve akademik gereksinimlere (proje yönergelerine) tam uyum sağlayacak şekilde inşa edilmiştir.

1. Veri Mühendisliği ve Manuel Veri Bölme (Data Split)
Sistemin atıkları doğru tanıyabilmesi için Roboflow üzerinden zenginleştirilmiş özel bir veri seti kullanıldı. Veri seti, modelin atıkları farklı açılardan ve ışık koşullarından öğrenebilmesi için yaklaşık 8.153 fotoğrafa çıkarıldı.
Proje gereksinimlerine ve akademik literatüre uygun olarak modelin ezberlemesini (overfitting) önlemek amacıyla veri seti manuel olarak %80 Eğitim (6522 görsel) ve %20 Doğrulama (1631 görsel) olacak şekilde ikiye ayrılmıştır. Model şu an 4 ana atık sınıfını tanımaktadır: Glass (Cam), Metal, Plastic (Plastik) ve Vinyl (Vinil/Poşet).

2. Yapay Zeka Modelinin Eğitimi (Model Training)
Projenin "beynini" oluşturmak için Ultralytics'in nesne tespitinde en güncel ve hızlı mimarilerinden biri olan YOLOv8s (YOLOv8 Small) tercih edilmiştir. Eğitim, donanımsal kısıtlamaları aşmak ve en yüksek verimi almak adına Google Colab üzerinde, NVIDIA Tesla T4 GPU kullanılarak gerçekleştirilmiştir. Model toplamda 50 Epoch (tur) boyunca eğitilmiştir.

3. Değerlendirme Metrikleri ve Başarı Oranları
Eğitim sonucunda modelimiz, özellikle en çok karşılaşılan ana atık türlerinde üst düzey doğruluk oranlarına ulaşmıştır. Eğitim grafikleri ve karmaşıklık matrisi detayları results.png dosyası ile ayrıca raporlanmıştır. Doğrulama (Validation) seti üzerinden elde edilen nihai başarı metrikleri şunlardır:

Genel Başarı Oranı (mAP50): %88.0

Plastik Başarısı: %96.6

Metal Başarısı: %95.6

Cam (Glass) Başarısı: %91.9

Vinil Başarısı: %67.9

4. Sistem Entegrasyonu ve Web Arayüzü
Eğitilen modelin ağırlıkları (best.pt), yerel bilgisayardaki Python projesine entegre edilmiştir. Sadece siyah bir terminal ekranı yerine, sistemin görselleştirilmesi için Streamlit ve OpenCV kullanılarak hocamızın talimatlarına uygun profesyonel bir gösterge paneli (Dashboard) programlanmıştır.

🛠️ Kullanılan Teknolojiler
YOLOv8 (Ultralytics): Nesne tespiti (Object Detection) ve model eğitimi.

Python: Ana programlama dili ve sistem mantığı.

OpenCV: Kamera erişimi, görüntü okuma ve bounding-box (çerçeve) çizimleri.

Streamlit: Web tabanlı canlı dashboard (arayüz) ve dosya yükleme modülü geliştirme.

Roboflow: Veri seti etiketleme ve versiyonlama.

Google Colab: Bulut tabanlı GPU ile derin öğrenme eğitimi.

📂 Proje Yapısı

├── best.pt                # Eğitilmiş final model dosyası (Weights)
├── dashboard_app.py       # Streamlit web arayüzü ana kodu
├── requirements.txt       # Gerekli Python kütüphane listesi
├── results.png            # Eğitim başarı grafikleri (Loss, mAP)
├── README.md              # Proje dokümantasyonu
└── data/                  # Veri seti klasör yapısı (80/20 split)

💻 Kurulum ve Çalıştırma
Projeyi kendi bilgisayarınızda (yerel ortamda) çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

1. Projeyi Klonlayın
git clone https://github.com/KULLANICI_ADIN/Akilli-Geri-Donusum-Sistemi.git
cd Akilli-Geri-Donusum-Sistemi

2. Gerekli Kütüphaneleri Kurun
Projenin çalışması için gereken bağımlılıkları tek seferde yükleyin:

pip install -r requirements.txt
pip install -r requirements.txt

3. Uygulamayı Başlatın
Streamlit web arayüzünü tarayıcınızda ayağa kaldırmak için terminale şu komutu girin:

streamlit run dashboard_app.py

"Bu proje, sürdürülebilir bir gelecek için teknolojik çözümler üretme motivasyonuyla; tüm algoritmik yapısı ve veri yönetimi anlaşılarak, akademik standartlara uygun bir şekilde geliştirilmiştir." 🌍♻️
