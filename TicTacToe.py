import random

def tahta_goster(tahta):
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        print(f"|   {tahta[i][0]}   |   {tahta[i][1]}   |   {tahta[i][2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def bos_kareler(tahta):
    bos = []
    for i in range(3):
        for j in range(3):
            if tahta[i][j] not in ['X', 'O']:
                bos.append((i, j))
    return bos

def kazanan(tahta, oyuncu):
    # Satır, sütun ve çapraz kontrolleri
    for i in range(3):
        if all(tahta[i][j] == oyuncu for j in range(3)) or all(tahta[j][i] == oyuncu for j in range(3)):
            return True
    if all(tahta[i][i] == oyuncu for i in range(3)) or all(tahta[i][2-i] == oyuncu for i in range(3)):
        return True
    return False

def oyuncu_hamlesi(tahta):
    while True:
        try:
            hamle = int(input("Hamleni yap (1-9): "))
            if hamle < 1 or hamle > 9:
                print("Lütfen 1 ile 9 arasında bir sayı gir.")
                continue
            satir = (hamle - 1) // 3
            sutun = (hamle - 1) % 3
            if tahta[satir][sutun] in ['X', 'O']:
                print("Burası dolu! Başka bir yer seç.")
            else:
                tahta[satir][sutun] = 'O'
                break
        except ValueError:
            print("Lütfen geçerli bir sayı gir.")

def bilgisayar_hamlesi(tahta):
    bos = bos_kareler(tahta)
    if bos:
        satir, sutun = random.choice(bos)
        tahta[satir][sutun] = 'X'

def oyun():
    tahta = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Bilgisayar ortadan başlar
    tahta[1][1] = 'X'

    while True:
        tahta_goster(tahta)

        # --- Oyuncu Hamlesi ---
        oyuncu_hamlesi(tahta)
        if kazanan(tahta, 'O'):
            tahta_goster(tahta)
            print("Kazandın!")
            break

        # Hamle kalmadıysa oyun biter (berabere)
        if not bos_kareler(tahta):
            tahta_goster(tahta)
            print("Berabere!")
            break

        # --- Bilgisayar Hamlesi ---
        print("Bilgisayar düşünüyor...")
        bilgisayar_hamlesi(tahta)
        if kazanan(tahta, 'X'):
            tahta_goster(tahta)
            print("Bilgisayar kazandı!")
            break

        # Hamle kalmadıysa yine berabere
        if not bos_kareler(tahta):
            tahta_goster(tahta)
            print("Berabere!")
            break

# --- Oyunu Başlat ---
if __name__ == "__main__":
    oyun()
