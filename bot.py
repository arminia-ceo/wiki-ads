#Console
print('=================================Console Log===================================')
print('Now Importing...')

#Imports
import bale
from bale import Update, Message, Bot, User, Chat
import logging
import os, re
import time
import random

print('Importing Finished!')
print()
#Proxy
print('Start Proxy...')
print('Being Ready...')

#Token
tokenbot = str(open("env.txt", "r").read())
bot = bale.Bot(token = tokenbot)

#Ready
@bot.listen('on_ready')
async def on_ready():
        print(bot.user.first_name, "is Ready!")
        print()
        print()
        print('===================================Massage=====================================')
        
#Update
@bot.event
async def on_update(update: Update):
        print("Update Id:", update.update_id)

#User Defs
import json
filename = "data.json"

#Load Data
def load_data():
        try:
                with open(filename, "r", encoding = "utf-8") as f:
                        return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
                return {}

#Save Data
def save_data(data):
        with open(filename, "w", encoding = "utf-8") as f:
                json.dump(data, f, ensure_ascii = False, indent = 4)

#Update Data
def set_user_data(user_id, info):
        data = load_data()
        if user_id in data :
                return 'Exist'
        else :
                data[user_id] = info
                save_data(data)
                return 'No Exist'

#Get Data
def get_user_data(user_id):
        data = load_data()
        return data.get(user_id, None)

#Change Main
def update_user_score(user_id):
        data = load_data()
        if user_id in data and data[user_id]["used"] == "No" :
                data[user_id]["used"] = "Yes"
                save_data(data)
                return "To Yes"
        elif user_id in data and data[user_id]["used"] == "Yes" :
                data[user_id]["used"] = "No"
                save_data(data)
                return "To No"
        else :
                return "Nothing"

#List Of Massages
startmassage = """✨ پلتفرم حرفه‌ای تبلیغات در کانال بله ویکی ماینکرفت ✨
🔥 پشتیبانی ها (با یکی پیگیر باشید) : @arminia_ceo | @excallibur

*توجه کنید تمامی موارد زیر برای کانال های ماینکرفتی ۱۰ هزار تومان بیشتر است و در عوض به صورت تضمینی بازدهی بیشتری خواهید داشت! تعرفه ها به شرح زیر است ✍️*

🔶 تبلیغات تضمینی
• هر 100 عضو : ۷۰,۰۰۰ تومان 
• جذب تضمینی ممبر به تعداد دلخواه شما

🟢 تبلیغات بازدیدی
• هر 1000 بازدید : ۳۰,۰۰۰ تومان
• مناسب برای کمپین‌های بازدید محور

⏳ تبلیغات ساعتی
• هر ساعت : ۵۰,۰۰۰ تومان
• نمایش به صورت آخرین پست در بازه های زمانی

🌃 تبلیغات شبانه
• هر شب : ۲۰,۰۰۰ تومان
• نمایش به صورت آخرین پست در بازه ساعتی 12 شب تا 10 صبح

_📌 برای سفارش مد نظر خود، بر اساس لیست داده شده در بالا، به پیوی پشتیبانی مراجعه کرده و محصول مدنظر خود را به همراه مقدار درخواستی بنویسید!_ *هر یک از پشتیبانی ها زودتر پاسخ داد، فقط و فقط در پیوی اون فرد پیگیر باشید، مسئولیت غیر این کار با عهده شماست.*

⚡ ویژگی‌های کلیدی پشتیبانی @arminia_ceo :
✅ گزارش عملکرد تبلیغ
✅ فعالیت در کانال شما برای جذب دو برابر (10 هزار تومان)
✅ پاسخ های سریع و جامع

⚡ ویژگی‌های کلیدی پشتیبانی @excallibur :
✅ پشتیبانی و مشاوره
✅ تضمین بازدید و جذب ممبر
✅ قابلیت های راهنمایی بیشتر

*⚠️ قوانین مربوط به خرید تبلیغات از ویکی*
1. پس از پرداخت وجه، امکان بازگشت وجه نیست.
2. پس از ارسال تبلیغ در کانال، امکان تغییر نوع تبلیغ را نخواهید داشت.
3. شما تنها قادر به استفاده یکباره از تخفیف خواهید بود!

*🎖️ در نگهداری کد تخفیف خود بکوشید، برای دریافت پیامی به سبک زیر بفرستید، توجه کنید که تخفیف پس از چک شدن توسط پشتیبانی فقط به آیدی چنل داده شده در کامند تعلق می‌گیرد، نه چنل دیگری :*
/off <channel>

*🫠 به طور مثال در صورتی که آیدی چنل شما @wiki_minecraft باشد، باید برای دریافت کد، مورد زیر را بفرستید :*
/off @wiki_minecraft
"""

nousername = """*درود بر شما کاربر گرامی! متاسفانه شما آیدی بله ندارید و قادر به استفاده از خدمات ربات نیستید 🫠

لطفا در صورت بروز مشکل با پشتیبانی این ربات صحبت کرده و مشکل آن را برطرف کنید : @arminia_ceo 🫵*
"""

offmass = """*بزودی کد تخفیف شما توسط ربات ساخته می‌شود! لطفا صبور باشید ✍️

زمان تخمینی برای ساخته شدن کد تخفیف : 4 الی 6 ثانیه 🔥*
"""

errortime = """* متاسفانه شما دارید از کامند اشتباهی استفاده می‌کنید، لطفا دوباره تلاش کنید ✍️

لطفا در صورت بروز مشکل با پشتیبانی این ربات صحبت کرده و مشکل آن را برطرف کنید : @arminia_ceo 🫵*
"""

listmasssave = """*✍️ لیست کاربران و کد های تخفیف آن ها به شرح زیر می‌باشد :*

"""

tiptime = """*🔥 توجه کنید برای تغییر استفاده شده یا نشده یک کد تخفیف، از دستور زیر استفاده کنید!*
/change <username>
"""

toyesmass = """*✍️ وضعیت کد تخفیف از "استفاده نشده" به "استفاده شده" تغییر کرد!

🫵 اگر ایرادی می‌بینی حتما با پشتیبانی در میان بزار : @arminia_ceo *
"""

tonomass = """
*✍️ وضعیت کد تخفیف از "استفاده شده" به "استفاده نشده" تغییر کرد!

🫵 اگر ایرادی می‌بینی حتما با پشتیبانی در میان بزار : @arminia_ceo *
"""

nochangemass = """
*✍️ به دلیل وجود مشکلات فنی، تغییری در وضعیت کد رخ نداد!

🫵 اگر ایرادی می‌بینی حتما با پشتیبانی در میان بزار : @arminia_ceo *
"""

offfail = """
*✍️ متاسفانه یا کانال قبلا ثبت شده یا مشکلی در ثبت کانال وجود داره!

🫵 اگر ایرادی می‌بینی حتما با پشتیبانی در میان بزار : @arminia_ceo *
"""

offok = """
*🔥 کد تخفیف شما ایجاد شد، در حفظ آن کوشا باشید! دقت کنید مقدار تخفیف به صورت عددی در کد شما مشخص شده است :*
"""

#Short Massages
usernamelist = "🗂️ آیدی کاربر : "
offcodelist = "🎖️ کد تخفیف کاربر : "
usedlist = "🫵 وضعیت استفاده از کد : "

#Lists & Allow
list_of_commands = ["/start","start","/off","off","/userlist","userlist"]
admins = ["@arminia_ceo"]
#Massage
@bot.listen("on_message")
async def when_message(message: bale.Message):
        username = ''
        username = message.from_user.username
        ider = message.from_user.id
        first = message.from_user.first_name
        mainuser = message.from_user.username
        print('✅ Username: @', mainuser, sep ='')
        print('✅ ID:', ider)
        print('✅ Command:', message.content)
        print()
        if not isinstance(mainuser, str) :
                await message.reply(nousername)
        else :
                usernameman = '@' + message.from_user.username
                if message.content == "/start" or message.content == "start":
                        await message.reply(startmassage)
                elif message.content[0:4] == "/off" or message.content[0:4] == "off":
                        await message.reply(offmass)
                        autosleep = random.randrange(4, 6)
                        channeluser = message.content[5:]
                        print('⚠ ', channeluser, ' is trying to won off after ', autosleep, ' seconds.', sep = '')
                        time.sleep(autosleep)
                        data = load_data()
                        if channeluser in data :
                                await message.reply(offfail)
                                print('⚠ ', channeluser, ' channel had already Exist! Mission Failed', sep = '')
                                print()
                        else :
                                randomlistoff = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 25, 25, 35]
                                amountoff = random.choice(randomlistoff)
                                if len(str(amountoff)) == 1 :
                                        amountoff = '0' + str(amountoff)
                                else :
                                        amountoff = str(amountoff)
                                offcode = 'WikiAd!' + channeluser[1:5] + '%' + amountoff
                                userdict = {"offcode": offcode , "used": "No"}
                                set_user_data(channeluser, userdict)
                                await message.reply(offok  + offcode)
                                print('⚠ ', channeluser, ' channel had won %', amountoff, ' off after ', autosleep, ' seconds!', sep = '')
                                print()
                elif message.content == "/userlist" or message.content == "userlist" and usernameman in admins :
                        data = load_data()
                        listmass = listmasssave
                        for user_id, info in data.items():
                                listmass = listmass + f"{usernamelist}{user_id}\n"
                                listmass = listmass + f"{offcodelist}{info['offcode']}\n"
                                listmass = listmass + f"{usedlist}{info['used']}\n\n"
                        listmass = listmass + tiptime
                        await message.reply(listmass)
                elif message.content[0:7] == "/change" or message.content == "change" and usernameman in admins :
                        updaterlast = update_user_score(message.content[8:])
                        print('⚠ Username to Change : ', message.content[8:], ', Please Wait.', sep = '')
                        if updaterlast == "To Yes" :
                                await message.reply(toyesmass)
                                print('⚠ Username ', message.content[8:], ' Used code changed to Yes.', sep = '')
                                print()
                        elif updaterlast == "To No" :
                                await message.reply(tonomass)
                                print('⚠ Username ', message.content[8:], ' Used code changed to No.', sep = '')
                                print()
                        else :
                                await message.reply(nochangemass)
                                print('⚠ Username ', message.content[8:], ' Used code had no change.', sep = '')
                                print()
                else :
                        await message.reply(errortime)  
bot.run()
