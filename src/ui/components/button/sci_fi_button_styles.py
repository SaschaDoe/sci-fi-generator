# Button styles

SCI_FI_BUTTON_BASE = """
    QPushButton {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                          stop:0 #002855, stop:1 #00509E);
        color: #5CFFFA;
        border: 2px solid #00A6ED;
        border-radius: 6px;
        font-family: 'Rajdhani', sans-serif;
        font-weight: bold;
        font-size: 14px;
        padding: 8px 16px;
        min-width: 120px;
        min-height: 40px;
        transition: all 0.3s ease-in-out;
    }
    QPushButton:hover {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                          stop:0 #007ACC, stop:1 #00BFFF);
        border: 2px solid #5CFFFA;
        color: #FFFFFF;
        text-shadow: 0 0 6px #5CFFFA;
    }
    QPushButton:pressed {
        background-color: #001529;
        border: 2px solid #00CCF5;
        padding-left: 18px;
        color: #B2FFFF;
    }
"""


SCI_FI_BUTTON_EXIT = """
    QPushButton {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                          stop:0 #5A0000, stop:1 #8B0000);
        color: #FF9999;
        border: 2px solid #CC0000;
        border-radius: 6px;
        font-family: 'Rajdhani', sans-serif;
        font-weight: bold;
        font-size: 14px;
        padding: 8px 16px;
        min-width: 120px;
        min-height: 40px;
    }
    QPushButton:hover {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                          stop:0 #B20000, stop:1 #FF1A1A);
        border: 2px solid #FF5555;
        color: #FFFFFF;
        text-shadow: 0 0 5px #FF6666;
    }
    QPushButton:pressed {
        background-color: #5A0000;
        border: 2px solid #FF0000;
        padding-left: 18px;
        color: #FFCCCC;
    }
"""

SCI_FI_BUTTON_INLINE = """
    QPushButton {
        background-color: transparent;
        color: #00FFFF;
        border: 1px solid #00FFFF;
        border-radius: 4px;
        padding: 2px 6px;
        font-family: 'Rajdhani', sans-serif;
        font-size: 14px;
        font-weight: normal;
    }
    QPushButton:hover {
        background-color: rgba(0, 255, 255, 0.1);
        color: #FFFFFF;
        border-color: #5CFFFA;
    }
    QPushButton:pressed {
        background-color: rgba(0, 255, 255, 0.2);
        color: #B2FFFF;
    }
"""
