# Resolve the problem!!
import re

def run():
    # Start  coding here
    with open('encoded.txt', 'r', encoding='utf-8') as f:

        secret_message = ''.join(re.findall('[a-z]', f.read()))
        print (secret_message)

if __name__ == '__main__':
    run()
