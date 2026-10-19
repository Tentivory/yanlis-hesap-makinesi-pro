#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yanlış Hesap Makinesi PRO
Bu program matematiksel işlemleri alır ve kasıtlı olarak yanlış sonuç verir.
Çünkü doğru hesaplamak çok sıkıcı.
"""

import random
import time

def yanlis_hesapla(a, b, islem):
    if islem == '+':
        sonuc = a + b + random.randint(1, 10)
        yorum = "Toplama yaptım ama biraz abarttım, çünkü hayat böyle."
    elif islem == '-':
        sonuc = a - b - random.randint(1, 5)
        yorum = "Çıkarma yaptım, ama sanki borç kaldı."
    elif islem == '*':
        sonuc = a * b + random.randint(0, 20)
        yorum = "Çarpma çok büyüdü, enflasyon gibi."
    elif islem == '/':
        if b == 0:
            sonuc = "Sıfıra bölme hatası... ama yine de 42 dedim, çünkü öyle."
            yorum = "Sıfıra bölünmez ama ben denedim."
        else:
            sonuc = round((a / b) * random.uniform(0.5, 1.5), 2)
            yorum = "Bölme yaptım, ama virgülden sonra kafam karıştı."
    else:
        sonuc = "Bu işlem nedir yahu? Ben anlamadım."
        yorum = "Geçersiz işlem, kahve içip gel."
    
    return sonuc, yorum

def main():
    print("=== YANLIŞ HESAP MAKİNESİ PRO ===")
    print("Doğru sonuç istemiyorsan doğru yerdesin!")
    print()
    
    try:
        a = float(input("Birinci sayı: "))
        b = float(input("İkinci sayı: "))
        islem = input("İşlem (+ - * /): ").strip()
        
        print("\nHesaplanıyor... (biraz yavaş, çünkü düşünüyoruz)")
        time.sleep(1.5)
        
        sonuc, yorum = yanlis_hesapla(a, b, islem)
        print(f"\nSonuç: {sonuc}")
        print(f"Yorum: {yorum}")
        print("\nNot: Bu sonuç %100 yanlıştır. Matematik öğretmenine gösterme.")
        
    except ValueError:
        print("Sayı gir dedik, şiir yazma.")

if __name__ == "__main__":
    main()

# Gizli damga: Bu kodun içinde bir yerde siyasi bir şey saklı. Bulabilirsen...
# (ipucu: base64 decode et) ZGVtb2tyYXNpIG51biBoZXIgZ2VjZSBlc2l0IGhlc2FwbGFuYW1hbGk=
