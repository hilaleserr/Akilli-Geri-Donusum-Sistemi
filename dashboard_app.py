import streamlit as st
from ultralytics import YOLO
import cv2
import PIL.Image

# --- DASHBOARD AYARLARI ---
st.set_page_config(page_title="Akıllı Geri Dönüşüm Paneli", layout="wide")
st.title("♻️ Akıllı Geri Dönüşüm Tespit Sistemi")
st.write("Sistem şu an canlı olarak atıkları analiz ediyor...")

# --- YAN MENÜ (SIDEBAR) ---
st.sidebar.header("Sistem Ayarları")
# Algılama hassasiyetini buradan canlı değiştirebilirsin
conf_threshold = st.sidebar.slider("Algılama Hassasiyeti (Confidence)", 0.0, 1.0, 0.4)
model_yolu = "best.pt" # Dosya isminin doğru olduğundan emin ol

# --- MODELİ YÜKLE ---
try:
    model = YOLO(model_yolu)
except Exception as e:
    st.error(f"Model yüklenemedi: {e}")

# --- CANLI GÖRÜNTÜ ALANI ---
sol_kolon, sag_kolon = st.columns([2, 1])
goruntu_alani = sol_kolon.empty()
sayaç_alani = sag_kolon.empty()

# --- KAMERA DÖNGÜSÜ ---
kamera = cv2.VideoCapture(0)

while True:
    basarili, kare = kamera.read()
    if not basarili:
        st.error("Kamera bağlantısı kesildi!")
        break

    # Nesne Tespit Et
    sonuclar = model.predict(source=kare, conf=conf_threshold)
    cizimli_kare = sonuclar[0].plot()
    
    # BGR'den RGB'ye dönüştür (Streamlit için gerekli)
    rgb_kare = cv2.cvtColor(cizimli_kare, cv2.COLOR_BGR2RGB)
    
    # Dashboard'u Güncelle
    goruntu_alani.image(rgb_kare, channels="RGB", use_container_width=True)
    
    # Sağ tarafa canlı istatistikleri yaz
    tespit_edilenler = sonuclar[0].boxes.cls.tolist()
    names = model.names
    
    with sayaç_alani.container():
        st.subheader("📊 Canlı İstatistik")
        for class_id in set(tespit_edilenler):
            sayi = tespit_edilenler.count(class_id)
            st.metric(label=f"Tespit Edilen {names[int(class_id)]}", value=sayi)