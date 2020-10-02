# this is a trivial project, more like its fun.
class Account:
# will do file handling embedded here in this code
    def __init__(self, filepath):
        with open(filepath, 'r')