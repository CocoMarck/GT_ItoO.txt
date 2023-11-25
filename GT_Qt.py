from Modulos.Modulo_GT import Translate
from Modulos.Modulo_Text import (
    Text_Read
)
from Modulos.Modulo_Language import (
    get_text as Lang,
    Default_Language
)

from Interface import Modulo_Util_Qt as Util_Qt
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QFileDialog,
    QMessageBox,
    QTextEdit,
    QPushButton,
    QLineEdit,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QIcon
from pathlib import Path


class Window_Main(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle( Lang('trs') )
        self.resize(512, -1)
        
        # Contenedor Principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Sección Vertical - Establecer archivo de texto
        hbox = QHBoxLayout()
        vbox_main.addLayout(hbox)
        
        self.entry_i_dir = QLineEdit(
            self,
            maxLength=-1,
            placeholderText=Lang('arch')
        )
        hbox.addWidget(self.entry_i_dir)
        
        button_i_dir = QPushButton( Lang('set_dir') )
        button_i_dir.clicked.connect(self.evt_set_input_dir)
        hbox.addWidget(button_i_dir)
        
        vbox_main.addStretch()
        
        # Sección Vertical - Texto en un Text Edit
        self.text_edit = QTextEdit(
            readOnly=False
        )
        vbox_main.addWidget(self.text_edit)
        
        # Sección Vertical - Establecer Language input y output
        hbox = QHBoxLayout()
        vbox_main.addLayout(hbox)
        
        label = QLabel(f'{Lang("lang")}: ')
        hbox.addWidget(label)
        
        hbox.addStretch()
        
        self.entry_i_lang = QLineEdit(
            self,
            maxLength=-1,
            text=str(Default_Language()),
            placeholderText=Lang('i')
        )
        hbox.addWidget(self.entry_i_lang)
        
        self.entry_o_lang = QLineEdit(
            self,
            maxLength=-1,
            text='',
            placeholderText=Lang('o')
        )
        hbox.addWidget(self.entry_o_lang)
        
        # Sección Vertical - Iniciar Traducción
        vbox_main.addStretch()
        
        button_start_translate = QPushButton( f'{Lang("start")} | {Lang("trs")}' )
        button_start_translate.clicked.connect(self.evt_start_translate)
        vbox_main.addWidget(button_start_translate)
        
        # Fin - Mostrar ventana
        self.show()
    
    def evt_set_input_dir(self):
        # Establecer un archivo de texto, y si se logra detectar texto, establecerlo en el text edit
        text, ok = QFileDialog.getOpenFileName(
            self,
            Lang('text'),
            self.entry_i_dir.text(),
            f'{Lang("text")} (*.txt)'
        )
        if text:
            self.entry_i_dir.setText(text)
            text = Text_Read(
                file_and_path=text,
                option='ModeText'
            )
            self.text_edit.setText(
                str(text).replace('\n', '<br>')
            )
    
    def evt_start_translate(self):
        # Verificar que los parametros esten correctos.
        text_error = ''
        
        self.text_input = self.text_edit.toPlainText()
        if self.text_input == '':
            text_error += f'ERROR - {Lang("text")}\n'
        
        if self.entry_i_lang.text() == '':            
            text_error += f'ERROR - {Lang("lang")} | {Lang("i")}\n'
        
        if self.entry_o_lang.text() == '':
            text_error += f'ERROR - {Lang("lang")} | {Lang("o")}\n'
        
        
        # Fin - Traducir o no
        if text_error == '':
            # Preguntar si guardar traducción o no.
            message_quest = QMessageBox.question(
                self,
                '',
                Lang('save-or-no_trs'),
                QMessageBox.StandardButton.Yes |
                QMessageBox.StandardButton.No
            )
            if message_quest == QMessageBox.StandardButton.Yes:
                self.save_translate = True
                print(self.text_input)
            
            else:
                self.save_translate = False
                print(self.text_input)

        else:
            # Error en alguno de los parametros
            QMessageBox.critical(
                self,
                'ERROR',
                text_error
            )


class Thread_translate(QThread):
    finished = pyqtSignal(str)
    def __init__(
        self,
        i_lang=None,
        o_lang=None,
        i_text=None,
        o_text=None,
    ):
        super().__init__()
        self._i_lang = i_lang
        self._o_lang = o_lang
        self._i_text = i_text
        self._o_text = o_text
    
    def run(self):
        self.text_translate = Translate(
            language_input = self.i_lang,
            language_output = self.o_lang,
            output_text = self.o_text,
            text_only = self.i_text,
            print_mode = False
        )
    
        self.finished.emit(self.text_translate)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_Main()
    sys.exit( app.exec() )