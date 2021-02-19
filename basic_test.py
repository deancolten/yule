from yule import *
l1 = YuleLogger(level=2,
                file_path="/dev/yule/yule",
                to_file=True,
                id="BasicTestLog"
                )
l1.set_level(Level.debug)


def add_one(number):
    l1.info(f"Add One before number - {number}")
    number += 1
    l1.warning(f"Add One after number - {number}")
    return number


def double_number(number):
    for _ in range(0, 12):
        l1.info(f"Double before number - {number}")
        try:
            number = int(number) * 2
            l1.warning(f"Double after number - {number}")
        except:
            l1.error("Function Double requires type int")
    return number


x = 10
y = 2
z = 100

l1.set_syntax('%D@%T|%N - %L: %M')
l1.clear_log_file()
l1.error("CRITICAL")
l1.warning("CRITICAL")
l1.info("CRITICAL")
l1.debug(1.289)
