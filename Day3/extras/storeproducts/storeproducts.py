from store import Store
from products import Product

apples = Product("apples", 5, "fruit")
bananas = Product("bananas", 5, "fruit")
lego = Product("lego", 5, "toy")

coding = Store("Coding Dojo", [])
coding.add_product(apples).add_product(bananas).add_product(lego).set_clearance("fruit", 0.1).print_info()
