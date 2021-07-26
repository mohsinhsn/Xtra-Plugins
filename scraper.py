import pyrogram 
from pyrogram import functions

@stylish.on(stylish_on_cmd(pattern="scrap ?(.*)"))
async def sed(event):
    if event.is_private:
        await event.edit("`This Plugin Only Works In Groups Channel`")
        return
    sed = event.pattern_match.group(1)
    if str(sed).startswith("-100"):
        kk = int(sed)
    else:
        kk = int(sed) if sed.isdigit() else str(sed) 
    user_s = 0
    tries = 0
    await event.edit("**Fetching Users !**")
    async for user in event.client.iter_participants(kk):
        await event.edit(f"**USER FIRST-NAME : ** `{user.first_name}` **USER ID :** `{user.id}`") 
        try:
            await stylish(
                functions.channels.InviteToChannelRequest(channel=event.chat_id, users=[user.id])
            )
            tries += 1
        except:
            user_s += 1 
    await event.edit(f"**Added {tries - user_s} To This Group, Failed To Add {user_s} Users**")
