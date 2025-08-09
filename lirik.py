import os
import time
import HEART
lirik = [
    ("hal yang paling kusuka didekatmu", 2),
    ("kau adalah orang favoritku", 1.4),
    ("nomor satu", 1.5),
    ("nomor", 0.4),
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ketik_teks(teks, speed=0.06):
    for char in teks:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

def main():
    clear_screen() 
    
    for i, (teks, delay) in enumerate(lirik):
        if i > 0:
            time.sleep(delay_sebelumnya)

        ketik_teks(teks)
        delay_sebelumnya = delay
    clear_screen()
    print("Hal yang paling kusuka didekatmu")
    print("Kau adalah orang favoritku")
    print("Nomor satu")
    print("Nomor")

    # delay lirik ke heart
    time.sleep(0.2)
    # heart
    HEART.buat_peta_hati()
    HEART.jalankan_animasi(HEART.buat_peta_hati(), HEART.NUMBER_COUNTS, HEART.HEART_WIDTH, HEART.HEART_HEIGHT)
    HEART.tampilkan_pesan_akhir((HEART.buat_peta_hati(), HEART.NUMBER_COUNTS, HEART.HEART_WIDTH, HEART.HEART_HEIGHT), HEART.HEART_WIDTH)
    




if __name__ == "__main__":
    main()
