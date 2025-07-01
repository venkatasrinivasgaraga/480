#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "<blockquote>Hello, \n\nThis is a Telegram <b>Video Encoder Bot</b>. \n\n<b>Please send me any Telegram big video file I will compress it as s small video file!</b> \n\n/help for more details.</blockquote>"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "<blockquote>Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail.</blockquote>"
    
    
    DOWNLOAD_START = "<blockquote> ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ...</blockquote>\n"
    
    UPLOAD_START = "<blockquote> ᴜᴘʟᴏᴀᴅɪɴɢ ...</blockquote>\n"
    
    COMPRESS_START = "<blockquote> ᴛʀʏɪɴɢ ᴛᴏ ᴇɴᴄᴏᴅᴇ ...</blockquote>"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "<blockquote><b>ENCODED BY HUNTERS</b></blockquote>"

    COMPRESS_PROGRESS = "<blockquote>🕛 ETA: {} ♻️ Progress: {}%</blockquote>"

    SAVED_CUSTOM_THUMB_NAIL = "<blockquote>Custom video / file thumbnail saved. This image will be used in the video / file.</blockquote>"
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = "HUNTERS"
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "<blockquote>Hi, I am Video Compressor Bot \n\n1. Send me your telegram big video file \n2. Reply to the file with: `/compress` </blockquote>"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
