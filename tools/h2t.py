import sys, re, html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in ('script','style','noscript'): s.skip+=1
        if t in ('p','br','div','li','h1','h2','h3','tr'): s.out.append('\n')
    def handle_endtag(s,t):
        if t in ('script','style','noscript'): s.skip=max(0,s.skip-1)
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
for f in sys.argv[1:]:
    raw=open(f,'rb').read()
    try: txt=raw.decode('utf-8')
    except: txt=raw.decode('cp1251','ignore')
    p=P(); p.feed(txt)
    t=''.join(p.out)
    t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(f+'.txt','w').write(t)
    print(f, len(t))
