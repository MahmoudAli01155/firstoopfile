# string=input("Enter the String :")
# letter=input("Enter the Letter :")
# iteList =[]
# for i in range(len(string)):
#     if string[i]==letter :
#         iteList.append(i)
#
# print(iteList)
##############################################################
# number=int(input("Enter the Number :"))
# sumlist=[]
# for i in range(1,number+1):
#     malist=[]
#     for n in range(1,i+1):
#         malist.append(n*i)
#     sumlist.append(malist)
# print(sumlist)
##########################################################################
thelist=list(input("Enter the list : ").replace("[", "").replace("]", "").replace("'", "").replace('"', "").split(","))
print(thelist)
firstletterlist=[]
for i in range(0, len(thelist),1):
    stringitem=thelist[i]
    firstletterlist.append(stringitem[0])
print(firstletterlist)

dictionarylist={}
for i in range(0, len(thelist),1):
    item = [thelist[i]]
    dictionarylist[firstletterlist[i]] = item

print(dictionarylist)


#print(dictionarylist)