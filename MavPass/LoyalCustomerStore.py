import random
def discountcreater():
    customer = {}

    for i in range (1,201):
        discount = random.random()
        customer[str(i)] = round(discount,2)

    with open("Test.txt","w") as f:
        for key, values in customer.items():
            f.write(f"Customer ID: {key} : discount {values} \n")
    return customer

def discountremover(id, dict):
    dict.pop(str(id))
    return dict

print(discountremover(5,discountcreater()))