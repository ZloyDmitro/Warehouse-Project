warehouse1 = ["Brand new laptop", "Exceptional monitor", "Cheap tablet", "Funny laptop", "Second hand smartphone", "Brand new smartphone", "Cheap router", "Second hand laptop", "Elegant tablet", "Funny tablet", "Second hand headphones", "Exceptional tablet", "Brand new smartphone", "Cheap mouse", "Elegant headphones", "Brand new headphones", "Second hand smartphone", "High quality smartphone", "Brand new keyboard", "Second hand headphones", "Elegant router", "Exceptional router", "Second hand smartphone", "Exceptional monitor", "Almost new tablet", "High quality monitor", "Second hand monitor", "Brand new keyboard", "Almost new keyboard", "High quality headphones", "Elegant laptop", "Elegant router", "Almost new monitor", "Almost new headphones", "Second hand keyboard", "Brand new tablet", "Elegant laptop", "Almost new keyboard", "Exceptional router", "High quality keyboard", "Exceptional router", "Elegant router", "Cheap keyboard", "High quality monitor", "High quality keyboard", "Funny keyboard", "Cheap mouse", "Cheap monitor", "Funny headphones", "Elegant mouse", "Cheap smartphone", "High quality mouse", "Funny keyboard", "Second hand monitor", "Almost new router", "Almost new mouse", "Elegant smartphone", "Second hand router", "Second hand mouse", "Second hand tablet", "Exceptional tablet", "High quality smartphone", "Brand new headphones", "Exceptional monitor", "Elegant mouse", "Cheap laptop", "High quality smartphone", "Cheap monitor", "Funny monitor", "Almost new mouse", "Elegant headphones", "Cheap mouse", "Exceptional smartphone", "Cheap monitor", "Exceptional tablet", "Almost new tablet", "Second hand headphones", "Cheap tablet", "Elegant mouse", "Second hand mouse", "Cheap laptop", "Cheap keyboard", "Elegant router", "Elegant headphones", "Second hand monitor", "Funny router", "Elegant mouse", "Elegant headphones", "Brand new mouse", "Exceptional tablet", "Funny router", "Second hand headphones", "Brand new laptop", "Second hand router", "Cheap mouse", "Funny keyboard", "Elegant headphones", "Brand new laptop", "Elegant laptop", "Second hand mouse"]
warehouse2 = ["High quality tablet", "Second hand headphones", "Second hand laptop", "Exceptional tablet", "Exceptional headphones", "Brand new smartphone", "Elegant laptop", "High quality tablet", "Brand new headphones", "Exceptional mouse", "Cheap mouse", "Cheap headphones", "High quality headphones", "Brand new keyboard", "Brand new smartphone", "Almost new mouse", "Second hand router", "High quality monitor", "High quality smartphone", "Second hand headphones", "Elegant monitor", "High quality mouse", "Almost new keyboard", "Exceptional headphones", "High quality smartphone", "Exceptional smartphone", "High quality tablet", "Cheap mouse", "Cheap monitor", "Funny monitor", "Elegant monitor", "Funny smartphone", "Second hand mouse", "Almost new headphones", "Cheap headphones", "High quality router", "Exceptional keyboard", "Funny keyboard", "Exceptional laptop", "Cheap keyboard", "Second hand mouse", "Elegant router", "Cheap router", "Funny mouse", "Funny laptop", "Elegant tablet", "Exceptional mouse", "Funny headphones", "Elegant tablet", "Second hand laptop", "Brand new headphones", "Second hand headphones", "Cheap router", "Exceptional mouse", "Elegant router", "Exceptional monitor", "Exceptional keyboard", "Funny headphones", "Second hand headphones", "Almost new router", "Brand new tablet", "Funny mouse", "Elegant mouse", "High quality router", "Second hand keyboard", "Second hand router", "Brand new monitor", "Funny mouse", "Funny tablet", "Elegant keyboard", "Cheap router", "Funny router", "Second hand monitor", "Elegant smartphone", "Brand new monitor", "Second hand monitor", "Second hand keyboard", "Cheap mouse", "Brand new keyboard", "Exceptional mouse", "Elegant router", "Brand new mouse", "Exceptional keyboard", "Elegant smartphone", "Exceptional tablet", "Second hand keyboard", "Almost new headphones", "Brand new tablet", "Brand new tablet", "Exceptional headphones", "Funny smartphone", "Funny smartphone", "Second hand tablet", "Cheap router", "Almost new keyboard", "Elegant router", "Brand new tablet", "High quality tablet", "Almost new router", "High quality monitor"]


class Item:
    def __init__(self, item_id, name, quantity):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity

class Warehouse:
    def __init__(self, warehouse_id):
        self.id = warehouse_id
        self.stock = [] 

    @property
    def occupancy(self):
        return len(self.stock)

    def add_item(self, item_name):
        for i, stock_item in enumerate(self.stock):
            if stock_item["name"] == item_name:
                self.stock[i]["quantity"] += 1
                break
        else:
            self.stock.append({"name": item_name, "quantity": 1})
    
class Stock:
    def __init__(self):
        self.warehouses = []  # Initialize as an empty list

    def add_warehouse(self, warehouse):
        self.warehouses.append(warehouse)

    def find_warehouse_by_id(self, warehouse_id):
        for warehouse in self.warehouses:
            if warehouse.id == warehouse_id:
                return warehouse
        return None
    
    
    def remove_item():
        pass
    
    def search(self, search_term):
        found_items = [item for item in self.stock if search_term.lower() in item["name"].lower()]
        return found_items
    
warehouse1 = Warehouse(1)
warehouse2 = Warehouse(2)
stock = Stock()

stock.add_warehouse(warehouse1)
stock.add_warehouse(warehouse2)

# found_warehouse = stock.find_warehouse_by_id(1)
# if found_warehouse:
#     print(f"Found warehouse with ID 1: {found_warehouse}")
# else:
#     print("Warehouse not found.")
print(Stock.search(1, "Brand new laptop"))

class Employee:
    def __init__(self) -> None:
        pass
