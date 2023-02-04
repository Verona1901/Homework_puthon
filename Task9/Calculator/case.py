from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from user_input import *


match oper:
    case '/':
        summa = num_1 / num_2
        Bot.send_message(Update.message.from_user.id, f"Результат {num_1} {oper} {num_2} = {summa}")
    case '*':
        summa = num_1 * num_2
        Bot.send_message(Update.message.from_user.id, f"Результат {num_1} {oper} {num_2} = {summa}")
    case '-':
        summa = num_1 - num_2
        Bot.send_message(Update.message.from_user.id, f"Результат {num_1} {oper} {num_2} = {summa}")
    case '+':
        summa = num_1 + num_2