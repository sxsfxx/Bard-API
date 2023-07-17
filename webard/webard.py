from bardapi import Bard

token = 'YwgC030KE0JFi41YY9iqOJ44y6uuKjZSQz6g8FEFMKmIY8SicAYQBLAlMv-A4yD6RjE23A.'
bard = Bard(token=token)
s = bard.get_answer("请告诉我世界上最高的山峰是哪一个？")['content']
print(s)
