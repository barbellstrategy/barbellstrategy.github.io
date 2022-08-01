import xmltodict
import markdownify
from dateutil.parser import parse

with open('w2.xml','rb') as f:
    document=xmltodict.parse(f)

workouts={}
for item in document['rss']['channel']['item']:
    if 'content:encoded' in item and item['content:encoded'] is not None:
        content=markdownify.markdownify(item['content:encoded'],heading_style='ATX')
        found=False

        find='Workout**'
        if not found and find in content:
            found=True
            content=content[content.find(find)+len(find):]
            
        if not found: 
            continue

        date=parse(item['pubDate'])
        workouts[date]=content
        # print('## ',date.strftime('%d-%b-%Y'))
        # print(content)

for date in sorted(workouts.keys(), key=lambda x:x.timestamp()):
    print('## ',date.strftime('%d-%b-%Y'))
    print(workouts[date])
