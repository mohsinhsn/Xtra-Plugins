# Copyright (C) 2020-2021 by MohsinHsn@Github, < https://github.com/MohsinHsn >.
#
# This file is part of < https://github.com/MohsinHsn/StylishUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MohsinHsn/blob/master/LICENSE >
#
# All rights reserved.

import io
import os
from tswift import Song

from main_startup.config_var import Config
from main_startup.core.decorators import stylish_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text, edit_or_send_as_file



@stylish_on_cmd(
    ["lyrics"],
    cmd_help={
        "help": "This plugin searches for song lyrics with song name",
        "example": "{ch}lyrics alone",
    }
)
async def _(client,message):
    query = get_text(message)
    lel = await edit_or_reply(message, "`Searching For Lyrics.....`")
    if not query:
        await lel.edit("`Give Me Input!`")
        return
    song = None
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "`Lyrics Not Found! Please Work On Your English!`"
    else:
        reply = "`Lyrics Not Found! Please Work On Your English!`"
    await edit_or_send_as_file(reply, lel, client, f"Result For {query}", query)
