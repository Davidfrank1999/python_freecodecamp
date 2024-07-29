# Build a Budget App Project
Complete the Category class. 
It should be able to instantiate objects based on different **budget categories** like food, clothing, and entertainment.<br>
When objects are created, they are passed in the name of the category.<br>
The class should have an instance variable called ledger that is a list. The class should also contain the following methods:<br>

4. A deposit method that accepts an amount and description.<br> 4.1 f no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.<br>
5. A withdraw method that is similar to the deposit method, <br>5.1 but the amount passed in should be stored in the ledger as a negative number. <br>5.2 If there are not enough funds, nothing should be added to the ledger. <br>5.3 This method should return True if the withdrawal took place, and False otherwise.
6. A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.<br>
7. A transfer method that accepts an amount and another budget category as arguments. <br> 7.1 The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".<br>7.2 The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".<br>7.3 If there are not enough funds, nothing should be added to either ledgers.<br>7.3 This method should return True if the transfer took place, and False otherwise.<br>

8. A check_funds method that accepts an amount as an argument.<br>8.1 It returns False if the amount is greater than the balance of the budget category and returns True otherwise.<br>8.2 This method should be used by both the withdraw method and transfer method.<br>
9. When the budget object is printed it should display:<br>

A title line of 30 characters where the name of the category is centered in a line of * characters.<br>
A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.<br>
A line displaying the category total.<br>
Here is an example usage:<br>

Example Code<br>
```python
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)
```
And here is an example of the output:
Example Code<br>
```shell
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```
Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.


The chart should show the percentage spent in each category passed in to the function.<br>10.1 The percentage spent should be calculated only with withdrawals and not with deposits.<br>10.2 Down the left side of the chart should be labels 0 - 100.<br>10.3 The "bars" in the bar chart should be made out of the "o" character.<br>10.4 The height of each bar should be rounded down to the nearest 10.<br>10.5 The horizontal line below the bars should go two spaces past the final bar.<br>10.6 Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".<br>

This function will be tested with up to four categories.<br>

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.<br>

Example Code<br>
```shell
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```
Note: open the browser console with F12 to see a more verbose output of the tests.<br>

Test2 
Calling food.deposit(900, "deposit") and food.withdraw(45.67, "milk, cereal, eggs, bacon, bread") should return a balance of 854.33.