# index() function => Used to return index of given argument or substrings.

msg="A kong string with a silly typo"
print(msg.index('k'))
print(msg)

# Strings are immutable in Python i . e does not support item assignment.
# But they can be modified by using concatenation.
# Method => A function associated with a certain class .

new_msg=msg[0:2]+"l"+msg[3:]
print(new_msg)

#another way to concatenate strings is join()
new_msg=''.join(["A ","long ","string ","with ","a ","silly ","typo "])
print(new_msg)

print(new_msg.index('s'))  #Gives the first index where argument matches
print(new_msg.index('silly'))


# Membership Operators => Checks if given substring is present in string or not.
# in and not in
print("silly" in new_msg)      #True
print('type' in new_msg)	   #False
print("silly" not in new_msg)  #False


z='...'.join(['Hello, ','This ','is ','Neel '])
print(z)
print(''.join(['I, ','am ','your ','Friend ']))



#Q1
''' Imagine that your company has recently moved to using a new domain,
	but a lot of the company email addresses are still using the old one. 
	You want to write a program that replaces this old domain with the new one
	in any outdated email addresses.'''
#SOLUTION :

def replace_domain(email,old_domain,new_domain):
	if "@"+old_domain in email:
		index=email.index("@"+old_domain)
		new_email=email[:index]+"@"+new_domain
		print("Before =>")
		print(email)
		print("After =>")
		print(new_email)
	return email
replace_domain('neelpandey@msn.com','msn.com','microsoft.com')
#OUTPUT
''' Before =>
	neelpandey@msn.com
	After =>
	neelpandey@microsoft.com
'''


