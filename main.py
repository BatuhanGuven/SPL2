
# try:
#     product_name = input("Enter the product name: ")
#     net_price = float(input("Enter the product price (net): "))
#     client_email = input("Enter the client email: ")
#     client_phone = input("Enter the client phone: ")
#     gross_price = net_price+ net_price*23/100
#     print("Welcome in Batuhan's store")
#     print("Product Name: ", product_name)
#     print("Net Price: ", net_price)
#     print("Gross Price: ", gross_price)
#     print("Client Email: ", client_email)
#     print("Client Phone: ", client_phone)
# except ValueError:
#     print("Process interrupted. Bad data type.")
#

p = False
q = True

left_s=not(p or q)
right_s=not(p) and not(q)
print(left_s==right_s)
