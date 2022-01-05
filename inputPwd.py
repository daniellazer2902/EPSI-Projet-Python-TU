from main import checkPwd

if __name__ == '__main__':
    pwd = input("Enter your password : ")
    res = checkPwd(pwd)
    if res[0]:
        print("Good Password")
    else:
        for i in range(1, len(res)):
            print(res[i]['message'])