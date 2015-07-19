from HTMLParser import HTMLParser
from gtts import gTTS

htmlp = HTMLParser()

def gen_voice(sentence):
    underscored = ''.join(map(lambda x: x if x.isalnum() else '_', sentence))
    gTTS(sentence).save(underscored + '.mp3')

with open('input.txt') as f:
    for line in f:
        raw = line.split('\t')[0]
        sentence = htmlp.unescape(raw.decode('utf-8'))
        gen_voice(sentence)
