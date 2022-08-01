import xmltodict
import markdownify
from dateutil.parser import parse

with open('w1.xml','rb') as f:
    document=xmltodict.parse(f)

workouts={}
for item in document['rss']['channel']['item']:
    content=markdownify.markdownify(item['content:encoded'],heading_style='ATX')
    date=parse(item['pubDate'])
    workouts[date]=content

for date in sorted(workouts.keys(), key=lambda x:x.timestamp()):
    print('## ',date.strftime('%d-%b-%Y'))
    print(workouts[date])
