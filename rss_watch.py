# Copyright (C) 2020-2021 by MohsinHsn@Github, < https://github.com/MohsinHsn >.
#
# This file is part of < https://github.com/MohsinHsn/StylishUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MohsinHsn/blob/master/LICENSE >
#
# All rights reserved.

from main_startup.core.decorators import stylish_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text
import feedparser
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from main_startup import Stylish
from xtraplugins.dB.rss_db import (
    add_rss,
    is_get_chat_rss,
    del_rss,
    get_chat_rss,
    update_rss,
    basic_check,
    get_all,
    overall_check,
    delete_all
)





@stylish_on_cmd(
    ["add_rss"],
    is_official=False,
    cmd_help={
        "help": "Add RSS To The Chat",
        "example": "{ch}add_rss (rss link)",
    },
)
async def addrss(client, message):
    pablo = await edit_or_reply(message, "`Processing....`")
    lenk = get_text(message)
    if not lenk:
        await pablo.edit("`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`")
        return
    try:
        rss_d = feedparser.parse(lenk)
        rss_d.entries[0].title
    except:
        await pablo.edit("ERROR: The link does not seem to be a RSS feed or is not supported")
        return
    lol = await is_get_chat_rss(message.chat.id, lenk)
    if lol:
        await pablo.edit("This Link Already Added")
        return
    content = ""
    content += f"**{rss_d.entries[0].title}**"
    content += f"\n\n{rss_d.entries[0].link}"
    try:
        content += f"\n{rss_d.entries[0].description}"
    except:
        pass
    await client.send_message(message.chat.id, content)
    await add_rss(message.chat.id, lenk, rss_d.entries[0].link)
    await pablo.edit("Successfully Added Link To RSS Watch")

@stylish_on_cmd(
    ["test_rss"],
    is_official=False,
    cmd_help={
        "help": "Test RSS Of The Chat",
        "example": "{ch}test_rss",
    },
)
async def testrss(client, message):
    pablo = await edit_or_reply(message, "`Processing....`")
    damn = await basic_check(message.chat.id)
    if not damn:
        URL = "https://www.reddit.com/r/funny/new/.rss"
        rss_d = feedparser.parse(URL)
        Content = (rss_d.entries[0]['title'] + "\n\n" + rss_d.entries[0]['link'])
        await client.send_message(message.chat.id, Content)
        await pablo.edit("This Chat Has No RSS So Sent Reddit RSS")
    else:
        all = await get_chat_rss(message.chat.id)
        for x in all:
            link = x.get("rss_link")
            rss_d = feedparser.parse(link)
            content = ""
            content += f"**{rss_d.entries[0].title}**"
            content += f"\n\nLink : {rss_d.entries[0].link}"
            try:
                content += f"\n{rss_d.entries[0].description}"
            except:
                pass
            await client.send_message(message.chat.id, content)
        await pablo.delete()

@stylish_on_cmd(
    ["list_rss"],
    is_official=False,
    cmd_help={
        "help": "List all RSS Of The Chat",
        "example": "{ch}list_rss",
    },
)
async def listrss(client, message):
    pablo = await edit_or_reply(message, "`Processing....`")
    damn = await basic_check(message.chat.id)
    if not damn:
        await pablo.edit("This Chat Has No RSS!")
        return
    links = ""
    all = await get_chat_rss(message.chat.id)
    for x in all:
        l = x.get("rss_link")
        links += f"{l}\n"
    content = f"Rss Found In The Chat Are : \n\n{links}"
    await client.send_message(message.chat.id, content)
    await pablo.delete()



@stylish_on_cmd(
    ["del_rss"],
    is_official=False,
    cmd_help={
        "help": "Delete RSS From The Chat",
        "example": "{ch}del_rss (rss link)",
    },
)
async def delrss(client, message):
    pablo = await edit_or_reply(message, "`Processing....`")
    lenk = get_text(message)
    if not lenk:
        await pablo.edit("`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`")
        return
    lol = await is_get_chat_rss(message.chat.id, lenk)
    if not lol:
        await pablo.edit("This Link Was Never Added")
        return
    await del_rss(message.chat.id, lenk)
    await pablo.edit(f"Successfully Removed `{lenk}` From Chat RSS")

@stylish_on_cmd(
    ["del_all_rss", "rm_all_rss"],
    is_official=False,
    cmd_help={
        "help": "Deletes All RSS From The Chat",
        "example": "{ch}del_all_rss",
    },
)
async def delrss(client, message):
    pablo = await edit_or_reply(message, "`Processing....`")
    if not await basic_check(message.chat.id):
        await pablo.edit("This Chat Has No RSS To Delete")
        return
    await delete_all()
    await pablo.edit("Successfully Deleted All RSS From The Chat")

async def check_rss():
    if not await overall_check():
        return
    all = await get_all()
    for one in all:
        link = one.get("rss_link")
        old = one.get("latest_rss")
        rss_d = feedparser.parse(link)
        if rss_d.entries[0].link != old:
             message = one.get("chat_id")
             content = ""
             content += f"**{rss_d.entries[0].title}**"
             content += f"\n\nLink : {rss_d.entries[0].link}"
             try:
                content += f"\n{rss_d.entries[0].description}"
             except:
                pass
             await update_rss(message, link, rss_d.entries[0].link)
             await Stylish.send_message(message, content)
             


scheduler = AsyncIOScheduler()
scheduler.add_job(check_rss, 'interval', minutes=10)
scheduler.start()
