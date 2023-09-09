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
    balld = [1, 1] # 方向は英語で Direction
    v = 1/1000
    ballv = [balld[0]*v, balld[1]*v] # 速度は英語で Velocity
    gameover = False

    # ボタンAかBが押されたらスタートする
    while not button_a.was_pressed() and not button_b.was_pressed():
        pass
    # 3,2,1,GOの合図でスタートする
    display.show("3", 1000)
    display.show("2", 1000)
    display.show("1", 1000)
    
    while not gameover:
        
        # ボールの描画位置を更新する
        ballx += ballv[0]
        bally += ballv[1]
        
        # ボールとバーの表示をする
        display.clear()
        display.set_pixel(int(ballx), int(bally), 9)
        display.set_pixel(barx[0], 4, 9)
        display.set_pixel(barx[1], 4, 9)
    
        if button_a.was_pressed():
            barx[0] -= 1
            barx[1] -= 1
        elif button_b.was_pressed():
            barx[0] += 1
            barx[1] += 1
        else:
            pass # ボタンが押されなければ何もしない
        
        # バーのx座標が0より小さくなったり、4より大きくなったりしないようにする
        # 境界条件と言われるやつ
        if barx[0] < 0: # 左端に来た時の処理
            barx[0] = 0
            barx[1] = 1
        elif barx[1] > 4: # 右端に来た時の処理
            barx[0] = 3
            barx[1] = 4
        
        # # ボールの進む向き（速度）が変わるようにする
        if ballx <= 0 and balld[0] < 0: # ① 左端 (x=0)
            balld[0] = 1
        if ballx >= 4 and balld[0] > 0: # ② 右端 (x=4)
            balld[0] = -1
        if bally <= 0 and balld[1] < 0: # ③ 天井 (y=0)
            balld[1] = 1
        if bally >= 4 and balld[1] > 0: # ④ 底 (y=4)
            balld[1] = -1
        
        # ボールの進む向き、速さをもとにボールの速度を更新する
        # v = 1/1000
        ballv = [balld[0]*v, balld[1]*v] # 速度は英語で Velocity