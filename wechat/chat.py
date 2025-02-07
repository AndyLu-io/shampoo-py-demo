import itchat

# 登录微信
itchat.login()

friends=itchat.get_friends(update=True)[0:]
print(friends)


Î