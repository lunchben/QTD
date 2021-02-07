import sys
from PyQt5.QtWidgets import QApplication, QWidget
import M

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400, 200)
    w.move(300, 300)

    w.setWindowTitle("蜻蜓目昆虫鉴别系统")
    w.show()

    # 进入GUI主循环，通过exit保证进程安全结束
    sys.exit(app.exec_())
