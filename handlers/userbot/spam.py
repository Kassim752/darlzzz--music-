# 𝐃𝐎𝐍𝐓 𝐌𝐄𝐒𝐒 𝐖𝐈𝐓𝐇 𝐂𝐎𝐃𝐄𝐒 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 @SHAILENDRA34
# 𝐃𝐎𝐍𝐓 𝐌𝐄𝐒𝐒 𝐖𝐈𝐓𝐇 𝐂𝐎𝐃𝐄𝐒 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 @SHAILENDRA34
# 𝐃𝐞𝐚𝐫 𝐏𝐞𝐫𝐨 𝐩𝐩𝐥𝐬 𝐏𝐥𝐢𝐬𝐡 𝐃𝐨𝐧'𝐭 𝐫𝐞𝐦𝐨𝐯𝐞 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐞 𝐟𝐫𝐨𝐦 𝐡𝐞𝐫𝐞 🌚


from pyrogram.types import Message
import asyncio
import time
from pyrogram import filters, Client
from config import SUDO_USERS as SUDO_USER


@Client.on_message(filters.user(SUDO_USER) & filters.command(["delspam", "deletespam"], [".", "!", "/"]))
async def delspam(client: Client, message: Message):
    hero = await message.reply_text("⚡ Usage:\n .delspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    await message.delete()
    for i in range(quantity):
        await hero.delete()
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.1)
        await msg.delete()
        await asyncio.sleep(0.1)


@Client.on_message(filters.user(SUDO_USER) & filters.command(["spam", "spamming"], [".", "!", "/"]))
async def suspam(client: Client, message: Message):
    hero = await message.reply_text("⚡ Usage:\n .spam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await hero.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.15)


@Client.on_message(filters.user(SUDO_USER) & filters.command(["fastspam", "fspam"], [".", "!", "/"]))
async def spspam(client: Client, message: Message):
    hero = await message.reply_text("⚡ Usage:\n .fastspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.002)
        return
    
    for _ in range(quantity):
        await hero.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.002)



@Client.on_message(filters.user(SUDO_USER) & filters.command(["slowspam", "dspam", "delayspam"], [".", "!", "/"]))
async def sperm(client: Client, message: Message):
    hero = await message.reply_text("⚡ Usage:\n .slowspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.9)
        return

    for _ in range(quantity):
        await hero.delete()
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.9)







@Client.on_message(filters.user(SUDO_USER) & filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], [".", "!", "/"]))
async def pussy(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("**reply to a sticker with amount you want to spam**")
        return
    if not message.reply_to_message.sticker:
        await message.edit_text(text="**reply to a sticker with amount you want to spam**")
        return
    else:
        i=0
        times = message.command[1]
        if message.chat.type in ["supergroup", "group"]:
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if umm.chat.type == "private":
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id, sticker
                )
                await asyncio.sleep(0.10)



@Client.on_message(filters.command('join', [".", "!", "/"]) & filters.user(SUDO_USER))
async def fuck(client: Client, message: Message):
    hero = message.text[6:]
    count = 0
    if not hero:
        return await message.reply_text("Need a chat username or invite link to join.")
    if hero.isnumeric():
        return await message.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        await client.join_chat(hero)
        await message.reply_text(f"**Joined ✅**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command('leave', [".", "!", "/"]) & filters.user(SUDO_USER))
async def leftfuck(client: Client, message: Message):
    hero = message.text[6:]
    count = 0
    if not hero:
        return await message.reply_text("Need a chat username or invite link to leave.")
    if hero.isnumeric():
        return await message.reply_text("Can't leave a chat with chat id. Give username or invite link.")
    try:
        await client.leave_chat(hero)
        await message.reply_text(f"**Left ❌**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")
