#!/bin/bash

# Bonzi Friend'u başlatmak için gereken komutlar
echo "Downloading and running the necessary files to start Bonzi Friend..."
pip install -r requirements.txt  # Gerekli Python kütüphanelerini yükle
python bonzi.py  # Bonzi Friend'u başlat

# İşlem tamamlandığında kullanıcıya bir mesaj gönder
echo "Bonzi Friend successfully launched!"
