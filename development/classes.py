
   class Mario:

       _Lives = 3
       _speed = 30.0

       def test(self):
           print("hallo")
           print("speed is", self_speed)
    
    instenceMario = mario()
    nogEenMario = Mario()

    print( instanceMario )
    instenceMario.test()
    instenceMario._speed = 50.5

    print("instenceMario speed", instenceMario._speed)
    print("nogEenMario speed", nogEenMario._speed)
    