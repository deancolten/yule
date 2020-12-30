from yule.yule import YuleLogger

l1 = YuleLogger(id="Log 1")
l1.set_level('error')





l1.info("This is info")
l1.warning("This is a warning")
l1.error("An Error occured")