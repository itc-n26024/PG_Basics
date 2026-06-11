me = {
      "height": "157",
      "fav_color": "green",
      "fav_author": "西尾維新"
      }

ask = input("知りたい特徴を入力してね :")
if ask in  me:
    answer =  me[ask]
    print(answer)
else:
    print("それはわからないよ。めんご")
