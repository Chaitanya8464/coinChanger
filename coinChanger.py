def coin_change_greedy(amount, coins=[100, 50, 25, 10, 5, 1]):
    

    coins.sort(reverse=True)
    
    result = {}
    
   
    for coin in coins:
        count = amount // coin

        if count > 0:
            result[coin] = count
            amount -= count * coin
    
    return result


def display_change(change):
    """Print the change in a readable format."""
    total_coins = 0
    
    print("\nChange breakdown:")
    for coin, count in change.items():
        total_coins += count
        
        # Format the output based on coin value
        if coin == 100:
            coin_name = "dollar" if count == 1 else "dollars"
        elif coin == 50:
            coin_name = "half-dollar" if count == 1 else "half-dollars"
        elif coin == 25:
            coin_name = "quarter" if count == 1 else "quarters"
        elif coin == 10:
            coin_name = "dime" if count == 1 else "dimes"
        elif coin == 5:
            coin_name = "nickel" if count == 1 else "nickels"
        elif coin == 1:
            coin_name = "penny" if count == 1 else "pennies"
        else:
            coin_name = f"{coin}¢ coin" if count == 1 else f"{coin}¢ coins"
            
        print(f"{count} {coin_name}")
    
    print(f"\nTotal: {total_coins} coins")


def main():
    print("COIN CHANGE DISPENSER")
    print("---------------------")
    
    # Get amount from user
    while True:
        try:
            amount_input = input("\nEnter amount (in cents or dollars, e.g., 125 or 1.25): ")
            
            # Handle dollar input (with decimal)
            if '.' in amount_input:
                dollars, cents = amount_input.split('.')
                # Ensure cents has 2 digits
                cents = cents + '0' if len(cents) == 1 else cents
                amount = int(dollars) * 100 + int(cents[:2])
            else:
                # Handle cent input
                amount = int(amount_input)
                
            if amount < 0:
                print("Amount cannot be negative.")
                continue
            
            break
        except ValueError:
            print("Please enter a valid amount.")
    
    # Calculate and display change
    change = coin_change_greedy(amount)
    display_change(change)
    
    # Format the total amount
    if amount >= 100:
        dollars = amount // 100
        cents = amount % 100
        formatted_amount = f"${dollars}.{cents:02d}"
    else:
        formatted_amount = f"{amount}¢"
    
    print(f"\nTotal amount: {formatted_amount}")


if __name__ == "__main__":
    main()