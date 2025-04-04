from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout
from PySide6.QtCore import Qt
from ui.components.screens.BaseScreen import BaseScreen
from ui.navigation.ScreenType import ScreenType
from domain.domain_objects.character.leader.leader import Leader


class LeaderScreen(BaseScreen):
    class LeaderScreen(BaseScreen):
        def __init__(self):
            super().__init__()
            self.leader = None
            self._layout = QVBoxLayout(self)
            self._setup_placeholder_ui()

        def set_context(self, data):
            if isinstance(data, Leader):
                self.leader = data
                self._refresh_ui()

        def _setup_placeholder_ui(self):
            # Initial state — maybe a "No Leader Selected" message
            self._layout.addWidget(QLabel("No leader data loaded yet."))

        def _refresh_ui(self):
            # Clear existing layout
            while self._layout.count():
                child = self._layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

            # Rebuild with leader data
            self._setup_ui()

    def set_leader(self, leader: Leader):
        self.leader = leader
        self._setup_ui()

    @property
    def screen_type(self) -> ScreenType:
        return ScreenType.LEADER

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(80, 40, 80, 40)
        layout.setSpacing(20)

        # Title
        title = QLabel("👤 Leader Profile")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 26px;
            font-weight: bold;
            color: #00FFFF;
            letter-spacing: 1px;
            text-shadow: 0 0 6px #00FFFF;
        """)
        layout.addWidget(title)

        # Main form layout
        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        form.setFormAlignment(Qt.AlignmentFlag.AlignTop)
        form.setSpacing(10)

        def add_row(label, value):
            form.addRow(QLabel(f"<b>{label}:</b>"), QLabel(str(value)))

        # Basic info
        add_row("Name", self.leader.name)
        add_row("Profession", self.leader.profession)
        add_row("Gender", self.leader.gender)
        add_row("Age", self.leader.age)
        add_row("Social Class", self.leader.social_class)
        add_row("Convictions", ", ".join(self.leader.convictions))
        add_row("Life Events", "\n".join(self.leader.life_events))

        # Attributes
        form.addRow(QLabel("<b>Attributes:</b>"))
        attrs = self.leader.attributes
        for attr_name, value in vars(attrs).items():
            readable = attr_name.replace("_", " ").title()
            add_row(readable, value)

        # Container widget
        info_container = QWidget()
        info_container.setLayout(form)
        info_container.setStyleSheet("""
            color: #00FFFF;
            font-size: 15px;
            border: 2px solid #00FFFF;
            padding: 16px;
            border-radius: 12px;
            background-color: rgba(10, 20, 40, 0.75);
        """)

        layout.addWidget(info_container)
