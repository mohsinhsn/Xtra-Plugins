# Copyright (C) 2020-2021 by MohsinHsn@Github, < https://github.com/MohsinHsn >.
#
# This file is part of < https://github.com/MohsinHsn/StylishUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MohsinHsn/blob/master/LICENSE >
#
# All rights reserved.

from main_startup.core.decorators import stylish_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text


@stylish_on_cmd(
    ["spam", "ultraspam"],
    is_official=False,
    cmd_help={
        "help": "Spam Message Multiple Times!",
        "example": "{ch}spam (number of times to spam) (reply to message)",
    },
)
async def spam(client, message):
    pablo = await edit_or_reply(message, "Processing....")
    count = get_text(message)
    if not count:
        await pablo.edit("`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`")
        return
    if not count.isnumeric():
        await pablo.edit("`Give Digits Idiot!`")
        return
    if not message.reply_to_message:
        await pablo.edit("`Reply To Message, Idiot!`")
        return
    count = int(count)
    x = 0
    for x in range(count):
        await client.copy_message(
            from_chat_id=message.chat.id,
            chat_id=message.chat.id,
            message_id=message.reply_to_message.message_id,
        )
        x += 1
