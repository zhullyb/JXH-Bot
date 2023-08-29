import plugins.quote as quote

def messageHander(data):
    message = data['message']
    quote.check(message)


