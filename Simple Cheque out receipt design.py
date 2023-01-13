# Now we want to create a variable called namesake

lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""

# Now we are about to create price for the loveseat
lovely_loveseat_price = float(254.00)

# Now we are adding a characteristic piece of furniture!

stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""

# Now setting the price for our Stylish Settee 
stylish_settee_price = 180.50

# Now creating a new variable called luxurious lamp description
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""

# Setting the price of the luxurious lamp
luxurious_lamp_price = float(52.15)

# Now defining for sales tax
sales_tax = float(.088)

# This is to keep a running tally of their expenses by defining a variable. 
# Since they haven't purchased anything yet, let's set that variable to = 0.
customer_one_total = 0

# now creating a variable to keep a list of the things a customer is purchasing.
customer_one_itemization = ""

# When our customer decides to buy our lovely loveseat!, add then the price to customer_one.

customer_one_total += lovely_loveseat_price

# Now tracking the bougth Items, we add a description of the Lovely Loveseat to customer items
customer_one_itemization += lovely_loveseat_description

# Our customer also decides to add the luxurious lamp, hence Also adding the price of the lamp to total

customer_one_total += luxurious_lamp_price

# Now add the description
customer_one_itemization += luxurious_lamp_description

# Now creating a variable called customer one tax
customer_one_tax = customer_one_total * sales_tax

# Now to add a sales_tax to customers total we have
customer_one_total += customer_one_tax

# Now we begin to print out our receipt for the customer to check out
print("Customer One Items: ", customer_one_itemization)

print(customer_one_itemization)
