'''
Assuming that we have some email addresses in the 
"username@companyname.com" format, please write program
 to print the company name of a given email address. 
Both user names and company names are composed of letters only.

'''
email_address = input("Enter Email Address : ")
company_name = (email_address.split("@")[1]).split(".")[0]

print(company_name)