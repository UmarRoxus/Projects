import winsound, keyboard, time, sys



while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
        
            time.sleep(1.5)
            print('No Jump!')
            winsound.PlaySound("buzzer_x.wav", winsound.SND_ASYNC)
        
            continue
    except:
        break  # if user pressed a key other than the given key the loop will break
 
input("")
