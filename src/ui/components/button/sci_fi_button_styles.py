# Button styles

SCI_FI_BUTTON_BASE = """
    QPushButton {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                       stop:0 #002855, stop:1 #00509E);
        color: #5CFFFA;
        border: 2px solid #00A6ED;
        border-radius: 5px;
        font-family: 'Rajdhani', sans-serif;
        font-weight: bold;
        font-size: 14px;
        padding: 8px 16px;
        min-width: 120px;
        min-height: 40px;
    }
    QPushButton:hover {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                       stop:0 #003B7A, stop:1 #0067CC);
        border: 2px solid #5CFFFA;
        color: #FFFFFF;
    }
    QPushButton:pressed {
        background-color: #001529;
        border: 2px solid #00CCF5;
        padding-left: 18px;
    }
"""

SCI_FI_BUTTON_EXIT = """
    QPushButton {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                       stop:0 #5A0000, stop:1 #8B0000);
        color: #FF9999;
        border: 2px solid #CC0000;
        border-radius: 5px;
        font-family: 'Rajdhani', sans-serif;
        font-weight: bold;
        font-size: 14px;
        padding: 8px 16px;
        min-width: 120px;
        min-height: 40px;
    }
    QPushButton:hover {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                       stop:0 #8B0000, stop:1 #B20000);
        border: 2px solid #FF5555;
        color: #FFFFFF;
    }
    QPushButton:pressed {
        background-color: #5A0000;
        border: 2px solid #FF0000;
        padding-left: 18px;
    }
"""