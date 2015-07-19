import os
from HTMLParser import HTMLParser
from gtts import gTTS

htmlp = HTMLParser()

def gen_voice(sentence):
    underscored = ''.join(map(lambda x: x if x.isalnum() else '_', sentence))
    filename = underscored + '.mp3'
    gTTS(sentence).save(filename)
    return filename

os.system('clear')
print 'voicegen'

while True:
    sentence = raw_input(':')
    filename = gen_voice(sentence)
    os.system('afplay {}'.format(filename))
    os.system('printf "[sound:{}]" | pbcopy'.format(filename))
