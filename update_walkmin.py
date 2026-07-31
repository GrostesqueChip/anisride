import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'(stop: "HMT Hospital Stop", time: ".*?", walkMin: )5', r'\g<1>15', content)
content = content.replace('walk to HMT Hospital Stop \u00b7 5 min', 'walk to HMT Hospital Stop \u00b7 15 min')
content = content.replace('Walk to <strong>HMT Hospital Stop</strong> \u00b7 ~400m / 5 min', 'Walk to <strong>HMT Hospital Stop</strong> \u00b7 ~400m / 15 min')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
