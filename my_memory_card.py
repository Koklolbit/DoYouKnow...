from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *
 
app = QApplication([])
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Правильно')
rbtn_2 = QRadioButton('Неправильно')
rbtn_3 = QRadioButton('Неправильно')
rbtn_4 = QRadioButton('Неправильно')
 
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
RadioGroupBox.setLayout(layout_ans1) 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
qlist = []






def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right) 
    show_question() 
qlist.append(Question('Кто был вождём СССР в 1941 году?', 'Иосиф Виссарионович Сталин', 'Владимир Ильич Ленин', 'Бенито Муссолини', 'Лев Давидович Троцкий'))
qlist.append(Question('Что из перечисленного реально?', 'Ирландцы', 'Коммунизм', 'Стабильная работа Ростелекома', 'Хорошая зарплата в России'))
qlist.append(Question('Какая страна имеет самую большую площадь?', 'Россия', 'США', 'Китай', 'Израиль'))
qlist.append(Question('Кем пугают маленьких детей, чтобы они хорошо вели себя?', 'Бабайкой', 'Бузовой', 'Путиным', 'Чебурашкой'))
qlist.append(Question('Кого больше всего ненавидел Гитлер?', 'Евреев', 'Японцев', 'Итальянцев', 'Иудеев'))
qlist.append(Question('KWK 36 - это?', 'Пушка', 'Автомат', 'Танк', 'Бомба'))
qlist.append(Question('Кто всегда хорошо выполняет свою работу?', 'Сапёры', 'Строители', 'Плотники', 'Программисты'))
qlist.append(Question('Кто автор книги "Божественная комедия"?', 'Данте Алигьери', 'А. С. Пушкин', 'Л. Н. Толстой', 'Неизвестный солдат'))
qlist.append(Question('Кто делил Польшу уже много раз?', 'Русские и немцы', 'Англичане и французы', 'Австрийцы и Венгры', 'Итальянцы и немцы'))
qlist.append(Question('Кем был придуман танк Т34?', 'Кондитером', 'Известным инженером', 'Самим Иосифом Сталиным', 'Байбаковым'))
qlist.append(Question('Как расшифровывается JSON?', 'JavaScript Object Notation', 'Joseph Stalin Otets Narodov', "JavaScript Opyat' Slomalsya", 'JopaScript Object Notation'))



window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.score = 0
window.total = 0


def show_correct(res):
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    window.total += 1
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')


def next_question():
    window.cur = randint(0, len(qlist) - 1)
    q = qlist[window.cur]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
        right_otvet = window.score / window.total * 100
        print(f'Статистика\n-Всего вопросов: {window.total}\n-Правильных ответов: {window.score}\n-Процент побед: {int(right_otvet)}%')
    else:
        
        next_question()





window.cur = -1
btn_OK.clicked.connect(click_OK) 
window.show()
app.exec()
