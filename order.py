from datetime import date
#create order class
class Order: 
  #Order class attributes
    order_id = 0 
    customer_name = "" 
    order_date = date.today()
    total_amount = 0
    total_tax = 0
    # initial order object
    def __init__(self, order_id, customer_name, order_date, total_amount): 
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount
    # calculate_tax method for calculate calculate_tax with total taxes given
    def calculate_tax(self, tax_rate):
        self.total_tax = self.total_amount + tax_rate
    # display_orders method for diplay an order details
    def display_order(self):
        return f"order_id: {self.order_id} \n customer_name: {self.customer_name} \n order_date: {self.order_date} \n total_amount: {self.total_amount} \n total_tax: {self.total_tax}"
#create OrderProcessor class
class OrderProcessor(Order): 
    #OrderProcessor class attributes
    orders = []
    total_taxs = 0
    total_revenue = 0
     # initial OrderProcessor object
    def __init__(self): 
        pass
    # calculate_total_tax method for calculate total_amount with total taxes from orders
    def calculate_total_tax(self):
        for order in  self.orders: 
            print(f"{order.total_tax}")
            self.total_taxs += order.total_tax
    # calculate_total_revenue method for calculate all total_amount in orders
    def calculate_total_revenue(self):
        for order in  self.orders: 
            self.total_revenue += order.total_amount
    # add_order method for add orders
    def add_order(self, order):
        self.orders.append(order)
    # display_orders method for diplay all order details
    def display_orders(self):
        for order in  self.orders: 
            print(f"order_id: {order.order_id} \n customer_name: {order.customer_name} \n order_date: {order.order_date} \n total_amount: {order.total_amount} \n total_tax: {order.total_tax} \n total_taxs: {self.total_taxs} \n total_revenue: {self.total_revenue}")

# create Order instance
order1 = Order(1,"nada",date.fromisoformat('2019-12-04'), 10000)
order1.calculate_tax(1000)
print(order1.display_order())
order2 = Order(2,"nisrina",date.fromisoformat('2023-12-04'), 20000)
order2.calculate_tax(2000)
print(order2.display_order())
order3 = Order(3,"septiana",date.fromisoformat('2024-12-04'), 30000)
order3.calculate_tax(3000)
print(order3.display_order())
# fill Order to OrderProcessor
orders = OrderProcessor()
orders.add_order(order1)
orders.add_order(order2)
orders.add_order(order3)
# display Orders details
orders.calculate_total_tax()
orders.calculate_total_revenue()
orders.display_orders()


