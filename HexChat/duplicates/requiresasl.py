import hexchat

__module_name__ = 'RequireSASL'
__module_author__ = 'TingPing'
__module_version__ = '1'
__module_description__ = 'Disconnect if SASL fails'

def response_cb(word, word_eol, userdata):
	if word[1] == '904': # Failed
		hexchat.command('timer .1 discon') # Delay so disconnect happens after message.

hexchat.hook_print('SASL Response', response_cb)
