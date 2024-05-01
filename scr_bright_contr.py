import screen_brightness_control as sbc  


class ScreenBrightnessControl:
    OFFSET = 1
    @staticmethod
    def get_current_brightness():
        return sbc.get_brightness()[0]

    @staticmethod
    def increase_brightness():
        current_brightness = ScreenBrightnessControl.get_current_brightness()
        if (current_brightness + ScreenBrightnessControl.OFFSET) > 100: return
        sbc.set_brightness(current_brightness + ScreenBrightnessControl.OFFSET) 

    @staticmethod
    def decrease():
        current_brightness = ScreenBrightnessControl.get_current_brightness()
        if current_brightness < ScreenBrightnessControl.OFFSET : return
        sbc.set_brightness(current_brightness - ScreenBrightnessControl.OFFSET) 

    @staticmethod
    def set_brightness_to_zero():
        sbc.set_brightness(0)

    @staticmethod
    def set_brightness_to_specific_percent(percent: int):
        sbc.set_brightness(percent)




if __name__ == "__main__":
    while True:
        print(ScreenBrightnessControl.get_current_brightness())
        answer = input("0: decrease to zero\n1: increase\n2: decrease\n")
        if answer == "1":
            ScreenBrightnessControl.increase_brightness()
        elif answer == "2":
            ScreenBrightnessControl.decrease()
        elif answer == "0":
            ScreenBrightnessControl.set_brightness_to_zero()

        print("\n")
        print(ScreenBrightnessControl.get_current_brightness())
        print("\n")

