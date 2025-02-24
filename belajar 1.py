import random


welcome_massage = "CUYPAY GAMES"
cuypy_position = random.randint(1,4)

print ("* "*10 + welcome_massage + " *"*10)

nama_user = input("masukan nama anda : ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4

goa = goa_kosong.copy()
goa [cuypy_position - 1]= "|0_0|"

goa_kosong = ' '.join(goa_kosong)
goa = ' '.join(goa)
print (f'''
Halo {nama_user}! Coba Perhatikan goa di bawah ini
{goa_kosong}
''')

pilihan_user = int(input("Menurut kamu dimana CUYPY berada [1/2/3/4] : "))
confirm_answer = input(f"Apakah kamu yakin jawabannya adalah {pilihan_user}? [y/n] : ")

if confirm_answer == "n":
    print ("Program dihentikan")
    exit()
elif confirm_answer == "y":
    if pilihan_user == cuypy_position:
        print (f"{goa} \n Selamat Kamu Menang 🏆")
    else:
        print (f"{goa} \n Maaf Kamu Kalah 🤪")
else : 
    print ("Program di hentikan, karena inputan anda salah")
    exit() 