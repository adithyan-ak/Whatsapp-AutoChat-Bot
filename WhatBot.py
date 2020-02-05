from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chatterbot import ChatBot
import time


def Main():
    driver = webdriver.Firefox()
    driver.get("https://web.whatsapp.com/")

    input("Press anything after QR scan")
    time.sleep(5)

    ContactName = 'Baddy'  # Enter the contact names

    Message = "Android Auto Messaging Bot Here!"  # Enter the Message

    try:

        driver.find_element_by_xpath("//input[@value='']").click()  # Click on search button
        driver.find_element_by_xpath("//div[@id='side']/div/div/label/input").clear()
        driver.find_element_by_xpath("//div[@id='side']/div/div/label/input").send_keys(
            ContactName)  # Type contact name
        time.sleep(5)
        driver.find_element_by_xpath("//div[2]/div[2]/div/span/span").click()  # Click open chat name
        time.sleep(5)

        lastmessage = driver.find_elements_by_xpath("//div[@class='FTBzM message-in']")
        range = len(lastmessage)
        last = lastmessage[range - 1]
        lsmsg = last.text
        finalmsg = stripper(lsmsg)
        firstfinal = finalmsg  # First received message

        Message = str(getQuery(finalmsg))

        # con.clear()
        con = driver.find_element_by_xpath("//div[@id='main']/footer/div/div[2]/div/div[2]")  # Find the reply box
        con.click()  # Click the reply box
        con.send_keys(Message)  # type in the reply box
        con.send_keys(Keys.RETURN)  # hit enter

        count = 0  # Initial count set to 0

        while True:

            lastmessage = driver.find_elements_by_xpath(
                "//div[@class='FTBzM message-in']")  # Selenium element for accessing all received messages
            range = len(lastmessage)  # Total length of Messages on page
            last = lastmessage[range - 1]  # Selenium element for last message
            lsmsg = last.text  # last message with date in last line
            finalmsg = stripper(lsmsg)  # Last message
            lastprevious = lastmessage[range - 2]  # Selenium element for last previous message
            lprevious = lastprevious.text  # last previous message with date in last line
            lprevious = stripper(lprevious)  # Last previous message

            if finalmsg != lprevious:  # if Last message is not equal to Last previous message

                count = 0  # Count is reset to 0 to prevent repeated execution

            if finalmsg != firstfinal:  # If Last message is not equal to first received message

                Message = str(getQuery(finalmsg))  # Get result for last message from Chatbot

                time.sleep(3)
                # con.clear()
                con = driver.find_element_by_xpath(
                    "//div[@id='main']/footer/div/div[2]/div/div[2]")  # Find the reply box
                con.click()  # Click the reply box
                con.send_keys(Message)  # type in the reply box
                con.send_keys(Keys.RETURN)  # hit enter

                firstfinal = finalmsg  # Re-writing the first received message with next received message

            elif finalmsg == lprevious and count == 0:  # Checking whether the last message and previous message are
                # same and count is 0

                Message = str(getQuery(finalmsg))  # Get result for last message from Chatbot
                time.sleep(3)
                # con.clear()
                con = driver.find_element_by_xpath(
                    "//div[@id='main']/footer/div/div[2]/div/div[2]")  # Find the reply box
                con.click()  # Click the reply box
                con.send_keys(Message)  # type in the reply box
                con.send_keys(Keys.RETURN)  # press enter
                count = count + 1  # Incrementing the count to prevent repeated execution

    except Exception as e:
        print("Exception Occured")
        print(e)


def stripper(s):  # Stripper function for removing last line

    try:
        return s[:s.rfind('\n')]  # Return the message after removing last line

    except Exception as e:
        print("Exception occured")
        print(e)


def getQuery(query):
    try:
        user_input = query

        bot_response = bot.get_response(user_input)

        return bot_response

    # Press ctrl-c or ctrl-d on the keyboard to exit
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
