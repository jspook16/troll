import requests
import urllib, json
import os
import requests
import subprocess
#import math
import time
import sys
#import curses
import binascii
import ast
from blessings import Terminal
#from select import select
import threading
#import readline
import multiprocessing


y = 0		# This is set for the initial contents of mempool_old

term = Terminal()


print '\n'
username = raw_input('what is your username for this session? ')	# Get username input
print '\n'

directory_path = raw_input('What directory is komodod installed in? [example: /home/mydirectory/komodo/src/  -- make sure you include all the forward slashes]  ::  ')
print '\n'

chain = raw_input('What Asset Chain would you like to Troll on? ')
print '\n'


def message_thread():
    while True:
        time.sleep(1)
	term = Terminal()
	with term.location (0, term.height -1):
		message = raw_input(term.green(':  ') + term.clear_eol)    # Dispalys Message area in green

#        sys.stdout.write('\r'+' '*(len(readline.get_line_buffer())+2)+'\r')
#        print 'Interrupting text!'
#	message = raw_input('Message: ')

	message_send = subprocess.check_output( directory_path + 'komodo-cli -ac_name='+ chain +' kvupdate '  + username + ' \"' +message+ '\" 1 > /dev/null',shell=True)		         # Sends message.

#        sys.stdout.write('Messages ' + readline.get_line_buffer())
        sys.stdout.flush()


def update_messages():
	while True:	

		global y		# Using global y to get initial value of 0

		mempool = subprocess.check_output( directory_path + 'komodo-cli -ac_name='+ chain +' getrawmempool',shell=True)	# Get rawmempool txids
		mempool = ast.literal_eval(mempool.decode())	# Decode the txid entries to a true list
#		print mempool
	
#============================================================================================================================================
		
		if y == 0:
			mempool_old=[]	# Set the initial mempool_old values to nothing
			y = +1
#			print y										# Debug
		else:
			y = +1
#			print y										# Debug

		mempool_txs = [i for i in mempool if i not in mempool_old]	# Create a list of new mempool tx ids by comparing it with processed list in mempool_old
#		mempool_txs = ast.literal_eval(mempool_txs.decode())
	#	print 'this is the difference list', mempool_txs					# Debug

	# ===========================================================================================================================================
		
		mempool_old = mempool

# ==============================================================================================================
		x = 0
		for mempool_tx in mempool_txs:				# Iterate txids to retrieve messages

			raw = mempool_txs[x]
#			print ' this is in the mempool', raw						# Debug
 
			rawtransaction = subprocess.check_output( directory_path + 'komodo-cli -ac_name='+ chain +' getrawtransaction \'' +raw+  '\' 1 | jq .vout[2].scriptPubKey.asm',shell=True)	# Get raw transaction info for a txid

			#command = ('/media/jspook16/SugarGlider/Komodo/KomodoNative/komodo/src/komodo-cli -ac_name=LIZ getrawtransaction \"'  +raw+ '\" 1 | jq .vout[2].scriptPubKey.asm')	# Debug to look at command being passed
			#print command										# Debug
	#		rawtransaction = subprocess.check_output(command,shell=True)	# Debug to test command structure

#			print 'raw transaction is:', rawtransaction					# Debug

			hex_input = (bytes (rawtransaction))		# Gets the next raw transaction hex ready for processing
#			print hex_input[1:10]								# Debug

			test = hex_input[0:4]
			test = str(test)
#			print test									# Debug
			

			if (test == 'null'):				# Checks to see if transaction is not KV
				with term.location (0, term.height -2):
#                               print ('\n')
	                                print (term.green( '___________Transaction on '+ chain +' Chain !!!____________' +  term.clear_eol + '\n'))
	                                print ""
				x += 1
				continue
			else:
#				print 'this is valid', test							# Debug
				x += 1


			key_length = hex_input[13:15]			# Gets key length. Key Length is in static location in hex string
			key_len = int(key_length.decode('ascii'),16)	# Converts key length to an int
	#		print 'key length is', key_len							# Debug

			if (key_len%2==0):				# Checks to see if key length is an odd number. Cause issues when handling bytes. I dont think we need this if/else anymore.
				key_pad = key_len * 2			# If even, multiplies by 2
	#			print 'key pad = ', key_pad						# Debug

			else:						# Key length is odd
				key_pad = key_len  * 2			# If odd, multiplies by 2
	#			print 'key pad =', key_pad

			key = hex_input[35:key_pad+37]			# Assigns the key (username) depending on the key length identified above
			key = binascii.unhexlify (bytes(key))		# Converts key (username) to readable text
	#		print 'username is', key							# Debug


			value_length = hex_input[17:19]			# Checks value (message) length. Value Length is in static location in hex string
			value_len = int(value_length.decode('ascii'),16)# Converts value length to an int
	#		print 'value length =', value_len						# Debug

			if (value_len%2==0):				# Checks to see if value length is an odd number. Causes issues when handling bytes. Need to investigate if we need this.
				value_pad = value_len * 2		# If even, multiplies by 2
	#		        print 'value_pad = ', value_pad						# Debug

			else:						# Value length is odd
				value_pad = (value_len ) * 2		# Adds 1 to value length and multiplies by 2. This may be ok. Need to check if we are displaying an extra byte
	#		        print 'value_pad =', value_pad						# Debug

			value = hex_input[key_pad+37:key_pad+37+value_pad]	# Assigns the value (message) depending on the value length identified above
	#		print 'raw value is', value							# Debug

			value = binascii.unhexlify(bytes(value))	# Converts  value (message) to readable text
	#		print 'message is', value							# Debug
	#		print key,': ',value								# Debug
	
			term = Terminal()				# Commented out. May be ok with stating this globally.
		        with term.location (0, term.height -2):
#			        print ('\n')
				print ( key + ' : '+ value + term.clear_eol + '\n')	# Commented out for testing
				print ""
#				sys.stdout.flush()

# =======================================================================================================================================================================================================================

time.sleep(0.5)		

# =======================================================================================================================================================================================================================


# ====================================================================================================
input_thread = threading.Thread(target=message_thread)
status_thread = threading.Thread(target=update_messages)


input_thread.start()
status_thread.start()

input_thread.join()
status_thread.join()
# ======================================================================================================

#input_thread = multiprocessing.Process(target=message_thread)
#status_thread = multiprocessing.Process(target=update_messages)

#input_thread.start()
#status_thread.start()

#input_thread.join()
#status_thread.join()

# ======================================================================================================
