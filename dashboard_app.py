import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np

# --- DASHBOARD AYARLARI ---
st.set_page_config(page_title="Akıllı Geri Dönüşüm Paneli", layout="wide")
st.title("♻️ Akıllı Geri Dönüşüm Tespit Sistemi")
st.write("Sistem şu an canlı olarak veya yüklenen fotoğraflar üzerinden atıkları analiz ediyor...")

# --- YAN MENÜ (SIDEBAR) ---
st.sidebar.header("⚙️ Sistem Ayarları")
# Algılama hassasiyetini buradan canlı değiştirebilirsin
conf_threshold = st.sidebar.slider("Algılama Hassasiyeti (Confidence)", 0.0, 1.0, 0.4)

model_yolu = "best.pt" # Kendi eğittiğin modelin dosya adı

# --- MODELİ YÜKLE ---
try:
    model = YOLO(model_yolu)
except Exception as e:
    st.error(f"Model yüklenemedi: {e}")
    st.stop() # Model yüklenemezse uygulamayı durdur

# --- SEKMELER (TABS) OLUŞTURMA ---
tab1, tab2 = st.tabs(["📂 Fotoğraf Yükle (Upload)", "📸 Canlı Kamera"])

# ==========================================
# 1. SEKME: DOSYA YÜKLEME (UPLOAD)
# ==========================================
with tab1:
    st.markdown("### 🖼️ Bilgisayardan Fotoğraf Yükle")
    yuklenen_dosya = st.file_uploader("Tespit edilmesini istediğiniz atık fotoğrafını seçin (JPG, PNG)", type=["jpg", "jpeg", "png"])
    
    if yuklenen_dosya is not None:
        image = Image.open(yuklenen_dosya)
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(image, caption="Yüklenen Orijinal Fotoğraf", use_container_width=True)
            analiz_butonu = st.button("🔍 Fotoğrafı Analiz Et", use_container_width=True)
            
        with col2:
            if analiz_butonu:
                with st.spinner("Yapay zeka analiz ediyor..."):
                    # YOLO ile tahmin yap
                    sonuclar = model.predict(image, conf=conf_threshold)
                    
                    # Çizilmiş resmi al ve RGB'ye çevir
                    cizilmis_resim = sonuclar[0].plot()
                    sonuc_rgb = cv2.cvtColor(cizilmis_resim, cv2.COLOR_BGR2RGB)
                    
                    st.success("✅ Tespit Tamamlandı!")
                    st.image(sonuc_rgb, caption="Yapay Zeka Sonucu", use_container_width=True)

# ==========================================
# 2. SEKME: CANLI KAMERA TESPİTİ
# ==========================================
with tab2:
    st.markdown("### 🎥 Gerçek Zamanlı Kamera Tespiti")
    st.write("Bilgisayarınızın kamerasını kullanarak anlık atık tespiti yapabilirsiniz.")
    
    # Kamerayı başlatmak/durdurmak için bir kontrol kutusu
    kamera_acik = st.checkbox("🟢 Kamerayı Başlat")
    
    # Görüntünün gösterileceği boş bir alan (placeholder) oluşturuyoruz
    ekran = st.image([])

    if kamera_acik:
        # 0 genelde bilgisayarın varsayılan (dahili) kamerasıdır. Harici kamera varsa 1 yapabilirsin.
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            st.error("Kamera açılamadı! Lütfen kamera izinlerinizi kontrol edin veya kamerayı kullanan başka bir uygulama (Zoom, Teams vb.) varsa kapatın.")
        else:
            st.success("Kamera aktif. Görüntü işleniyor...")
            
            while kamera_acik:
                ret, frame = cap.read()
                if not ret:
                    st.error("Kameradan kare okunamıyor...")
                    break
                
                # 1. Kameradan gelen görüntüyü YOLO modeline ver (anlık çıkarım)
                # verbose=False yaparak terminalin gereksiz yazılarla dolmasını engelliyoruz
                sonuclar = model.predict(frame, conf=conf_threshold, verbose=False)
                
                # 2. Modelin çizdiği (kutu içine aldığı) görüntüyü al
                cizilmis_frame = sonuclar[0].plot()
                
                # 3. OpenCV BGR formatında çalışır, Streamlit ise RGB sever. Renkleri düzeltiyoruz.
                frame_rgb = cv2.cvtColor(cizilmis_frame, cv2.COLOR_BGR2RGB)
                
                # 4. İşlenmiş görüntüyü ekrana basıyoruz
                ekran.image(frame_rgb, channels="RGB", use_container_width=True)
                
            # Döngü kırılırsa (Kamerayı durdur tikini kaldırırsan) kamerayı serbest bırak
            cap.release()