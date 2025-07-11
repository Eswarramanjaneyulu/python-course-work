data= {
        101: {"name": "Mobile", "price": 15000,"Categories":"Electronics","Available Stock":100,"Sold Stock":20,"Discount Percentage":"2%","Product Features":"waterproof"},
        102: {"name": "Laptop", "price": 50000,"Categories":"Electronics","Available Stock":70,"Sold Stock":5,"Discount Percentage":"5%","Product Features":"waterproof"},
        103: {"name": "Headphones", "price": 1500,"Categories":"Electronics","Available Stock":200,"Sold Stock":10,"Discount Percentage":"2%","Product Features":"waterproof"},
        104: {"name": "Shoes", "price": 2500,"Categories":"fitness","Available Stock":50,"Sold Stock":15,"Discount Percentage":"2.5%","Product Features":"waterproof"},
        105: {"name": "SmartWatch", "price": 3000,"Categories":"Electronics","Available Stock":100,"Sold Stock":50,"Discount Percentage":"3%","Product Features":"waterproof"}
    }
        
a = int(input("Enter a Product ID: "))
if a in data:
    print("\nProduct Details:")
    print("ID:", a)
    print("Name:", data[a]["name"])
    print("Price: ₹", data[a]["price"])
    print("Category:", data[a]["Categories"])
    print("Available Stock:", data[a]["Available Stock"])
    print("Sold Stock:", data[a]["Sold Stock"])
    print("Discount:", data[a]["Discount Percentage"])
    print("Features:", data[a]["Product Features"])
else:
    print("Invalid Product ID. Please try again.")

