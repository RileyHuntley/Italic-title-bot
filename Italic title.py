import wikipedia
import json
x = raw_input("Category:")
x = "Category:" + x
print x
def getCategoryList(x):
        site = wikipedia.getSite()
        predata = {'action': 'query',
            'list': 'categorymembers',
            'cmnamespace': '0',
            'cmtitle': x,
            'cmtype': 'page',
            'cmlimit': '2500',
            'cmprop': 'title',
            'format': 'json'
        }
        response, raw = site.postForm(site.apipath(), predata)
        result = json.loads(raw)
        reg = result
        return reg
print getCategoryList(x)
