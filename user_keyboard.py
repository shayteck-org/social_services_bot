from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton


home_keyboard = ReplyKeyboardMarkup(
    [
        ["➕ افزایش موجودی", "💰 شارژ رایگـان"],
        ["🛍 محصولات فضـای مجازی 🛍"],
        ["💡 حساب کاربری"],
        ["📮 پـشتیبانـی"],
        ["🙋🏻‍♂️ درخواست مشاوره", "🎖 درخواست نمایندگـی 🎖"]
    ],resize_keyboard=True
    ,one_time_keyboard=True
)

sm_keyboard = ReplyKeyboardMarkup(
    [
        ["تلـگرام 💎", "اینسـتاگرام 🛒"],
        ["⭐️ خدمـات ویـژه ⭐️"],
        ["خدمات پر فروش"],
        ["بازگشت به منوی اصلی♻️"]
    ],resize_keyboard=True
    ,one_time_keyboard=True
)

increase_balance = InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("✅ پرداخت آنلاین", callback_data="IncreaseGateway")],
        [InlineKeyboardButton("کارت بـه کارت 💳", callback_data="IncreaseCC"), InlineKeyboardButton("🪙 ارز دیـجیتال", callback_data="IncreaseCrypto")],
        [InlineKeyboardButton("بازگشت به منوی اصلی♻️", callback_data="BackToMainMenu")]
    ]
)

support = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("پشتیبان مالی", callback_data="sup"), InlineKeyboardButton("پشتیبان سفارشات", callback_data="sup")],
        [InlineKeyboardButton("پشتیبان فنی", callback_data="sup"), InlineKeyboardButton("سایر موارد", callback_data="sup")],
        [InlineKeyboardButton("ارتباط با مدیریت", callback_data="sup")]
    ]
)

join_channel = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("ورود به کانال", url="https://t.me/AcademyRoyale")],
        [InlineKeyboardButton("عضو شدم", callback_data="check")]
    ]
)

user_info = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("➕ افزایش موجودی", callback_data="increase_balance")],
        [InlineKeyboardButton("🔐 احراز هویت کارت", callback_data="register")]
    ]
)

first_time = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("دریافت هدیه", callback_data="prize")]
    ]
)

put_order = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("ثبت سفارش تکی", callback_data="one_order")],
        [InlineKeyboardButton("ثبت سفارش به تعداد ماکسیموم", callback_data="full_order")]
    ]
)

charge_amount = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("۲۰۰۰۰ تومان", callback_data="20"), InlineKeyboardButton("۵۰۰۰۰ تومان", callback_data="50")],
        [InlineKeyboardButton("۱۰۰۰۰۰ تومان", callback_data="100"), InlineKeyboardButton("۲۰۰۰۰۰ تومان", callback_data="200")],
        [InlineKeyboardButton("۵۰۰۰۰۰ تومان", callback_data="500"), InlineKeyboardButton("۱۰۰۰۰۰۰ تومان", callback_data="1000")],
        [InlineKeyboardButton("🏦شارژ مبلغ دلخواه🏦", callback_data="wish_amount")]
    ]
)

