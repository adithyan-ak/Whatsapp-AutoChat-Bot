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

    driver.find_element_by_xpath("//input[@value='']").click()
    driver.find_element_by_xpath("//div[@id='side']/div/div/label/input").clear()
    driver.find_element_by_xpath("//div[@id='side']/div/div/label/input").send_keys("Cute Camillus") #Type contact name
    time.sleep(7)
    driver.find_element_by_xpath("//div[2]/div[2]/div/span/span").click() #Click open chat name
    time.sleep(5)

    lastmessage = driver.find_elements_by_xpath("//div[@class='FTBzM message-in']")
    range = len(lastmessage)
    last = lastmessage[range-1]
    lsmsg = last.text
    finalmsg = stripper(lsmsg)
    firstfinal = finalmsg #Alternate variable #How are you

    Message = str(getQuery(finalmsg))

    #con.clear()
    con = driver.find_element_by_xpath("//div[@id='main']/footer/div/div[2]/div/div[2]") #Find the reply box
    con.click() #Click the reply box
    con.send_keys(Message) #type in the reply box
    con.send_keys(Keys.RETURN) #hit enter

    count = 0

    while(True):


        lastmessage = driver.find_elements_by_xpath("//div[@class='FTBzM message-in']")
        range = len(lastmessage)
        last = lastmessage[range - 1]
        lastprevious = lastmessage[range-2]
        lprevious = lastprevious.text
        lprevious = stripper(lprevious)
        lsmsg = last.text
        finalmsg = stripper(lsmsg)


        if finalmsg != lprevious:
            count = 0

        if finalmsg != firstfinal: #Comparing with first alternate variable

            Message = str(getQuery(finalmsg))

            time.sleep(3)
            # con.clear()
            con = driver.find_element_by_xpath("//div[@id='main']/footer/div/div[2]/div/div[2]")  # Find the reply box
            con.click()  # Click the reply box
            con.send_keys(Message)  # type in the reply box
            con.send_keys(Keys.RETURN)  # hit enter

            firstfinal = finalmsg

        elif finalmsg == lprevious and count == 0:

            Message = str(getQuery(finalmsg))
            time.sleep(3)
            # con.clear()
            con = driver.find_element_by_xpath("//div[@id='main']/footer/div/div[2]/div/div[2]")  # Find the reply box
            con.click()  # Click the reply box
            con.send_keys(Message)  # type in the reply box
            con.send_keys(Keys.RETURN)
            count = count+1


        time.sleep(3)

def stripper(s):
    return s[:s.rfind('\n')]

def getQuery(query):
    try:
        user_input = query

        bot_response = bot.get_response(user_input)

        return bot_response

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        pass



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
