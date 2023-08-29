import re

quote_pattern = r".*?(?: |.)(/q(?: \d)?)$"

def check(message):
    match = re.search(quote_pattern, message)
    q_command = match.group(1) if match else ""
    if len(q_command.split()) == 1:
        quote()
    else:
        quote_num = q_command.split()[1]
        quote(quote_num)
        
def quote():
    pass