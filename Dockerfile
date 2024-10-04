# Temel imaj olarak resmi Python imajını kullanıyoruz
FROM python:3.12-slim

# Gerekli paketleri yükle
RUN apt update && apt install -y \
    chromium \
    && apt clean

# Çalışma dizinini oluştur ve ayarla
WORKDIR /app

# Gereksinimler dosyasını çalışma dizinine kopyala
COPY requirements.txt .

# Gereksinimleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını çalışma dizinine kopyala
COPY . .

# Uygulamayı başlat
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
