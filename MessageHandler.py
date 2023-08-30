import plugins.quote as quote
from plugins.xlKWReply import XlWKReply

def messageHander(data):
    message = data['message']
    quote.check(message)
    kwr1 = XlWKReply('example_kdocs_id')


