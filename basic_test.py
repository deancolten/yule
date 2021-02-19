from yule import YuleLogger
from dotenv import load_dotenv
import os

load_dotenv()

GM_LOGIN = os.environ.get("GM_LOGIN")
GM_PASS = os.environ.get("GM_PASS")

l1 = YuleLogger(level=0,
                file_path="/dev/yule/yule",
                to_file=True,
                id="BasicTestLog"
                )

l1.clear_log_file()

l1.debug("debug test")
l1.info("info test")
l1.warning("warning test")
l1.error("error test")

l1.debug(100)
l1.info(0 < 1)
l1.warning(l1)
l1.error(False)

l1.set_syntax("Syntax Test")
l1.debug("debug test")
l1.info("info test")
l1.warning("warning test")
l1.error("error test")

l1.set_syntax(None)
l1.error("Syntax Change Test")

l1.setup_gmail(GM_LOGIN, GM_PASS)
l1.send_gmail(
    "Basic Test",
    "Content is here",
    "coltenrdean@gmail.com"
)
