# Yule
A python logger


## Install
'''
pip install yule
'''

## Example

'''python
from yule.yulelog import YuleLogger

logger = YuleLogger(level=2,
                file_path="LOG FILE PATH HERE",
                to_file=false,
                id="BasicTestLog"
                )

logger.info("This is info")
logger.warning("This is a warning")
logger.error("This is an error")
'''