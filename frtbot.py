import telegram as tg
import time
import os.path,os.stat
#from subprocess import call,Popen
import subprocess
update_id_fname = "update_id.frt"
update_id = -1
if os.path.isfile(update_id_fname) and os.stat(update_id_fname).st_size !=0:
	try:
		update_id_fd = open(update_id_fname,"rb+")
		update_id = int(update_id_fd.readline())
	except IOError:
		print "IOError accured!"
		exit()
else:
	try:	
		print "There is no "+update_id_fname+" file exit or it's empty try to create newone!"
		update_id_fd = open(update_id_fname,"wb")
		update_id = 0
	except IOError:
		print "IOError accured!"
		exit()
#if update_id < 0 :
#	update_id = int(update_id_fd.readline())
#	print "The last update_id is :"+str(update_id)
#else:
#	update_id = 0
	
print "Strat the fortune Bot"
bot = tg.Bot(token='<YOUR TOKEN>')
print "Try to run getMe"
print "I am "+bot.getMe().first_name
print "Try to run fortune"
#print call("fortune")
if subprocess.Popen("fortune", shell=True, stdout=subprocess.PIPE).stdout.read():
	print "fortune is OK"
else:
	print "Please install fortune and run again!"
	exit()
#update_id = 0
custom_keyboard = [[ tg.Emoji.THUMBS_UP_SIGN, tg.Emoji.THUMBS_DOWN_SIGN ]]
reply_markup = tg.ReplyKeyboardMarkup(custom_keyboard)


while(True):
	updates = bot.getUpdates(offset=update_id,timeout=120)
	for update in updates:
		if (update.update_id != update_id):
			update_id = update.update_id
			update_id_fd.seek(0,0)
			update_id_fd.write(str(update_id)+"\n")
			#print update
			if update.message.chat == None:
				continue
			bot.sendChatAction(update.message.chat_id,tg.ChatAction.TYPING)
			fortune = subprocess.Popen("fortune", shell=True, stdout=subprocess.PIPE).stdout.read()
			print update_id
			print fortune
			
			bot.sendMessage(chat_id=update.message.chat_id,text=fortune,reply_markup=reply_markup)
		#time.sleep(1)
	time.sleep(1)
if update_id_fd:
	update_id_fd.close()

