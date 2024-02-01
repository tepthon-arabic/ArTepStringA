from pyrogram import filters
from pyrogram.types import Message

from ArStringTep import Anony
from ArStringTep.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"✦ **مرحبًــا  👋** {message.from_user.first_name},\n\n  {Anony.mention},\n**✦ يمكنـك استخـدامي لـ استخـراج كـود الجلسـة لـ تنصيـب  تيبثـون اضغط بدء استخراج الجلسة وابدأ بالاستخراج ✨ .**",
        reply_markup=keyboarأ
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
