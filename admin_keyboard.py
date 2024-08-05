from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton


answered = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("پاسخ داده شده", callback_data="HALLO")],
        ]
)

home = ReplyKeyboardMarkup(
            [
                ["پیام همگانی🗣", "اضافه کردن ادمین جدید🧑🏻‍💻👩🏻‍💻"],
                ["مدیریت یوزرها✏️"],
                ["گزارشات📝🗂", "افزایش موجودی کاربر💰"],
                ["📝اضافه کردن تاپیک جدید📝"],
                ["✏️اضافه کردن ایتم جدید✏️"],
                ["حذف تاپیک", "حذف ایتم"]
                ],resize_keyboard=True
                ,one_time_keyboard=True
                )

admin_set = ReplyKeyboardMarkup(
    [
        ["اضافه کردن ادمین جدید✅", "حذف کردن ادمین موجود❌"],
        ["بازگشت به منوی اصلی♻️"]
    ],resize_keyboard=True
    ,one_time_keyboard=True
)  

ban_unban = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("بن کردن کاربر🚫", callback_data="ban")],
            [InlineKeyboardButton("انبن کردن کاربر✅", callback_data="unban")],
        ]
)

admin_return = ReplyKeyboardMarkup(
    [
        ["بازگشت به منوی اصلی♻️"]
    ],resize_keyboard=True,
    one_time_keyboard=True
)










