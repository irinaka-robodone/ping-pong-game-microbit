from microbit import *
import random

"""
1. ボタン(AでもBでもOK)を押したらスタートする
2. 3,2,1,GOの合図でスタート
3. GameOver(ボールが床に触れたとき)になるまで4~6を繰り返す
4. バー(ライト2つ分)をボタンAで左、ボタンBで右に動かす
5. ボールをxを1~3、yを1からスタートして一定方向(ランダム)に動かす。
6. 壁と天井にふれたときに鏡に光が当たった時のように跳ね返らせる。
7. GameOverになったら続けられた時間を10で割ってスコアを表示させる
"""

while True:
    
    # ゲームのステート初期化
    ballx = 2
    bally = 0
    barx = (2,3)
    ballv = [1, 1] # 速度は英語で Velocity
    gameover = False

    # ボタンAかBが押されたらスタートする
    while not button_a.was_pressed() and not button_b.was_pressed():
        pass
    # 3,2,1,GOの合図でスタートする
    display.show("3", 1000)
    display.show("2", 1000)
    display.show("1", 1000)
    
    while not gameover:
        
        # ボールとバーの表示をする
        display.clear()
        display.set_pixel(ballx, bally, 9)
        display.set_pixel(barx[0], 4, 9)
        display.set_pixel(barx[1], 4, 9)
    
        # if button_a.was_pressed():
        #     barx[0] -= 1
        #     barx[1] -= 1
        # elif button_b.was_pressed():
        #     barx[0] += 1
        #     barx[1] += 1
        # else:
        #     pass # ボタンが押されなければ何もしない
        
        # # バーのx座標が0より小さくなったり、4より大きくなったりしないようにする
        # # 境界条件と言われるやつ
        # if barx[0] < 0: # 
        #     barx[0] = 0
        #     barx[1] = 1
        # elif barx[1] > 4:
        #     barx[0] = 3
        #     barx[1] = 4
        
        # # ボールの進む向き（速度）が変わるようにする
        # if ballx == 0 and ballv[0] < 0:
        #     ballv[0] = 1
        # elif ballx == 4 and ballv[0] > 0:
        #     ballv[0] = -1
        # if bally == 0 and ballv[1] < 0:
        #     ballv[1] = 1
        # if ballx in barx and bally == 3 and ballv[1] < 0:
        #     ballv[1] = -1
        
        # # ボールの座標を速度で更新する
        # ballx += int(ballv[0]* 0.001)
        # bally += int(ballv[1] * 0.001)