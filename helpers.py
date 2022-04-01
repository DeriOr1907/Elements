PLAY_BUTTON_X_POS = 100
PLAY_BUTTON_Y_POS = 100
PLAY_BUTTON_WIDTH = 50
PLAY_BUTTON_HIGHT = 50

TEXT_FONT_SIZE = 15

def mouse_in_button(button, mouse_pos):
    if button.Location[0] + button.width > mouse_pos[0] > button.Location[0] and button.Location[1] < mouse_pos[1] < button.Location[1] + button.height:
        return True
