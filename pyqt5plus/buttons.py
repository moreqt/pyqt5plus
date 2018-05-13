'''
Created on 13-May-2018

@author: dgraja
'''
from PyQt5 import QtWidgets


class ToggleButton(QtWidgets.QPushButton):
    '''
        A Simple On / Off button which separate text and icon values for on and off states.
        This class extends QPushButton. So use it like a pushbutton, with a simple enhancement
        of two sets of text and icon values.
        checked = True means On state
        checked = False means Off state
        usage:
            self.btn_play = ToggleButton(text_on="Play", icon_on="play.png",
                text_off="Pause", icon_off="pause.png", checked=False, parent=self)
    '''
    def __init__(self, text_on="", icon_on=None, text_off="", icon_off=None, checked=False, parent=None):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setCheckable(True)
        self.toggle_on = True
        self.icon_off = icon_off
        self.text_off = text_off
        self.icon_on = icon_on
        self.text_on = text_on
        self.setChecked(checked)
        self.update_ui(checked)
        self.clicked.connect(self.on_click)
    
    def configure(self, text_on, icon_on, text_off, icon_off, checked=False):
        self.text_on = text_on
        self.text_off = text_off
        self.icon_on = icon_on
        self.icon_off = icon_off
        self.setChecked(checked)
        self.update_ui(checked)

    def update_ui(self, checked=False):
        if checked:
            self.setText(self.text_on)
            if self.icon_on:
                self.setIcon(self.icon_on)
        else:
            self.setText(self.text_off)
            if self.icon_off:
                self.setIcon(self.icon_off)
    
    def on_click(self, checked):
        try:
            self.update_ui(checked)
        except Exception as e:
            print (e)



if __name__ == '__main__':
    pass