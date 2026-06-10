me = {
      "height": "157",
      "fav_color": "green",
      "fav_author": "西尾維新"
      }

answer = input("Type height, fav_color or fav_author:")
if answer in  me:
    result =  me[answer]
    print(result)
