from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant

from musikku.helpers.decorators import authorized_users_only, errors
from musikku.services.callsmusic.callsmusic import client as USER


@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Tambahkan saya sebagai admin grup Anda terlebih dahulu</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "MY-VCG"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "Dahlah di culik lagi gue")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Cuma jadi kang bacot</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f" ⛔ Permintaan bnjur ⛔\nPengguna {user.first_name} tidak dapat bergabung dengan grup Anda karena banyak permintaan bergabung untuk userbot! Pastikan pengguna tidak diblokir di grup."
            "\n\nAtau tambahkan BOT Asisten secara manual ke Grup Anda dan coba lagi</b>" ,
         )
        return
    await message.reply_text(
        "<b>bantu userbot bergabung dengan obrolan Anda</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
          f"<b>Pengguna tidak dapat meninggalkan grup Anda! Mungkin menunggu lama." 
           "\n\nAtau cara manual menendang saya dari Grup Anda</b>",
        )
        return

@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is chat even linked")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Jadiin admin dulu bangke</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "MY-VCG"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "Di culik lagi gue")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Gue dah siap bangst</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"⛔ Permintaan banjir ⛔\nPengguna {user.first_name} tidak dapat bergabung dengan grup Anda karena banyak permintaan bergabung untuk userbot! Pastikan pengguna tidak diblokir di grup."
            "\n\nAtau tambahkan BOT Asisten secara manual ke Grup Anda dan coba lagi</b>" ,
         )
    return
    await message.reply_text(
        "<b>Gue dah gabung cuk</b>",
    )
    
