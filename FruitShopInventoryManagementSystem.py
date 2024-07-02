'''Create a dictionary-based mini project in Python to manage an inventory in stock. 
The user should have options to add new items, buy items, change the price of items, 
and update the inventory of current items. There should also be a total sales variable that is 
initially set to 0. The project should handle inventory, price, and count. 
The project should be broken down into steps with clear instructions for each step. 
Each step should be pushed to GitHub.'''
'''1. Create a new GitHub repository and set up a new Python project.

2. Define the inventory dictionary to hold item data and a variable for total sales.

3. Create a `main` function to run the program and print a welcome message.

4. Create a function `add_item` to add new items to the inventory with a
 specified name, price, and count.

5. Update the `main` function to include a menu option for adding new items.

6. Commit the changes to GitHub.
7. Create a function `buy_item` to handle buying items from the inventory, updating the 
item count and total sales.

8. Update the `main` function to include a menu option for buying items.
9. Commit the changes to GitHub.

10. Create a function `change_price
    ` to update the price of an existing item in the inventory.

11. Update the `main` function to include a menu option for changing item prices.
12. Commit the changes to GitHub.

13. Create a function `display_inventory` to print the current state of the inventory and 
total sales.

14. Update the `main` function to include a menu option for displaying the inventory.

15. Commit the changes to GitHub.

16. Create a function `update_inventory` to update the count of an existing item in the inventory.

17. Update the `main` function to include a menu option for updating the inventory 
count of existing items.

18. Commit the changes to GitHub.

19. Review and refactor the code if necessary. Add comments and documentation
 to explain the functionality.

20. Add a final commit to GitHub with any refinements and the completed project.'''


total_sales = 0

invent={
    "Apple":    {"Price":150, "Count":100},   #[price,count]
    "Banana":   {"Price":180.30, "Count":150},
    "Orange":   {"Price":90.60, "Count": 80},
    "Pear":     {"Price":100, "Count": 50},
    "Apricot":  {"Price":55, "Count": 230},
    "Dates":    {"Price":670, "Count": 450},
    "Plum":     {"Price":120, "Count": 33},
    "Fig":      {"Price":98.76, "Count": 10},
    "Coconut":  {"Price":100, "Count": 10}
}
 

def main():
    print('\033[1mWelcome to the Fruit Shop Inventory Management System\033[0m')
    print()

    def add_item():
        #{newITEM : {price: xxx , count : xxx}}
        KEYS=list(invent.keys())
        new_item =input("Please write the new item you would like to add to the inventory.  ")
        while(True):
            ni=new_item.title()
            if ni in KEYS:
                print(f'{ni} already exists in the inventory')
                new_item =input("Please Re-write the new item you would like to add to the inventory.  ") 
                continue         
            else:
                break


        pri=float(input("Enter new item's price: "))
        coun=int(input("Enter new item's count: "))
                                            # Method 1
        
        # d={}                   
        # d["Price"]=pri
        # d["Count"]=coun
        # invent[ni]=d
                                            # Method 2

        invent[ni]={"Price":pri, "Count":coun}
        print()
        return print(f'{ni} has been added to the Inventory successfully.')

    def buy_item():
        global total_sales
        x=input('Please write what iten you are looking for ')
        x=x.title()
        ditkey=list(invent.keys()) 
        ditskey=[]
        for i in ditkey:
            i=i.title()
            ditskey.append(i)

        
        while(x not in ditskey):
            print('This Item not available!')
            j=input(('Enter "exit" or to rewrite, press "Enter":  '))
            j=j.lower()
            if (j=="exit"):
                print('Ok bye!')
                exit()
            else:
                x=input('Again tell what you want to get: ')
                x=x.title()
                
        if (x=="Banana"or x=="Orange"):
            r=int(input('Please enter quantity in Dozen: '))
        else:
            r=int(input('Please enter quantity of KGs: '))

        item_price=invent[x]['Price']
        y=invent[x]["Count"]
        gen_sales= item_price * r
        
        while(r>=y):
            print('This much stock is not available.')
            print('Please try with lower quantity')
            print()

            p=input(('Enter "exit" or to continue press "Enter":  '))
            p=p.lower()
            if (p=="exit"):
                print('Ok bye!')
                exit()
            else:        
                r=int(input('Again enter quantity of item: '))
                continue

        else:
            print()
            print(f'The total is {round(gen_sales)}')
            print(f'{x.capitalize()} bought succesfully!')
            
            print()
            total_sales=total_sales + gen_sales
            y-=r
            r= {'Count': y}
            invent[x].update(r)
            return print('Thanks for your purchase')
        
    def change_price():

        x=input('Please write the name of item you want to update the price   ')
        x=x.title()
        ditkey=list(invent.keys())
        ditskey=[]
        for i in ditkey:
            i=i.title()
            ditskey.append(i)
        
        
        while(x not in ditkey):
            print('Unable to find this item')
            j=input(('To continue, press "Enter" to rewrite or you can write "exit" to skip:  '))
            j=j.lower()
            if (j=="exit"):
                print('Thanks for your time !')
                exit()
            else:
                x=input('Please write the correct item')
                x=x.title()
        a=invent[x]['Price']
        print('Current price is ',a)
        upd_pri=float(input('New Updated price : '))
        q={"Price":upd_pri}
        invent[x].update(q)

        return print(f'The price of {x} has been updated succesfully')
    
    def update_inventory():
        x=input('Please write the name of item in order to update the stock :  ')
        x=x.title()
        ditkey=list(invent.keys()) 
        ditskey=[]
        for i in ditkey:
            i=i.title()
            ditskey.append(i)
        
        
        while(x not in ditkey):
            print('Unable to find this item')
            j=input(('To continue, press "Enter" to rewrite or you can write "exit" to skip:  '))
            j=j.lower()
            if (j=="exit"):
                print('Thanks for your time !')
                exit()
            else:
                x=input('Please write the correct item ')
                x=x.title()
        a=invent[x]['Count']
        print('Current Count of',x, 'is',a)
        upd_count=int(input('New Updated Count : '))
        
        q={"Count":upd_count}
        invent[x].update(q)

        return print(f'The count of {x} has been updated succesfully')
    

    def display_inventory():
        dikeys=list(invent.keys())

        from prettytable import PrettyTable
        table = PrettyTable()
        table.field_names = ["Name", "Price", "Count"]  # Add columns

        for i in dikeys:
            g=invent[i]['Price']
            h=invent[i]['Count']

            # Add rows
            table.add_row([i, g, h])

        return print(table,"\n","Total Sales : ",total_sales)

    print('\033[1mWelcome to the Fruit Shop Inventory Management System\033[0m')
    print()

    print('➡️',' If you like to add a new item to the inventory. Press "1"')
    print('➡️',' To make a purchase from the inventory. Press "2"')
    print('➡️',' Want to adjust the price of an existing item. Press "3"')
    print('➡️',' If you like to update the stock count for an item. Press "4"')
    print()
    print('➡️',' To see your current Inventory Stock. Press "5"')
    print('➡️',' In order to exit. Press "6"')
    while(True):
        try:
            customer_select=int(input('Please tell us what would you like to do '))
            print()
            if customer_select==1:
                add_item()
            if customer_select==2:
                buy_item()
            if customer_select==3:
                change_price()
            if customer_select==4:
                update_inventory()
            if customer_select==5:
                display_inventory()
            if customer_select==6:
                print('\033[1mTHANKS FOR CHOOSING OUR SHOP\033[0m')
                print('\033[1mGood Bye !\033[0m')
                exit()
           
        except ValueError:
            print("Input does not seems like number. Please enter number from 1 to 5.")
            z=input('If you want to exit please write "exit" or to continue press "enter" button ')
            z=z.lower()
            if (z=="exit"):
                exit()
            else:
                print()
                continue
            


    
   


main()

