# Flipkart Mini Project - Assignment Version

class Flipkart:
    def __init__(self):
        # Products available in Flipkart Mini
        self.products = {
            101: {"name": "Mobile", "price": 15000},
            102: {"name": "Laptop", "price": 50000},
            103: {"name": "Headphones", "price": 1500},
            104: {"name": "Shoes", "price": 2500},
            105: {"name": "Watch", "price": 3000}
        }
        self.cart = []  # To store cart items

    def show_all_products(self):
        print("\nAvailable Products:")
        for pid, info in self.products.items():
            print(f"ID: {pid} | Name: {info['name']} | Price: ₹{info['price']}")

    def show_product_by_id(self, product_id):
        if product_id in self.products:
            info = self.products[product_id]
            print("\nProduct Details:")
            print(f"ID: {product_id}")
            print(f"Name: {info['name']}")
            print(f"Price: ₹{info['price']}")
        else:
            print("Invalid Product ID.")

    def add_to_cart(self, product_id):
        if product_id in self.products:
            self.cart.append(self.products[product_id])
            print(f"{self.products[product_id]['name']} added to cart.")
        else:
            print("Invalid Product ID.")

    def view_cart(self):
        if not self.cart:
            print("\nYour cart is empty.")
        else:
            print("\nItems in your cart:")
            total = 0
            for item in self.cart:
                print(f"{item['name']} - ₹{item['price']}")
                total += item['price']
            print(f"Total Amount: ₹{total}")

    def checkout(self):
        if not self.cart:
            print("\nCart is empty. Add items before checkout.")
        else:
            self.view_cart()
            print("Order placed successfully.")
            self.cart.clear()

# Main program
def main():
    flipkart = Flipkart()
    while True:
        print("\n==== Flipkart Mini Menu ====")
        print("1. Show All Products")
        print("2. Show Product by ID")
        print("3. Add to Cart")
        print("4. View Cart")
        print("5.your order successfully")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            flipkart.show_all_products()
        elif choice == '2':
            try:
                pid = int(input("Enter Product ID: "))
                flipkart.show_product_by_id(pid)
            except:
                print("Please enter a valid number.")
        elif choice == '3':
            try:
                pid = int(input("Enter Product ID to add to cart: "))
                flipkart.add_to_cart(pid)
            except:
                print("Please enter a valid number.")
        elif choice == '4':
            flipkart.view_cart()
        elif choice == '5':
            flipkart.checkout()
        elif choice == '6':
            print("Thank you for using Flipkart Mini!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
