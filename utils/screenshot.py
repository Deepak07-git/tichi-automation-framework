import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def take_screenshot(driver, name="screenshot"):

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        path = f"screenshots/{name}_{timestamp}.png"

        driver.save_screenshot(path)

        return path