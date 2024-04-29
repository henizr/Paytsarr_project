import screen_brightness_control as sbc


class ScreenBrightnessControl:
    
    @staticmethod
    def get_current_brightness():
        return sbc.get_brightness()