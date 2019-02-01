from nntplib import NNTP

server=NNTP('web.aioe.org')

howmany=1
resp, count, first, last, name = server.group('comp.lang.python')
start = last-howmany+1
resp, overviews = server.over((start, last))
for id, over in overviews:
    subject = over['subject']
    resp, info = server.body(id)
    print(subject)
    print('-' * len(subject))
    for line in info.lines:
        print(line.decode('latin1'))
    print()
server.quit()
