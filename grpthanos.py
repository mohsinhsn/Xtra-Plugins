from main_startup.core.decorators import stylish_on_cmd, Config, listen
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text
from pyrogram import filters


@listen(stylish_on_cmd(pattern="(banall|snap)$"))
async def sed(event):
    if event.is_private:
        await event.edit("`This Plugin Only Works In Groups Channel`")
        return
    user_s = 0
    tries = 0
    hmm = await bot.get_me()
    if not await is_admin(event, hmm.id):
        await event.edit("`You Should Be Admin To Do This !`")
        return
    async for user in event.client.iter_participants(int(event.chat_id)):
        await event.edit(f"**Banning** \n**USER FIRST-NAME : ** `{user.first_name}` \n**USER ID :** `{user.id}`") 
        try:
            await event.client.edit_permissions(event.chat_id, user.id, view_messages=True)
            tries += 1
        except:
            user_s += 1 
    await event.edit(f"**Banned {user_s - tries} Users From This Group, Failed To Ban {user_s} Users**")

@listen(stylish_on_cmd(pattern="kickall$"))
async def rip(event):
    if event.is_private:
        await event.edit("`This Plugin Only Works In Groups Channel`")
        return
    user_s = 0
    tries = 0
    hmm = await bot.get_me()
    if not await is_admin(event, hmm.id):
        await event.edit("`You Should Be Admin To Do This !`")
        return
    async for user in event.client.iter_participants(int(event.chat_id)):
        if user.id != hmm.id:
            await event.edit(f"**Kicking** \n**USER FIRST-NAME : ** `{user.first_name}` \n**USER ID :** `{user.id}`") 
       	    try:
                await event.client.kick_participant(event.chat_id, user.id)
                tries += 1
            except:
                user_s += 1 
    await event.edit(f"**Kicked {user_s - tries} Users From This Group, Failed To Kick {user_s} Users**")
