import json
import os
import sys

class JsonFileHandler:
    def __init__(self, file_path = None):
        self.file_path = file_path

    def load(self) -> list:
        data = []

        if not self.file_path:
            raise Exception("Filename error: File path is not set.")

        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, "r", encoding="utf-8") as f:
                    if os.stat(self.file_path).st_size > 0:
                        data = json.load(f)

            return data

        except json.JSONDecodeError:
            print("Reading JSON file error: The file has not a valid JSON format.")
            sys.exit(1)

    def append(self, *items):     
        pre_formatted_data = self.load()
        pre_formatted_data.extend(items) 

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(pre_formatted_data, f, ensure_ascii=False, indent=4)

    def set_filepath(self, file_path):
        self.file_path = file_path

    def get_filepath(self):
        return self.file_path
    

