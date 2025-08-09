import time
import os
import random

# x, y = angka, banyak angka
NUMBER_COUNTS = [
    ('2', 60),
    ('3', 70),
    ('4', 60),
    ('5', 60),
    ('6', 100),
]
HEART_HEIGHT = 21
HEART_WIDTH = 40

def buat_peta_hati():
    
    positions = []
    for y in range(10, -10, -1):
        for x in range(-20, 20):
            if ((x * 0.075)**2 + (y * 0.15)**2 - 1.01)**3 - (x * 0.075)**2 * (y * 0.15)**3 <= 0:
                row_idx = 10 - y
                col_idx = 20 + x
                positions.append((row_idx, col_idx))
    time.sleep(0.3) 
    return positions

def jalankan_animasi(posisi, kuota, lebar, tinggi):
    

    display_canvas = [[" " for _ in range(lebar)] for _ in range(tinggi)]
    current_number_index = 0
    count_for_current_number = 0
    print("Hal yang paling kusuka didekatmu")
    print("Kau adalah orang favoritku")
    print("Nomor satu")

    for row_index, col_index in posisi:
        if current_number_index >= len(kuota):
            break

        number_char, quota_limit = kuota[current_number_index]

        display_canvas[row_index][col_index] = number_char
        count_for_current_number += 1

        os.system('cls' if os.name == 'nt' else 'clear')
        for row in display_canvas:
            print("".join(row))
        time.sleep(0.003)

        if count_for_current_number >= quota_limit:
            current_number_index += 1
            count_for_current_number = 0
    
    return display_canvas

def efek_typing(teks, speed=0.05):
    for char in teks:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()  # new

def tampilkan_pesan_akhir(canvas_final, lebar):
    closing_text = "Isinya namamuu"
    closing_text2 = "HURUF BESAR SEMUA"
    centered_text = closing_text.center(lebar)
    centered_text2 = closing_text2.center(lebar)
    
    print()
    efek_typing(centered_text, speed=0.1)
    efek_typing(centered_text2, speed=0.1)
    time.sleep(0.06)

def main():
    """
    Fungsi utama yang mengatur alur keseluruhan program.
    """
    posisi_hati = buat_peta_hati()
    canvas_terakhir = jalankan_animasi(posisi_hati, NUMBER_COUNTS, HEART_WIDTH, HEART_HEIGHT)
    tampilkan_pesan_akhir(canvas_terakhir, HEART_WIDTH)

# Titik masuk program: Ini adalah baris pertama yang akan dieksekusi
if __name__ == "__main__":
    main()
