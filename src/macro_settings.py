from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QSlider, QLabel, QLineEdit, QPushButton, QDialogButtonBox, QCheckBox
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt
import keyboard
from time import sleep
import logging

logging.basicConfig(
    filename='log.txt', 
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Macro_Settings(QWidget):
    def __init__(self, hotstrings = None, events = None, macro = None):
        super().__init__()
        self.setWindowTitle("Macro settings")
        
        self.hotstrings = hotstrings
        self.events = events
        self.macro = macro
        
        # Main layout
        main_layout = QVBoxLayout(self)
        
        # Playback speed box with Slider and Labels
        self.playback_box = QGroupBox("Playback speed")
        playback_speed_layout = QHBoxLayout()
        self.speed_label_left = QLabel("Speed:")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 35)
        self.slider.setValue(9)
        self.speed_label_right = QLabel()
        self.speed_label_right.setFixedWidth(40)
        
        # Update the right label as the slider moves
        self.slider.valueChanged.connect(self.change_slider)
                
        playback_speed_layout.addWidget(self.speed_label_left)
        playback_speed_layout.addWidget(self.slider)
        playback_speed_layout.addWidget(self.speed_label_right)
        self.playback_box.setLayout(playback_speed_layout)
        
        # Repeat count box with Radio Buttons and QLineEdit
        self.repeat_box = QGroupBox("How many times should the macro play?")
        repeat_layout = QVBoxLayout()
        n_layout = QHBoxLayout()
        inf_layout = QHBoxLayout()
        
        self.radio_once = QRadioButton("Once")
        self.radio_n = QRadioButton("This many times:")
        self.radio_inf = QRadioButton("Until I stop it")
        self.radio_inf.setChecked(True)
        
        self.n_textbox = QLineEdit()
        self.n_textbox.textChanged.connect(self.validate_n)
        self.n = ''
        self.n_textbox.setEnabled(False)

        self.skip_paths_checkbox = QCheckBox('Remove mouse paths')

        self.radio_once.toggled.connect(self.validate_settings)
        # Enable toggle_n_textbox only when radio_n is selected
        self.radio_n.toggled.connect(self.toggle_n_textbox)
        self.radio_n.toggled.connect(self.validate_settings)
        self.radio_inf.toggled.connect(self.validate_settings)
        
        # Arrange radio buttons in group 3
        repeat_layout.addWidget(self.radio_once)
        
        # Place Option B and QLineEdit on the same row
        n_layout.addWidget(self.radio_n)
        n_layout.addWidget(self.n_textbox)
        repeat_layout.addLayout(n_layout)

        inf_layout.addWidget(self.radio_inf)
        inf_layout.addWidget(self.skip_paths_checkbox)
        repeat_layout.addLayout(inf_layout)
        
        self.repeat_box.setLayout(repeat_layout)
        
        # Hotkey box with Label, QLineEdit, and Button
        self.hotkey_box = QGroupBox("Macro hotkey combo")
        hotkey_layout = QHBoxLayout()
        self.hotkey_label = QLabel("Start/stop on this combo:")
        self.hotkey_textbox = QLineEdit()
        self.hotkey_textbox.setEnabled(False)
        self.detect_button = QPushButton("Detect")
        self.detect_button.clicked.connect(self.handle_detect_button)
        
        # Add widgets to new group layout
        hotkey_layout.addWidget(self.hotkey_label)
        hotkey_layout.addWidget(self.hotkey_textbox)
        hotkey_layout.addWidget(self.detect_button)
        self.hotkey_box.setLayout(hotkey_layout)
        
        # OK and Cancel buttons
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.ok)
        self.button_box.button(QDialogButtonBox.Ok).setEnabled(False)
        self.button_box.rejected.connect(self.cancel)
        
        # Add widgets to main layout
        main_layout.addWidget(self.playback_box)
        main_layout.addWidget(self.repeat_box)
        main_layout.addWidget(self.hotkey_box)
        main_layout.addWidget(self.button_box)
        self.setGeometry(100, 100, 1, 1)

        self.change_slider(self.slider.value())

        if self.macro:
            self.set_macro()
    
    def cancel(self):
        """Closes the window without saving anything"""
        self.close()
        del self.hotstrings.settings
    
    def change_slider(self, value):
        """Processes changes to the speed slider"""
        # Custom range of possible speeds I thought might be handy
        mapping_dict = {0: 0.1, 1: 0.2, 2: 0.3, 3: 0.4, 4: 0.5, 5: 0.6, 6: 0.7, 7: 0.8, 8: 0.9, 9: 1,
                        10: 1.1, 11: 1.25, 12: 1.5, 13: 1.75, 14: 2, 15: 2.5, 16: 3, 17: 4, 18: 5,
                        19: 6, 20: 7, 21: 8, 22: 9, 23: 10, 24: 15, 25: 20, 26: 25, 27: 30,
                        28: 40, 29: 50, 30: 60, 31: 70, 32: 80, 33: 90, 34: 100, 35: 'inf'}
        value = mapping_dict[value]
        # Set the selected speed in the accompanying label
        self.speed_label_right.setText(f'{value}x')
        self.validate_settings()
    
    def handle_detect_button(self):
        """Detects when the user presses a key combination, for the macro hotkey"""
        try:
            self.detect_button.setText('Listening..')
            self.detect_button.setEnabled(False)
            # The read_hotkey() function below locks the thread, but the below line ensures
            # the button visually updates with the above changes before this happens
            QApplication.processEvents()
            keyboard.unhook_all()
            state = keyboard.stash_state()
            try:
                # Waits until it detects the user has pressed some key combo, then returns it
                hotkey = keyboard.read_hotkey()
            except ValueError:
                # Caused when Fn key is pressed, bug in the keyboard library
                hotkey = ''
            keyboard.restore_modifiers(state)
            self.hotstrings.create_hooks()
            # Show the detected hotkey to the user for verification
            self.hotkey_textbox.setText(hotkey)
            self.detect_button.setEnabled(True)
            self.detect_button.setText('Detect')
            self.validate_settings()
        except Exception:
            logging.exception('Unhandled exception in handle_detect_button')
    
    def ok(self):
        """Processes and returns selected settings after user clicks OK"""
        hotkey = self.hotkey_textbox.text()
        # [:-1] is because the label always ends in x, like "2x"
        speed_factor = float(self.speed_label_right.text()[:-1])
        if self.radio_once.isChecked():
            repeat_count = 1
        elif self.radio_n.isChecked():
            repeat_count = int(self.n_textbox.text())
        elif self.radio_inf.isChecked():
            repeat_count = float('inf')
        skip_paths = self.skip_paths_checkbox.isChecked()
        args = {'hotkey': hotkey,
                'speed_factor': speed_factor,
                'repeat_count': repeat_count,
                'skip_paths': skip_paths,
                'events': self.events}
        if self.macro: # We are editing an existing macro
            # So delete it before we recreate it - creates a dupe if they changed the hotkey otherwise
            del self.hotstrings.user_macros[self.macro['hotkey']]
        self.hotstrings.user_macros[hotkey] = args
        self.hotstrings.save_settings()
        self.hotstrings.load_settings()
        self.hotstrings.create_hooks()
        # Close the window
        self.close()
    
    def set_macro(self):
        """Sets all settings to match those of self.macro"""
        # Inverse of the mapping_dict used for the speed slider
        mapping_dict = {0.1: 0, 0.2: 1, 0.3: 2, 0.4: 3, 0.5: 4, 0.6: 5, 0.7: 6,
                        0.8: 7, 0.9: 8, 1: 9, 1.1: 10, 1.25: 11, 1.5: 12, 1.75: 13,
                        2: 14, 2.5: 15, 3: 16, 4: 17, 5: 18, 6: 19, 7: 20, 8: 21,
                        9: 22, 10: 23, 15: 24, 20: 25, 25: 26, 30: 27, 40: 28, 50: 29,
                        60: 30, 70: 31, 80: 32, 90: 33, 100: 34, float('inf'): 35}
        self.hotkey_textbox.setText(self.macro['hotkey'])
        speed_factor = mapping_dict[self.macro['speed_factor']]
        self.slider.setValue(speed_factor)
        # Calling this will update the label appropriately
        self.change_slider(speed_factor)
        repeat_count = self.macro['repeat_count']
        if repeat_count == 1:
            self.radio_once.setChecked(True)
            self.radio_n.setChecked(False)
            self.radio_inf.setChecked(False)
            self.n_textbox.setEnabled(False)
        elif repeat_count == float('inf'):
            self.radio_once.setChecked(False)
            self.radio_n.setChecked(False)
            self.radio_inf.setChecked(True)
            self.n_textbox.setEnabled(False)
        else:
            self.radio_once.setChecked(False)
            self.radio_n.setChecked(True)
            self.radio_inf.setChecked(False)
            self.n_textbox.setEnabled(True)
            self.n_textbox.setText(str(repeat_count))
            self.n = repeat_count
        self.skip_paths_checkbox.setChecked(self.macro['skip_paths'])
        self.events = self.macro['events']
    
    def toggle_n_textbox(self, checked):
        """Enables or disables the 'Repeat n times' textbox with its associated ratio button"""
        self.n_textbox.setEnabled(checked)
        self.validate_settings()
    
    def validate_n(self, value):
        """Ensures only valid values are entered into the 'Repeat n times' textbox"""
        value = value.lstrip('0')
        if value == '' or value == self.n:
            # If it's empty or equal to the current self.n, just keep it as-is
            self.n_textbox.setText(value)
            self.n = value
            return self.validate_settings()
        if not value.isnumeric():
            # If it's not a positive integer, revert it to the current self.n value
            # .isnumeric rejects both '.' and '-'
            self.n_textbox.setText(self.n)
            return self.validate_settings()
        try:
            value_int = int(value)
            value_float = float(value)
            if value_int != value_float:
                raise Exception
            if value_int <= 0:
                raise Exception
            # The above two should never happen because of the above checks
            # Here just in case I overlooked something
            # The input is now definitely valid - update self.n appropriately
            self.n = str(value_int)
            self.validate_settings()
        except:
            # Validating the input failed, fall back to the current self.n value
            self.n_textbox.setText(self.n)
            return self.validate_settings()
    
    def validate_settings(self):
        """Enables the OK button if the currently selected settings are acceptable, disables it otherwise"""
        if self.hotkey_textbox.text() == '':
            # Definitely can't save without a hotkey
            return self.button_box.button(QDialogButtonBox.Ok).setEnabled(False)
        if self.radio_n.isChecked() and self.n_textbox.text() == '':
            # "Repeat n times" is selected but nothing is entered into the textbox, indicating how many times to repeat
            return self.button_box.button(QDialogButtonBox.Ok).setEnabled(False)
        if self.radio_inf.isChecked() and self.speed_label_right.text() == 'infx':
            # Don't allow repeating the macro "Until I stop it" while also having the max speed selected
            # Pretty much always just leads to locking up the machine
            return self.button_box.button(QDialogButtonBox.Ok).setEnabled(False)
        return self.button_box.button(QDialogButtonBox.Ok).setEnabled(True)

if __name__ == "__main__":
    window = Macro_Settings()
    window.show()
