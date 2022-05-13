# Python on Replit

This is a template to get you started with Python on Replit. It's ready to go so you can just hit run and start coding!

## Running the repl

Simply hit run! You can edit the run command from the `.replit` file.

## Installing packages

To add packages to your repl, you can just import directly in the file you want to use the package in, and it will automatically be installed when you press the run button. Like below:
```python
import math
import pandas as pd
from flask import Flask
```

You could also install packages by using the Replit packager interface in the left sidebar.

## Help

If you need help you might be able to find an answer on our [docs](https://docs.replit.com) page. Feel free to report bugs and give us feedback [here](https://replit.com/support).

##Functionality covered:

1. Create inventory items
2. Edit Them
3. Delete Them
4. View a list of them
5. When deleting, allow deletion comments and undeletion

Create:
If the item exists the application will ask to update the quantity rather adding the same item. its case sensitive.

If the element does not exists it would go ahead and add to the database.

Edit:
If the element is present in the system it would edit the quantity of the element.

If the element does not exists the system will take you back to edit option.


Delete:
If the element exists it would delete the element and you can add comment you can check that in deleted item table.

after deleting it would ask whether you want to undelete the transaction.
if you click on undelete it would undelete the item.


If the element does not exist it would ask to check the view and delete correct element.


View:
There are two fields to store information regarding the our inventory i.e Name and Quantity.

Delete Entire Database: it would wipe the entire data.

Note: The system is case sensitive.





