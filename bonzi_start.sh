#!/bin/bash

# Bonzi Friend'u başlatmak için gereken komutlar
echo "Downloading and running the necessary files to start Bonzi Friend..."

# Gerekli Python kütüphanelerini yükle
pip install -r requirements.txt

# Kullanıcıya hangi dosyanın çalıştırılacağını sorsun
echo "Which file do you want to run: bonzi.py or bonzi_movement3.py?"
read choice

if [ "$choice" = "bonzi.py" ]; then
    python bonzi.py  # bonzi.py dosyasını çalıştır
elif [ "$choice" = "bonzi_movement3.py" ]; then
    python bonzi_movement3.py  # bonzi_movement3.py dosyasını çalıştır
else
    echo "Invalid choice. Exiting..."
    exit 1
fi

# İşlem tamamlandığında kullanıcıya bir mesaj gönder
echo "Bonzi Friend successfully launched!"
