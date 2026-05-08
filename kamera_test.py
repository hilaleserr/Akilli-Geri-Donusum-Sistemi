from ultralytics import YOLO
import cv2

# 'best.pt' yerine tam adresi yazıyoruz (Ters slashlara dikkat!)
model = YOLO(r"c:\Users\hsuhe\Desktop\dijitalgörüntüçözümleme\best.pt")

# 2. Bilgisayarın kamerasını açıyoruz (0 varsayılan kameradır)
kamera = cv2.VideoCapture(0)

print("Sistem hazır. Kameradan çıkmak için 'q' tuşuna basın.")

while True:
    basarili, kare = kamera.read()
    if not basarili:
        break

    # 3. Kameradan gelen her kareyi modele soruyoruz
    # conf=0.5 diyerek sadece %50'den emin olduğu nesneleri göstermesini sağlıyoruz
    sonuclar = model.predict(source=kare, conf=0.5)

    # 4. Tespit edilen nesnelerin kutularını çiziyoruz
    cizimli_kare = sonuclar[0].plot()

    # 5. Sonucu ekrana yansıtıyoruz
    cv2.imshow("Akilli Geri Donusum Tespit Sistemi", cizimli_kare)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()