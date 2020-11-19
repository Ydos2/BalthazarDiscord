import time
import json
#import timeago as timesince

def get(file):
    try:
        with open(file, encoding='utf8') as data:
            return json.load(data)
    except AttributeError:
        raise AttributeError("Unknown argument")
    except FileNotFoundError:
        raise FileNotFoundError("JSON file wasn't found")


#def timeago(target):
#    return timesince.format(target)


def date(target, clock=True):
    if not clock:
        return target.strftime("%d %B %Y")
    return target.strftime("%d %B %Y, %H:%M")