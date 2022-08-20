

import time

from plyer import notification

if __name__ == "__main__":

    while True:

        notification.notify(
            title="Coders Unite. Together We Rise.",
            message="“Code is like humor. When you have to explain it, it’s bad.” – Cory House",
            app_icon=r"C:\Powershell\DATABASE\PROJECTS\ASSESTS\Icon.ico.ico",
            timeout=10
        )
        time.sleep(60)
