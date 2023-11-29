import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QCheckBox, QFrame, QStackedLayout
from PyQt5.QtCore import Qt
from exercises import list

class ExerciseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Exercise Planner")
        self.setGeometry(100, 100, 400, 600)
        self.stackedLayout = QStackedLayout()

        self.selectionPage = QWidget()
        self.detailsPage = QWidget()

        self.initSelectionPage()
        self.initDetailsPage()

        self.stackedLayout.addWidget(self.selectionPage)
        self.stackedLayout.addWidget(self.detailsPage)

        self.setLayout(self.stackedLayout)

    def initSelectionPage(self):
        layout = QVBoxLayout(self.selectionPage)

        label = QLabel("Select body parts to exercise:", self.selectionPage)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.muscles = {
            "Arms": QCheckBox("Arms", self.selectionPage),
            "Legs": QCheckBox("Legs", self.selectionPage),
            "Chest": QCheckBox("Chest", self.selectionPage),
            "Back": QCheckBox("Back", self.selectionPage),
            "Shoulders": QCheckBox("Shoulders", self.selectionPage)
        }

        for muscle, checkbox in self.muscles.items():
            layout.addWidget(checkbox)

        nextButton = QPushButton("Next", self.selectionPage)
        nextButton.clicked.connect(self.showExercises)
        layout.addWidget(nextButton)

    def initDetailsPage(self):
        self.detailsLayout = QVBoxLayout(self.detailsPage)

    def showExercises(self):
        self.detailsLayout.setAlignment(Qt.AlignTop)
        self.clearLayout(self.detailsLayout)

        exercise_details = list
        
        for muscle, checkbox in self.muscles.items():
            if checkbox.isChecked():
                muscle_label = QLabel(f"{muscle} Exercises", self.detailsPage)
                muscle_label.setAlignment(Qt.AlignCenter)
                self.detailsLayout.addWidget(muscle_label)

                for exercise, description in exercise_details.get(muscle, {}).items():
                    exercise_label = QLabel(f"{exercise}: {description}", self.detailsPage)
                    self.detailsLayout.addWidget(exercise_label)

        self.stackedLayout.setCurrentWidget(self.detailsPage)

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

def main():
    app = QApplication(sys.argv)
    exApp = ExerciseApp()
    exApp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
