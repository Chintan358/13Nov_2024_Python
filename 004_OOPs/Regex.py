import re

Nameage="""RanY Is 235 and Jeny is 65, Tom is_85 and Roy is 42 """

# age = re.findall(r'\d{1,3}',Nameage)
# # names=re.findall(r'[A-Za-z0-9_]',Nameage)
# names=re.findall(r'[a-z][A-Z]',Nameage)
# print(names)

# flag = re.search("i","niki is registered in python technology")
# print(flag)

# if re.search("i","niki is registered in python technology"):
#     print("found")
# else:
#     print("Not found")

# name="Python is world's best programming language "
# for i in re.finditer("world's",name):
#   ans=i.span()
#   print(ans)


# word="dog, bot , god , bot,rose , not "
# regex=re.compile("[a-z]og")
# word=regex.sub("Sample",word)
# print(word)


# print(re.match(r'cat','dog cat dog cat'))

# print("search function")

# print(re.search(r'cat','cat dog cat'))


print(re.match("^[a-zA-z0-9_]+@tops\\-int\\.com+$","test@tops-int.co"))

