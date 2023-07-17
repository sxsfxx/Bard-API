from bardapi import Bard

token = 'sidts-CjEBPu3jId5TpMgIrxLRekMb6nVWUuSG4qjU9PdNEi04R7YzdOPaSBpe1bQmu2d78zvTEAA'
bard = Bard(token=token)
bard.get_answer("请告诉我世界上最高的山峰是哪一个？")['content']