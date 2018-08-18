<h1> Quoter</h1><br>
Extracts a random quote from quotes.json and pyQt5 displays it in windows notification bar.<br>

Made it automatically run every 15 minutes in my PC by using Task Sheduler.<br>

In Task Sheduler:<br>
* In General, tick the checkbox- Run with highest provileges.<br>
* In Triggers, set the required settings for you.<br>
* In Actions, set the Program/script to the path of .exe, Add arguments should be name of python script(i.e quoteGenerator.py) and Start in should be location of the python script.<br>
 
.py to .exe made using cx_Freeze.<br>

To create .exe create a setup.py and type: <br>
python setup.py build<br><br>

Enjoy Random Motivational Quotes!<br>

<img src="sc.png">


