email = input("Enter your email: ")

k, j, d = 0, 0, 0 
if len(email) >= 6:
    if ("@" in email) and (email.count("@") == 1):
        if (email[-4]==".") ^ (email[-3]=="."): # ^ = XOR ==> XOR is used to check if the last character is a dot or not
            for i in email:
                if i == i.isspace(): # i.isspace() checks if the character is a space
                    k = 1
                elif i.isalpha(): # i.isalpha() checks if the character is a letter
                    if i == i.upper(): # i.upper() checks if the character is a capital letter
                        j=1
                elif i.isdigit(): # i.isdigit() checks if the character is a number
                    continue
                elif i=="_" or i=="." or i=="@": # i=="_" or i=="." or i=="@" checks if the character is a underscore or a dot or an at symbol
                    continue
                else:
                    d=1
                    
            if k == 1 or j==1 or d==1:
                print("Valid Email3")
    else:
        print("Invalid Email 2")
else:
    print("Invalid Email 1")