'''
Creating a tool that can strip a username from an email
'''

email = 'mysticalmango647@github.com'
print(email.split('@')[0])


emails =['hello@mango.com', 'goodbyte@mango.ca']
print([x.split('@')[0] for x in emails])