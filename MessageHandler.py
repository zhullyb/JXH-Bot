import plugins.quote as quote
from plugins.xlKWReply import XlKWReply

kwr1 = XlKWReply('example_kdocs_id')

def messageHander(data):
    message = data['message']
    quote.check(message)
    kwr1.check(data)


