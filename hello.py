#print("Blind Auction Program")

#def find_highest_bidder(bidding_dictionary):
#    winner = ""
#    highest_bid = 0
#    for bidder in bidding_dictionary:
#        bid_amount = bidding_dictionary[bidder]
#        print("\n"* 20 )
#        if bid_amount > highest_bid:
#            highest_bid = bid_amount
#            winner = bidder


#        print(f"The winner is {winner} with a bid of {highest_bid} ")

#bids = {}
#continue_bidding = True
#while continue_bidding:
#    name = input("What is your name?: ")
#    price = int(input("What is your bid?: "))
#    bids[name] = price
#    should_continue = input("Anyone else wants to bid? YES or NO?: ")
#    if should_continue == "NO":
#        continue_bidding = False
#        find_highest_bidder(bids)
#    if should_continue == "YES":
#        print("\n"* 20 )

#functions with output 

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# formatted_name = format_name("tushaR", "JumaLE") 
# print(formatted_name)

#storing function as a variable

# def add(n1, n2):
#     return n1 + n2 

# your_fav_operation = add

# print(your_fav_operation(2, 4))


#calculator using while loop
# def add(n1, n2):
#     return n1 + n2

# def substract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# operations = {"+" : add , "-" : substract , "*" : multiply , "/" : divide}

# should_accumalate = True
# def calculate():
#     num1 = float(input("What is the first number?: "))
#     while should_accumalate:
#         for symbol in operations:
#             print(symbol)
#         operation_symbol = input("Pick an operation: ")
#         num2 = float(input("What is the second number?: "))
#         answer = operations[operation_symbol](num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
#         direction = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
#         if direction == "y":
#             num1 = answer
#         else:
#             print(f"\n" * 30)
#             calculate()

#calculate()





























































































