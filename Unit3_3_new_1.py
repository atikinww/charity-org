inventory = ['Jacket', 'Trousers', 'Knife']
zero_answer = ''
strategy = input("What is the strategy? ")

if strategy == "FIFO":
    your_items = input("0What have you got? ")
    while your_items != zero_answer:
        inventory.append(your_items)
        print(inventory)
        break
    your_items = input("FIFO_What have you got? ")
    inventory.append(your_items)
    print(inventory)

second_answer = input("Thanks. Anything else?")

if second_answer != zero_answer:
    second_answer = input("Anything else?")
    inventory.append(second_answer)
    print(inventory)
    pass
else:
    last_item = inventory.pop()
    print(f'Here you have it, {last_item}')
    print("Thank you, bye!")

# else:
# your_items = input("1What have you got? ")
# while your_items != zero_answer:
# inventory.insert(0, your_items)
# print(inventory)
# your_items = input("FIFO_What have you got? ")
