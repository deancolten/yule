from os import path


class LogFile():
    """Class to handle writing and reading from log files"""

    def __init__(self, name, location):
        self.location = location
        self.name = name

        self.file_path = f"{location}/{name}.log"

    def create_file(self):
        """Create the log file on init"""

        if not path.exists(self.file_path):
            with open(self.file_path, 'w') as _:
                pass

    def record_entry(self, entry):
        """Record entry to log file"""

        with open(self.file_path, 'a') as f:
            f.write(entry + '\n')

    def clear_file(self):
        with open(self.file_path, 'w') as _:
            pass
