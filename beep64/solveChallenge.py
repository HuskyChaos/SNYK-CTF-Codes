# Make sure to keep the extracted audio file in the same folder.

import os, subprocess, base64
os.system('git clone https://github.com/ribt/dtmf-decoder.git')
os.chdir('dtmf-decoder/')
dtmf_decoded = subprocess.check_output(['python3','dtmf.py', '../sine.wav'], text=True)

dtmf_decoded = dtmf_decoded.split('*')
numpad = [['a', 'b', 'c'],['d', 'e', 'f'],['g', 'h', 'i'],['j', 'k', 'l'],
    ['m', 'n', 'o'],['p', 'q', 'r', 's'],['t', 'u', 'v'],['w', 'x', 'y', 'z']
]
t6_decode = ''
for i in dtmf_decoded:
    if '2' in i:t6_decode+=numpad[0][len(i)-1]
    elif '3' in i:t6_decode+=numpad[1][len(i)-1]
    elif '4' in i:t6_decode+=numpad[2][len(i)-1]
    elif '5' in i:t6_decode+=numpad[3][len(i)-1]
    elif '6' in i:t6_decode+=numpad[4][len(i)-1]
    elif '7' in i:t6_decode+=numpad[5][len(i)-1]
    elif '8' in i:t6_decode+=numpad[6][len(i)-1]
    elif '9' in i:t6_decode+=numpad[7][len(i)-1]
t6_decode = t6_decode[9:]

binary_decode = ''
i = 0
while i < len(t6_decode)-1:
    if t6_decode[i] == 'z':
        binary_decode+='0'
        i+=4
    elif t6_decode[i] == 'o':
        binary_decode+='1'
        i+=3
    elif t6_decode[i] == 's':
        i+=5

i=0
base64_decode = ''
while i<len(binary_decode):
    base64_decode+=chr(int(binary_decode[i:i+8], 2))
    i+=8
print(f"\033[32m[+] Here's your flag:\033[00m")
print(base64.b64decode(base64_decode.encode()).decode())
