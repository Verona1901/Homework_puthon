import actions_with as act
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import user_input as u


heap = {
    'count': 0,
    'first': None, 
    'second': None,
    'operator': None
}

async def startcalc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    heap['count']=1
    await update.message.reply_text("Я простой калькулятор) Введите числа поочередно, затем знак матем. операции ")

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if heap['count'] != 0:
        if heap['count'] == 1:
            heap['first'] = update.message.text
            heap['count'] +=1
        elif heap['count'] == 2:
            heap['second'] = update.message.text
            heap['count'] +=1
        elif heap['count'] == 3:
            heap['operator'] = update.message.text
        
            a,b = u.inp(heap["first"], heap["second"])
            await update.message.reply_text(f"{a} {heap['operator']} {b} = {act.action(a,b,heap['operator'])}")
            heap['count'] = 0
            heap['first'] = None
            heap['second'] = None
            heap['operator'] = None





app = ApplicationBuilder().token("TOKEN").build()
print("Запускаюсь")
app.add_handler(CommandHandler("start", startcalc))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))



app.run_polling()
