class script(object):
    START_TXT = """ð·ð´ð»ð»ð¾ {},
ð¼ð ð½ð°ð¼ð´ ð¸ð <a href=https://t.me/{}>{}</a>, ð¸ ð°ð¼ ð±ð¾ðð½ ðð¾ ð¿ðð¾ðð¸ð³ð´ ð¼ð¾ðð¸ð´ð, ð¹ððð ð°ð³ð³ ð¼ð´ ðð¾ ðð¾ðð ð¶ðð¾ðð¿ ð°ð½ð³ ð´ð½ð¹ð¾ð ð.."""
    HELP_TXT = """ð·ð´ð {}
ð·ð´ðð´ ð¸ð ð¼ð ð·ð´ð»ð¿ ð²ð¾ð¼ð¼ð°ð½ð³ð."""
    ABOUT_TXT = """<b>ðð¾ð¼ð´ðð·ð¸ð½ð¶ ð°ð±ð¾ðð ð¼ð´</b>
    
ââââââââââ° êªá¥êª®êªð½ êªð´á§ â±âââ±âÛªÛª
ââ­ââââââââââââââââ£</b>
ââ£âª¼ â¯ <b>ð¼ð ð½ð°ð¼ð´: {}</b>
ââ£âª¼ â¯ <b>ð²ðð´ð°ðð¾ð: <a href=https://t.me/Illaya_Tholan>ME ð</a></b>
ââ£âª¼ â¯ <b>ð»ð¸ð±ðð°ðð: ð¿ððð¾ð¶ðð°ð¼</a></b>
ââ£âª¼ â¯ <b>ð»ð°ð½ð¶ðð°ð¶ð´: ð¿ððð·ð¾ð½ ð¹</a></b>
ââ£âª¼ â¯ <b>ð³ð°ðð° ð±ð°ðð´: ð¼ð¾ð½ð¶ð¾-ð³ð±</a></b>
ââ£âª¼ â¯ <b>ð±ð¾ð ðð´ððð´ð: ð·ð´ðð¾ðºð</a></b>
ââ£âª¼ â¯ <b>ðð¾ððð²ð´: ð <a href=https://t.me/isaimini_updates>ð²ð»ð¸ð²ðº ð·ð´ðð´</a></b>
ââ£âª¼ â¯ <b>ð±ðð¸ð»ð³ ððð°ððð: ð1.0.43</b>
ââ£âª¼ â¯ <b>ðð¿ð³ð°ðð´ð: <a href=https://t.me/isaimini_updates>ðð¬ðð¢ð¦ð¢ð§ð¢ ðð©ððð­ðð¬</a></b>
ââ°âââââââã<a href=https://t.me/+2YaY1CQKOfg3MzQ9>ð ð¼ðð¶ð²ð ðð¹ðð¯</a>ã</b>
"""
    SOURCE_TXT = """<b>DISCLAIMER NOTEâ¼ï¸:</b>
- ððð®ð¶ðºð¶ð»ð¶ ð£ð¿ð¶ðºð² ð»  ðð ðð ð¾ððð ðððððð ð¿ðððððð. All the files in this bot are freely available on the internet or posted by somebody else. This bot is indexing files which are already uploaded on Telegram for easy of searching, We respect all the copyright laws and works in compliance with DMCA and EUCD. If anything is against law please contact us so that it can be removed asap. It is forbidden to download, stream, reproduce, or by any means, share, or consume, content without explicit permission from the content creator or legal copyright holder. If you believe this bot is violating your intellectual property, contact the respective channels for removal. The Bot does not own any of these contents, it only index the files from telegram.. 
- Source - <a href=https://t.me/isaimini_updates>ððð®ð¶ðºð¶ð»ð¶ ð£ð¿ð¶ðºð²</a>  

<b>DEVS:</b>
- <a href=https://t.me/isaimini_updates>ðð¬ðð¢ð¦ð¢ð§ð¢ ðð©ððð­ðð¬</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and à´®à´¿à´¨àµà´¨àµ½ à´®àµà´°à´³à´¿ (à´à´±à´¿à´à´¿à´¨àµ½) will respond whenever a keyword is found the message

<b>NOTE:</b>
1. ððð®ð¶ðºð¶ð»ð¶ ð£ð¿ð¶ðºð² ð» should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¢ /filter - <code>add a filter in chat</code>
â¢ /filters - <code>list all the filters of a chat</code>
â¢ /del - <code>delete a specific filter in chat</code>
â¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- ððð®ð¶ðºð¶ð»ð¶ ð£ð¿ð¶ðºð² ð» Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ððð®ð¶ðºð¶ð»ð¶ ð£ð¿ð¶ðºð² ð» supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/isaimini_updates)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¢ /connect  - <code>connect a particular chat to your PM</code>
â¢ /disconnect  - <code>disconnect from a chat</code>
â¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of ððð®ð¶ðºð¶ð»ð¶ ð£ð¿ð¶ðºð² ð»

<b>Commands and Usage:</b>
â¢ /id - <code>get id of a specified user.</code>
â¢ /info  - <code>get information about a user.</code>
â¢ /imdb  - <code>get the film information from IMDb source.</code>
â¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins ð¤¯

<b>Commands and Usage:</b>
â¢ /logs - <code>to get the rescent errors</code>
â¢ /stats - <code>to get status of files in db.</code>
â¢ /delete - <code>to delete a specific file from db.</code>
â¢ /users - <code>to get list of my users and ids.</code>
â¢ /chats - <code>to get list of the my chats and ids </code>
â¢ /leave  - <code>to leave from a chat.</code>
â¢ /disable  -  <code>do disable a chat.</code>
â¢ /ban  - <code>to ban a user.</code>
â¢ /unban  - <code>to unban a user.</code>
â¢ /channel - <code>to get list of total connected channels</code>
â¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>áâºâ® ðð¾ðð°ð» ðµð¸ð»ð´ð: <code>{}</code></b>
<b>áâºâ® ðð¾ðð°ð» ððð´ðð: <code>{}</code></b>
<b>áâºâ® ðð¾ðð°ð» ð²ð·ð°ðð: <code>{}</code></b>
<b>áâºâ® ððð´ð³ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ð±</b>
<b>áâºâ® ðµðð´ð´ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ð±</b>"""
    LOG_TEXT_G = """#ððð°ðð«ð¨ð®ð© (Url Evamaria)
    
<b>áâº ðð«ð¨ð®ð© âª¼  {}(<code>{}</code>)</b>
<b>áâº ðð¨ð­ðð¥ ððð¦ððð«ð¬ âª¼ <code>{}</code></b>
<b>áâº ððððð ðð² âª¼  {}</b>
"""
    LOG_TEXT_P = """#ððð°ðð¬ðð« (Url Evamaria)
    
<b>áâº ðð - <code>{}</code></b>
<b>áâº ððð¦ð - {}</b>
"""
