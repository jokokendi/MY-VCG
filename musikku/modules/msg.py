import os
from musikku.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 Saya bot musik yang dibuat untuk memutar musik di obrolan suara Grup & Channel Telegram.\n\n✅ Ketik /help bila butuh bantuan."
      HELP_MSG = [
        ".",
f"""
**Hei 👋 Selamat datang di {PROJECT_NAME}

⚡ {PROJECT_NAME} dapat memutar musik di obrolan suara Grup dan obrolan suara Channel Anda

⚡ Nama Assistant Bot >> @{ASSISTANT_NAME}\n\nKlik tombol dibawah untuk melihat Panduan menggunakan bot**
""",

f"""
📌 ** Panduan Menggunakan Bot di Group**

1) Tambahkan bot ini ke Grup Anda
2) Jadikan bot ini dan bot @{ASSISTANT_NAME} sebagai admin dan berikan semua akses , kecuali jangan di anonim
2) Hidupkan Obrolan Suara atau Voice Chat Group
3) Lalu coba /play [song name] untuk memastikan bot berjalan
*) Jika berhasil berarti udah bisa digunakan, kalo error coba add @{ASSISTANT_NAME} ke Group lalu ulangi cara diatas.

**Daftar Perintah Menggunakan Bot di Group**

⎋ **Berikut beberapa opsi pilihan untuk /play lagu 🎧**

- /play <judul lagu> : memutar lagu dengan mengetikan judul lagu
- /play <yt link> : memutar lagu melalui link yt
- /play <reply ke vn> : memutar dari vn dgn cara reply vn tersebut
- /dplay <judul lagu> : memutar lagu via deezer
- /splay <judul lagu> : memutar lagu jio saavn

⎋ **Daftar Perintah lain**

- /player : membuka panel pengaturan Musik Player
- /skip : putar lagu berikutnya
- /pause : jeda pemutaran lagu
- /resume : melanjutkan pemutaran lagu
- /end : menghentikan pemutaran musik
- /current : melihat lagu yang sedang diputar
- /playlist : melihat daftar playlist

""",
        
f"""
⎋ ** Daftar Perintah Lain**

- /song <judul lagu> : mendownload lagu dengan cepat
- /video <judul video> : mendownload video dengan cepat
- /reload : memperbaharui daftar admin
- /userbotjoin :  menambahkan @{ASSISTANT_NAME} ke Group Anda

""",

f"""
📌 **Panduan Menggunakan Bot di Channel**

1) Jadikan Bot ini sebagai Admin di Channel dan Group Anda
2) Ketik /userbotjoinchannel pada Group yang ditautkan ke Channel
3) Lalu coba ketik satu Perintah di bawah pada Group yang ditaukat ke Channel
#️⃣ Note : Channel wajib ditautkan pada suatu group

**Daftar Perintah Menggunakan Bot di Channel**

- /cplay <judul lagu> : memutar lagu dengan mengetikan judul lagu
- /cdplay <judul lagu> : memutar lagu via deezer
- /csplay <judul lagu> : memutar lagu jio saavn
- /cplaylist - melihat daftar playlist
- /cccurrent - melihat lagu yang sedang diputar
- /cplayer - membuka panel pengaturan Musik Player
- /cpause - jeda pemutaran lagu
- /cresume - melanjutkan pemutaran lagu
- /cskip - putar lagu berikutnya
- /cend - menghentikan pemutaran musik
- /userbotjoinchannel - menambahkan Assistant ke Channel Anda

"""
      ]
