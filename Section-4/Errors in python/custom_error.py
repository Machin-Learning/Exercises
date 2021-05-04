class WidrawLimitOver(Exception):
    def __init__(self,msg):
        self.msg = msg


def widraw(ammount):
    if ammount > 500:
        raise WidrawLimitOver("Your Limit of the day Over")



widraw(600)