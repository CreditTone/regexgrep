import re
import sys
try:
    p = re.compile(r'cat=(\d+)')
    m = p.finditer(sys.argv[1])
    ret = m.next()
    print ret.group(1)
except:
    pass
