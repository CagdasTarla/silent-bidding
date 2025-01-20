from replit import clear

bidding_dict = {}
start_stop = "yes"
while start_stop == "yes":
  clear()
  bidder_name = input("Name of the bidder: ")
  bid_amount = int(input("Bidding amount: "))
  bidding_dict[bidder_name] = bid_amount
  start_stop = input("Do you want to place another bid? Type'yes' or 'no'. ")

max_bid = 0
max_bidder = ""
for name in bidding_dict:
  if bidding_dict[name] > max_bid:
    max_bid = bidding_dict[name]
    max_bidder = name
print(f"{max_bidder} has won the bidding with {max_bid} $")

input("Press enter to quit")