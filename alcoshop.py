# alcoshop.py ver.001
# feature request 001 is realised
print("Program that desides to sell alcohol to customer or not to sell")
print " "
# current date just for example September 11, 2017
cye = 2017
cm = 9
cd = 11
print("If the customer is younger than a certain age, then he/she is not entitled to purchase alcohol.")
age= int(input ("Give the age at which purchase alcohol is allowed (whole years):"))
ye= int(input ("Give customer's year of birth: "))
m = int(input ("Give customer's month of birth (as a number from 1 to 12): "))
d = int(input ("Give customer's day of birth: "))
print " "
a= cye-ye
if (a>age):
	print "	You have", a, "year and You can buy an alcohol. "
elif (a<age):
	print "	You have", a, "year and You can not buy an alcohol. "
else: # a=age
	if (cm>m):
		print " You have", a , "year and", cm-m , "months and You can buy an alcohol. "
	elif (cm<m):
		print " You have", a-1 , "year and", cm-m+12 , "months and You can not yet buy an alcohol. "
	else: # a= age, cm=m
		if (d>cd):
			print "	You have", a , "year", cm-m , "months and", d-cd, "days and You can buy an alcohol. "
		elif(d<cd):
			print "	You have", a-1 , "year and", cm-m+11, "months. And You will have the same birthday when purchase alcohol is allowed only for", cd-d, "days and only then You will can buy an alcohol. "
		else: # the same birthday today
			print "	Congratiulations! You have the same birthday when purchase alcohol is allowed today! You can buy an alcohol. "

raw_input()
exit(0)
