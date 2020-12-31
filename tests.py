from yule.yule import YuleLogger

l1 = YuleLogger(id="Yule")
l1.set_level('info')


l1.info("This is info")
l1.warning("This is a warning")
l1.warning("This is a warning")
l1.error("An Error occured")
