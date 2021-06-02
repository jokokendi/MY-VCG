from pyrogram import filters
from pyrogram.types import Message

from musikku.services.callsmusic.callsmusic import client as USER


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        "Halo, Ini adalah layanan asisten musik .\n\n❗️ Aturan:\n - Chatting tidak diizinkan\n  - Spam tidak diizinkan\n\n👉 **KIRIM LINK UNDANGAN GRUP ATAU NAMA PENGGUNA JIKA USERBOT TIDAK BISA BERGABUNG GROUP.**\n\n⚠️ Penafian: Jika Anda mengirim pesan di sini, artinya admin akan melihat pesan Anda dan bergabung dengan obrolan\n - Jangan tambahkan pengguna ini ke grup rahasia.\n - Jangan Bagikan info pribadi disini\n\n",
   )
    return
