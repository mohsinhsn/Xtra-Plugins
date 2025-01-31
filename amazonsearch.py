# Copyright (C) 2020-2021 by MohsinHsn@Github, < https://github.com/MohsinHsn >.
#
# This file is part of < https://github.com/MohsinHsn/StylishUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MohsinHsn/blob/master/LICENSE >
#
# All rights reserved.

import requests
from main_startup.core.decorators import stylish_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text


@stylish_on_cmd(
    ["amsearch"],
    cmd_help={
        "help": "Search Products From Amazon!",
        "example": "{ch}amsearch Iphone",
    }
)

async def _am_search_by_lackhac(client,message):
    query = get_text(message)
    msg_ = await edit_or_reply(message, "`Searching Product!`")
    if not query:
        await msg_.edit("`Please, Give Input!`")
        return
    product = ""
    r = requests.get(f"https://amznsearch.vercel.app/api/?query={query}").json()
    for products in r:
        link = products['productLink']
        name = products['productName']
        price= products['productPrice']
        product += f"<a href='{link}'>• {name}\n{price}</a>\n"
    await msg_.edit(product, parse_mode="HTML")
