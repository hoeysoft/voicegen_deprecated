from HTMLParser import HTMLParser
htmlp = HTMLParser()

def soundline(sentence):
    underscored = ''.join(map(lambda x: x if x.isalnum() else '_', sentence))
    return u'<div>[sound:{}]</div>'.format(underscored+'.mp3')

with open('input.txt') as f,\
     open('output.txt', 'w') as of:
    for line in f:
        uline = line.decode('utf-8')
        columns = uline.split('\t')
        sentence = htmlp.unescape(columns[0])
        columns[2] = columns[2] + soundline(sentence)
        of.write('\t'.join(columns).encode('utf-8'))
