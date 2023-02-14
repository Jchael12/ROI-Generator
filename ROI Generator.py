import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton


class Business:

    def __init__(self, total_item_price, total_number_of_items, item_price, Salary, Percentage, ROI):
        self.total_item_price = total_item_price
        self.total_number_of_items = total_number_of_items
        self.item_price = item_price
        self.Salary = Salary
        self.Percentage = Percentage
        self.ROI = ROI

    def computation_info(self):
        result = "Total item price: " + self.total_item_price + "\n" + \
                 "Total number of items: " + self.total_number_of_items + "\n" + \
                 "Item price: " + self.item_price + "\n" + \
                 "Salary: " + str(self.Salary) + "\n" + \
                 "Percentage: " + str(self.Percentage) + "\n" + \
                 "ROI: " + str(self.ROI) + "%"
        return result


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Business ROI Calculator")
        self.widgets()

    def widgets(self):
        self.total_item_price_label = QLabel("Total item price:", self)
        self.total_item_price_label.move(50, 50)
        self.total_item_price_input = QLineEdit(self)
        self.total_item_price_input.move(200, 50)

        self.total_number_of_items_label = QLabel("Total number of items:", self)
        self.total_number_of_items_label.move(50, 100)
        self.total_number_of_items_input = QLineEdit(self)
        self.total_number_of_items_input.move(200, 100)

        self.item_price_label = QLabel("Item price:", self)
        self.item_price_label.move(50, 150)
        self.item_price_input = QLineEdit(self)
        self.item_price_input.move(200, 150)

        self.percentage_label = QLabel("Percentage:", self)
        self.percentage_label.move(50, 200)
        self.percentage_input = QLineEdit(self)
        self.percentage_input.move(200, 200)

        self.investment_label = QLabel("Investment:", self)
        self.investment_label.move(50, 250)
        self.investment_input = QLineEdit(self)
        self.investment_input.move(200, 250)

        self.compute_button = QPushButton("Compute ROI", self)
        self.compute_button.move(150, 300)
        self.compute_button.clicked.connect(self.compute_roi)

        self.result_label = QLabel("", self)
        self.result_label.move(50, 350)
        self.result_label.setFixedSize(360, 100)
        self.result_label.setWordWrap(True)



    def compute_roi(self):
        total_item_price = self.total_item_price_input.text()
        total_number_of_items = self.total_number_of_items_input.text()
        item_price = self.item_price_input.text()
        Percentage = self.percentage_input.text()
        Investment = self.investment_input.text()

        Salary = (float(total_number_of_items)) * (float(item_price))
        Percent = (float(Percentage)) / 100 * Salary
        ROI = (float(Salary)) / (float(Investment)) * 100
        S = Business(total_item_price, total_number_of_items, item_price, Salary, Percentage, ROI)
        result = S.computation_info()

        self.result_label.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
