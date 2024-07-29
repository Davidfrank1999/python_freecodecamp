class Category:
    def __init__(self,category) -> None:
        self.ledger =[]
        self.category=category
        """ self.balance=0
        self.all_deposit=0
        self.get_balance()
        self.total_deposit() """
        
    def __str__(self) -> str:
       
        title = f"{self.category:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total
        
    def deposit(self,amount,description=""):
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self,amount,description=""):
        if self.check_funds(amount):# checking balance
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
        
        
    def get_balance(self):
        cat_balance=0
        for i in range(len(self.ledger)):
            cat_balance +=self.ledger[i]["amount"]
        #self.balance=cat_balance
        return cat_balance
    
    
    def transfer(self,amount,to_category):
        if self.check_funds(amount):# checking balance
            self.withdraw(amount,f'Transfer to {to_category.category}')
            to_category.deposit(amount,f'Transfer from {self.category}')
            return True
        else:
            return False
        
    def check_funds(self,amount):
        if self.get_balance()< amount:
            return False
        else:
            return True
        
    def total_deposit(self):
        total_deposit=0
        for item in (self.ledger):
            if item["amount"] > 0:
                total_deposit +=item["amount"]
        #self.all_deposit=total_deposit
        return total_deposit

    def total_spent(self):
        return sum(-item["amount"] for item in self.ledger if item["amount"] < 0)
        

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    
    total_spent = sum(category.total_spent() for category in categories)
    category_percentage = [(category.total_spent() / total_spent) * 100 for category in categories]
    
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percentage in category_percentage:
            chart += " o " if percentage >= i else "   "
        chart += " \n"
    
    chart += "    -" + "---" * len(categories) + "\n"
    
    max_len = max(len(category.category) for category in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            chart += f"{category.category[i]}  " if i < len(category.category) else "   "
        chart += " \n"

    print(chart)
    
        
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)

#------------------------------------------------------------------------------------

def create_spend_chart(categories):
  # Calculate spending percentages
  total_spent = sum(category.total_spent() for category in categories)
  category_percentage = [(category.total_spent() / total_spent) * 100 for category in categories]
 

  chart = "Percentage spent by category"
  for i in range(100, -1, -10):
    chart += "\n" + str(i).rjust(3) + "|"
    for category in category_percentage:
      if category > i:
        chart += " o "
      else:
        chart += "   "
    # Spaces
    chart += " "
  chart += "\n    ----------"

  cat_length = []
  for category in categories:
    cat_length.append(len(category.category))
  max_length = max(cat_length)

  for i in range(max_length):
    chart += "\n    "
    for j in range(len(categories)):
      if i < cat_length[j]:
        chart += " " + categories[j].category[i] + " "
      else:
        chart += "   "
    # Spaces
    chart += " "

  return chart

''' food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
#print(food)

print(create_spend_chart([food,clothing])) '''