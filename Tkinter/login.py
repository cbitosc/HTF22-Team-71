user_name = 'Rames'
pass_word = '1342%plse'
file = open('login credentials.csv','r')
headers = file.readline()
credentials = file.readline()
while credentials!='':
    s = credentials.split(',')
    print(s)
    if s[0]==user_name:
        if s[1][:-1]==pass_word:
            print('Login successful')
            break
    credentials = file.readline()
print("login unsuccessful")