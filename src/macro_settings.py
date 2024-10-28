from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QSlider, QLabel, QLineEdit, QPushButton, QDialogButtonBox
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt
import keyboard
from time import sleep

class Macro_Settings(QWidget):
    def __init__(self, hotstrings = None, events = None):
        super().__init__()
        self.setWindowTitle("Macro settings")
        
        self.hotstrings = hotstrings
        self.events = events
        
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
        
        self.radio_once = QRadioButton("Once")
        self.radio_n = QRadioButton("This many times:")
        self.radio_inf = QRadioButton("Until I stop it")
        self.radio_inf.setChecked(True)
        
        self.n_textbox = QLineEdit()
        self.n_textbox.textChanged.connect(self.validate_n)
        self.n = ''
        self.n_textbox.setEnabled(False)

        self.radio_once.toggled.connect(self.validate_settings)
        # Enable toggle_n_textbox only when radio_n is selected
        self.radio_n.toggled.connect(self.toggle_n_textbox)
        self.radio_inf.toggled.connect(self.validate_settings)
        
        # Arrange radio buttons in group 3
        repeat_layout.addWidget(self.radio_once)
        
        # Place Option B and QLineEdit on the same row
        n_layout.addWidget(self.radio_n)
        n_layout.addWidget(self.n_textbox)
        repeat_layout.addLayout(n_layout)
        
        repeat_layout.addWidget(self.radio_inf)
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
        self.button_box.accepted.connect(self.accept)
        self.button_box.button(QDialogButtonBox.Ok).setEnabled(False)
        self.button_box.rejected.connect(self.reject)
        
        # Add widgets to main layout
        main_layout.addWidget(self.playback_box)
        main_layout.addWidget(self.repeat_box)
        main_layout.addWidget(self.hotkey_box)
        main_layout.addWidget(self.button_box)
        self.setGeometry(100, 100, 1, 1)

        self.change_slider(self.slider.value())

    def validate_settings(self):
        if self.hotkey_textbox.text() == '':
            return self.button_box.button(QDialogButtonBox.Ok).setEnabled(False)
        if self.radio_n.isChecked() and self.n_textbox.text() == '':
            return self.button_box.button(QDialogButtonBox.Ok).setEnabled(False)
        if self.radio_inf.isChecked() and self.speed_label_right.text() == 'infx':
            return self.button_box.button(QDialogButtonBox.Ok).setEnabled(False)
        return self.button_box.button(QDialogButtonBox.Ok).setEnabled(True)
    
    def toggle_n_textbox(self, checked):
        self.n_textbox.setEnabled(checked)
        self.validate_settings()
    
    def validate_n(self, value):
        value = value.lstrip('0')
        if value == '' or value == self.n:
            self.n_textbox.setText(value)
            self.n = value
            return self.validate_settings()
        if not value.isnumeric():
            self.n_textbox.setText(self.n)
            return self.validate_settings()
        if '.' in value:
            self.n_textbox.setText(self.n)
            return self.validate_settings()
        try:
            value_int = int(value)
            value_float = float(value)
            if value_int != value_float:
                raise Exception
            if value_int <= 0:
                raise Exception
            self.n = str(value_int)
            self.validate_settings()
        except:
            self.n_textbox.setText(self.n)
            return self.validate_settings()
    
    def change_slider(self, value):
        mapping_dict = {0: 0.1, 1: 0.2, 2: 0.3, 3: 0.4, 4: 0.5, 5: 0.6, 6: 0.7, 7: 0.8, 8: 0.9, 9: 1,
                        10: 1.1, 11: 1.25, 12: 1.5, 13: 1.75, 14: 2, 15: 2.5, 16: 3, 17: 4, 18: 5,
                        19: 6, 20: 7, 21: 8, 22: 9, 23: 10, 24: 15, 25: 20, 26: 25, 27: 30,
                        28: 40, 29: 50, 30: 60, 31: 70, 32: 80, 33: 90, 34: 100, 35: 'inf'}
        value = mapping_dict[value]
        self.speed_label_right.setText(f'{value}x')
        self.validate_settings()
    
    def accept(self):
        speed_factor = float(self.speed_label_right.text()[:-1])
        if self.radio_once.isChecked():
            repeat_count = 1
        elif self.radio_n.isChecked():
            repeat_count = int(self.n_textbox.text())
        elif self.radio_inf.isChecked():
            repeat_count = float('inf')
        hotkey = self.hotkey_textbox.text()
        args = {'hotkey': hotkey,
                'speed_factor': speed_factor,
                'repeat_count': repeat_count,
                'events': self.events}
        self.hotstrings.user_macros[hotkey] = args
        self.hotstrings.save_settings()
        self.hotstrings.load_settings()
        self.hotstrings.create_hooks()
        self.close()
    
    def reject(self):
        self.close()
    
    def handle_detect_button(self):
        self.detect_button.setText('Listening..')
        self.detect_button.setEnabled(False)
        QApplication.processEvents()
        keyboard.unhook_all()
        state = keyboard.stash_state()
        hotkey = keyboard.read_hotkey()
        keyboard.restore_modifiers(state)
        self.hotstrings.create_hooks()
        self.hotkey_textbox.setText(hotkey)
        self.detect_button.setEnabled(True)
        self.detect_button.setText('Detect')
        self.validate_settings()

if __name__ == "__main__":
    app = QApplication([])
    window = Macro_Settings()
    window.show()
