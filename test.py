from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chatterbot import ChatBot
import time

def Main():

    driver = webdriver.Firefox()
    driver.get("https://web.whatsapp.com/")

    input("Press anything after QR scan")
    time.sleep(5)

    names = 'Baddy' #Enter the contact names

    Message = "Android Auto Messaging Bot Here!" #Enter the Message

    try:

        driver.find_element_by_xpath("//input[@value='']").click() # Click on search button
        driver.find_element_by_xpath("//div[@id='side']/div/div/label/inpu").clear()
        driver.find_element_by_xpath("//div[@id='side']/div/div/label/inpu").send_keys("Cute Camillus") #Type contact name
        time.sleep(5)
        driver.find_element_by_xpath("//div[2]/div[2]/div/span/span").click() #Click open chat name
        time.sleep(5)

    except IOError as e:
        print("Exception Occured")
        print(e)

    except Exception as e:
        print("Exception occured")
        print(e)


if __name__ == '__main__':

    chatbot = ChatBot('Adithyan AK')

    bot = ChatBot(
        'Default Response Example Bot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch'
            },
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'threshold': 0.90,
                'default_response': 'I am sorry, but I do not understand.'
            }
        ],
        trainer='chatterbot.trainers.ListTrainer'
    )

    Main()
