#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hai {}, \n\n<code>Iam a simple telegram video compresser bot.send me any telegram file or media.I will compress it</code>\n\n<code>For More Details Press</code> /help.\n\nπ² α΄α΄ΙͺΙ΄α΄α΄ΙͺΙ΄α΄α΄ ΚΚ : @BX_Botz"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "π₯ Downloading ... π₯l \n"
    
    UPLOAD_START = "π€ Uploading ...  \n"
    
    COMPRESS_START = "π Trying to compress ... π"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "π₯ Downloaded in {}\n\nπ Compressed in {}\n\nπ€ Uploaded in {}\n\nβοΈ πΌπππππππππ  π±π’ @BX_Botz"

    COMPRESS_PROGRESS = "β³ ETA: {}\nπ Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "β Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "β Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "β Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "β οΈ Already one Process going on! β οΈ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "β  Send Me Any Media Or File\n\nβ  Reply To Telegram Media /Compress"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
