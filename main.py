import os
import clipboard
from HTMLParser import HTMLParser
from gtts import gTTS

htmlp = HTMLParser()


def to_filename(sentence):
    underscored = ''.join(map(lambda x: x if x.isalnum() else '_', sentence))
    return underscored + '.mp3'


def genvoice(sentence, filename):
    gTTS(sentence).save(filename)

os.system('clear')
while True:
    sentence = raw_input('vg:').strip()
    filename = to_filename(sentence)
    toclipboard = '{}\n[sound:{}]'.format(sentence, filename)
    clipboard.copy(toclipboard)
    genvoice(sentence, filename)
    os.system('afplay {}'.format(filename))
