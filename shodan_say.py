#!/usr/local/bin/python3

import requests
import urllib.parse
import random
import string
import sys
import os
import re
from subprocess import call

if len(sys.argv) != 2:

    print('I need something to say!')

else:

    lang = 'en'

    lines = sys.argv[1].split('\\n')

    say_sequence = []

    for line in lines:
        url = 'https://translate.google.com/translate_tts?ie=UTF-8&tl=%s&client=tw-ob&q=%s' % (
            lang, line)
        output = 'files/' + ''.join(random.choice(string.hexdigits)
                                    for i in range(32)) + '.mp3'
        r = requests.get(url)

        if 200 == r.status_code:
            if not os.path.isdir('files'):
                os.makedirs('files')
            with open(output, 'wb') as f:
                f.write(r.content)
            say_sequence += [output]

    for file in say_sequence:
        call('mpg123 %s' % file, shell=True)
        os.remove(file)
