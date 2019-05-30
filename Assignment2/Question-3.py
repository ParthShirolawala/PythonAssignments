import re

count = {}
ip_string = input("Enter a string:")

def countSpecial():
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    for i in ip_string:
        if(regex.match(i)) and i in count:
            count[i]+= 1;
        elif(regex.match(i)) and i not in count:
            count[i] = 1;
        else:
            continue

    print(count)

countSpecial()