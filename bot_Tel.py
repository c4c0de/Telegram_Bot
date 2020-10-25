import telebot
import time
import os
from datetime import datetime

os.environ["TZ"] = "Asia/Kolkata"
#time.tzset()


# print(time.time())
TOKEN = '1002713211:AAF4UxJg-sqEtVQVEEqWUtI_BplLQuFQrs4'  # replace token which you got from @botfather
bot = telebot.TeleBot(token=TOKEN)

from datetime import datetime as date

# print(date.today().weekday())

time_table = {0: {'09:00': 'toc\nhttps://meet.google.com/lookup/ephmmeas6j', '10:00': 'mm\nhttps://meet.google.com/lookup/bpr5e6dt6u', '11:00': 'gtc\nhttps://meet.google.com/lookup/gymjsmeumb', '12:00': 'sc\nhttps://meet.google.com/lookup/av3biuh5hq'},
              1: {'09:00': 'dc\nhttps://meet.google.com/lookup/f2r7dglxns', '10:00': 'toc\nhttps://meet.google.com/lookup/ephmmeas6j', '11:00': 'ss\nhttps://meet.google.com/lookup/dqgihjb7vs', '12:00': 'gtc\nhttps://meet.google.com/lookup/gymjsmeumb'},
              2: {'09:00': 'gtc\nhttps://meet.google.com/lookup/gymjsmeumb', '10:00': 'sc\nhttps://meet.google.com/lookup/av3biuh5hq', '11:00': 'ss\nhttps://meet.google.com/lookup/dqgihjb7vs', '12:00': 'toc\nhttps://meet.google.com/lookup/ephmmeas6j'},
              3: {'09:00': 'sc\nhttps://meet.google.com/lookup/av3biuh5hq', '10:00': 'gtc\nhttps://meet.google.com/lookup/gymjsmeumb', '11:00': 'mm\nhttps://meet.google.com/lookup/bpr5e6dt6u', '12:00': 'dc\nhttps://meet.google.com/lookup/f2r7dglxns'},
              4: {'09:00': 'ss\nhttps://meet.google.com/lookup/dqgihjb7vs', '10:00': 'dc\nhttps://meet.google.com/lookup/f2r7dglxns', '19:00': 'toc\nhttps://meet.google.com/lookup/ephmmeas6j', '20:00': 'mm\nhttps://meet.google.com/lookup/bpr5e6dt6u'},
              5: {'09:00': 'system sotware', '10:00': 'mm', '11:00': 'gtc\nhttps://meet.google.com/lookup/gymjsmeumb', '12:00': 'toc\nhttps://meet.google.com/lookup/ephmmeas6j'}}


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'hello')
    bot.send_message(message.chat.id, 'to use /now,/next or \n /subject_name   eg:  /ss ,\n/sub to view all subject')


@bot.message_handler(commands=['stop'])
def stop(message):
    bot.reply_to(message, 'bi')


@bot.message_handler(commands=['ss'])
def ss(message):
    bot.reply_to(message, 'ss\nhttps://meet.google.com/lookup/dqgihjb7vs')


@bot.message_handler(commands=['sc'])
def sc(message):
    bot.reply_to(message, 'sc\nhttps://meet.google.com/lookup/av3biuh5hq')


@bot.message_handler(commands=['mm'])
def mm(message):
    bot.reply_to(message, 'mm\nhttps://meet.google.com/lookup/bpr5e6dt6u')


@bot.message_handler(commands=['dc'])
def dc(message):
    bot.reply_to(message, 'dc\nhttps://meet.google.com/lookup/f2r7dglxns')


@bot.message_handler(commands=['gtc'])
def gtc(message):
    bot.reply_to(message, 'gtc\nhttps://meet.google.com/lookup/gymjsmeumb')


@bot.message_handler(commands=['toc'])
def toc(message):
    bot.reply_to(message, 'toc\nhttps://meet.google.com/lookup/ephmmeas6j')


@bot.message_handler(commands=['sub'])
def sub(message):
    bot.reply_to(message, '1./toc \n2./gtc \n3./dc \n4./ss \n5./sc \n6./mm \n')


@bot.message_handler(commands=['now'])
def now(message):
    try:
        sub = time_table[date.today().weekday()]
    except Exception:
        pass

    time1 = str(date.time(date.now()))
    min = int(time1[3:5])
    if min < 15:
        '''hr = int(time1[:2]) - 1
        print(hr)
        corrected_time = str(hr) + ':00'''''
        bot.reply_to(message, 'no ongoing class')

    else:
        try:
            bot.reply_to(message, sub[time1[:2] + ':00'])
        except Exception:
            bot.reply_to(message, 'no ongoing class')


@bot.message_handler(commands=['next'])
def next(message):
    try:
        sub = time_table[date.today().weekday()]
    except Exception:
        pass

    time1 = str(date.time(date.now()))
    min = int(time1[3:5])
    if min < 15:
        hr = int(time1[:2])
        # print(hr)
        corrected_time = str(hr) + ':00'
        try:
            if hr <= 9:
                corrected_time = '0'+corrected_time
                bot.reply_to(message, sub[corrected_time[:5]])
            else:
                bot.reply_to(message, sub[corrected_time[:5]])
        except Exception:
            bot.reply_to(message,'no upcoming class')

    else:
        hr = int(time1[:2]) + 1
        #print(hr)
        corrected_time = str(hr) + ':00'
        print(corrected_time)
        try:
            if hr <= 9:
                corrected_time = '0'+corrected_time
                #print(sub[corrected_time[:5]])
                bot.reply_to(message, sub[corrected_time[:5]])
            else:
                bot.reply_to(message, sub[corrected_time[:5]])
        except Exception:
            bot.reply_to(message,'no upcoming class f')


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(0.2)
