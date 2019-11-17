import os
from datetime import datetime
from pytz import timezone
from PIL import Image, ImageDraw, ImageFont, ImageFile
from pySmartDL import SmartDL
from telethon.tl import functions
from uniborg.util import admin_cmd
import asyncio
import shutil

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
VERY_PIC = "http://lorempixel.com/500/500/" 

@borg.on(admin_cmd(pattern="autopp"))
async def autopic(event):
    downloaded_file_name = "./DOWNLOADS/original_pic.png"
    photo = "photo.png" 
    while True:
        downloaded_file_name = "./DOWNLOADS/original_pic.png"
        downloader = SmartDL(VERY_PIC, downloaded_file_name, progress_bar=False)
        downloader.start(blocking=False)
        while not downloader.isFinished():
           place_holder = None
        counter = -30
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        file_test = im.save(photo, "PNG")
        now_utc = datetime.now(timezone('UTC'))
        now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
        x = 350
        y = 15
        x2 = 250
        y2 = 430
        white = (255, 255, 255) 
        black = (0, 0, 0)
        cn_time = now_asia.strftime("%d %b %Y\n@user_nmr")
        ct_time = now_asia.strftime("%I:%M %p")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 20)
        fnt2 = ImageFont.truetype(FONT_FILE_TO_USE, 40)
        #top_part
        #outline 
        drawn_text.text((x+2,y), cn_time, font=fnt, fill=white)
        drawn_text.text((x-2,y), cn_time, font=fnt, fill=white)
        drawn_text.text((x,y+2), cn_time, font=fnt, fill=white)
        drawn_text.text((x,y-2), cn_time, font=fnt, fill=white)
        #main
        drawn_text.text((x,y), cn_time, font=fnt, fill=(0, 102, 204))
        #bottom
        #outline
        drawn_text.text((x2+1,y2), ct_time, font=fnt2, fill=black)
        drawn_text.text((x2-1,y2), ct_time, font=fnt2, fill=black)
        drawn_text.text((x2,y2+1), ct_time, font=fnt2, fill=black)
        drawn_text.text((x2,y2-1), ct_time, font=fnt2, fill=black)
        #main        
        drawn_text.text((x2,y2), ct_time, font=fnt2, fill=(255, 0, 0))
        #draw_complete
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(downloaded_file_name)
            counter -= 30
            await asyncio.sleep(65)
        except:
            return
