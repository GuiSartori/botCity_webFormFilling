"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
import pandas as pd

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.EDGE

    # Uncomment to set the WebDriver path
    bot.driver_path = r"C:\Users\guilh\Documents\BotCity\Drivers\msedgedriver.exe"

    # Opens the BotCity website.
    # bot.browse("https://www.botcity.dev")

    # Implement here your logic...
    excel_path = r"C:\Users\guilh\Documents\BotCity\data\Data.xlsx"
    web_form = r"https://docs.google.com/forms/d/e/1FAIpQLSfWBhBnzkAfK3UCrHVG3mCud9e0L4ILu3DCScGLxMjpiP5_xQ/viewform"
    df = pd.read_excel(excel_path)
    bot.browse(web_form)


    for index, row in df.iterrows():

        # xdom_enviar = "//span[text()='Enviar']"
        # xdom_enviar_again = "//a[text()='Enviar outra resposta']"

        name_input_field = bot.find_element("//div[contains(@data-params, 'Name')]//input", By.XPATH)
        name_input_field.send_keys(row["Name"])
        age_input_field = bot.find_element("//div[contains(@data-params, 'Age')]//input", By.XPATH)
        age_input_field.send_keys(row["Age"])
        city_input_field = bot.find_element("//div[contains(@data-params, 'City')]//input", By.XPATH)
        city_input_field.send_keys(row["City"])
        enviar = bot.find_element("//span[text()='Enviar']", By.XPATH)
        enviar.click()
        enviar_outra = bot.find_element("//a[text()='Enviar outra resposta']", By.XPATH)
        enviar_outra.click()


    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
