# For @UniBorg

# (c) Shrimadhav U K

"""Auto Profile Updation Commands

.autopp"""

import asyncio

from datetime import datetime

from pytz import timezone

from telethon.tl import functions

from telethon.errors import FloodWaitError

from uniborg.util import admin_cmd

DEL_TIME_OUT = 70

@borg.on(admin_cmd(pattern="autoname"))  # pylint:disable=E0602

async def _(event):

    if event.fwd_from:

        return

    while True:


        now_utc = datetime.now(timezone('UTC'))

        now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))

        name = now_asia.strftime("NMR 💥 %T:%M:%p 💥 ")

       

        logger.info(name)

        try:

            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602

                first_name=name

            ))

        except FloodWaitError as ex:

            logger.warning(str(e))

            await asyncio.sleep(ex.seconds)

        # else:

            # logger.info(r.stringify())

            # await borg.send_message(  # pylint:disable=E0602

            #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602

            #     "Changed Profile Picture"

            # )

        await asyncio.sleep(DEL_TIME_OUT)
