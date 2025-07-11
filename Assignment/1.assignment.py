class Mini_Flipkart:
    def __init__(self):
        self.products = {
            101: {"name": "Mobile", "price": 15000},
            102: {"name": "Laptop", "price": 50000},
            103: {"name": "Headphones", "price": 1500},
            104: {"name": "Shoes", "price": 2500},
            105: {"name": "Watch", "price": 3000}
        }
        self.cart = []

    def show_products(self):
        print("\nAvailable Products:")
        for pid, details in self.products.items():
            print(f"ID: {pid} | {details['name']} - {details['price']}")
            
    def show_product_by_id(self, product_id):
        if product_id in self.products:
            details = self.products[product_id]
            print(f"\nProduct Details for ID {product_id}:")
            print(f"Name: {details['name']}")
            print(f"Price: ₹{details['price']}")
        else:
            print("Invalid Product ID!")

    def add_to_cart(self, product_id):
        if product_id in self.products:
            self.cart.append(self.products[product_id])
            print(f"{self.products[product_id]['name']} added to cart.")
        else:
            print("Invalid Product ID!")

    def view_cart(self):
        if not self.cart:
            print("\nYour cart is empty!")
        else:
            print("\nItems in your cart:")
            total = 0
            for item in self.cart:
                print(f"{item['name']} - ₹{item['price']}")
                total += item['price']
            print(f"Total: ₹{total}")

    def checkout(self):
        if not self.cart:
            print("\nYour cart is empty. Add items before checkout.")
        else:
            self.view_cart()
            print("Thank you for shopping with Flipkart Mini!")
            self.cart.clear()

def main():
    app = Mini_Flipkart()
    while True:
        print("\n========= Flipkart Mini Menu =========")
        print("1. Show All Products")
        print("2. Show Product by ID")
        print("3. Add to Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            app.show_products()
        elif choice == '2':
            try:
                pid = int(input("Enter Product ID to view details: "))
                app.show_product_by_id(pid)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            try:
                pid = int(input("Enter Product ID to add to cart: "))
                app.add_to_cart(pid)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            app.view_cart()
        elif choice == '5':
            app.checkout()
        elif choice == '6':
            print("Exiting Flipkart Mini. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
