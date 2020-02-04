# Android Auto Message Bot :robot:

Automated Android text messaging bot that uses android web messaging feature to send automated reply messages to multiple contacts for a particular interval.

## Installation

```
git clone https://github.com/adithyan-ak/AndroidAutoMessageBot
```

## Recommended Python Version:

The Bot supports **Python 3**.

* The recommended version for Python 3 is **3.8.x**

## Dependencies:

The Bot depends on the `Selenium`and `Chatterbot` python modules.

#### Selenium Module (https://selenium-python.readthedocs.io/)

- Install for Windows:
```
C:\python37\python3.exe -m pip install selenium
```

- Install using pip on Linux:
```
sudo pip3 install selenium
```
## Setup:

Edit the **Automessage.py** file according to your needs. 

Add the contact names to whom you wish to send the message in ```names```(Tuple) variable of **Line 10**.

Add the Message which you wish to send to the selected contacts in ```Message``` variable of **Line 12**.

Edit the **AutoChat.py** file according to your needs.

Change the contact name with whom you want the Chatbot to reply automatically in ```Contact``` variable of **Line 8**.


## Execution:

To send a particular message to selected contacts automatically, run the **AutoMessage.py** file.

```
python3 AutoMessage.py
```

To send automatically chat to a contact, run the **AutoChat.py** file.

```
python3 AutoChat.py
```

## License

AndroidMessageBot is licensed under the GNU GPL license. take a look at the [LICENSE](https://github.com/adithyan-ak/AndroidMessageBot/blob/master/LICENSE) for more information.


## Version
**Current version is 1.0**

