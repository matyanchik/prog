from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner


class BankAppGUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.add_widget(Label(text='Выберите услугу:', size_hint=(1, None), height=30))
        self.service_spinner = Spinner(
            text='Кредит',
            values=('Кредит', 'Рассрочка', 'Вклад'),
            size_hint=(1, None),
            height=44
        )
        self.service_spinner.bind(text=self.toggle_rate_input)
        self.add_widget(self.service_spinner)

        self.principal_input = TextInput(hint_text='Сумма', multiline=False, input_filter='float', size_hint=(1, None), height=44)
        self.rate_input = TextInput(hint_text='Ставка (%)', multiline=False, input_filter='float', size_hint=(1, None), height=44)
        self.term_input = TextInput(hint_text='Срок (мес.)', multiline=False, input_filter='int', size_hint=(1, None), height=44)

        self.add_widget(self.principal_input)
        self.add_widget(self.rate_input)
        self.add_widget(self.term_input)

        self.calc_button = Button(text='Рассчитать', size_hint=(1, None), height=44)
        self.calc_button.bind(on_press=self.perform_calculation)
        self.add_widget(self.calc_button)

    def toggle_rate_input(self, spinner, text):
        """Скрывает поле ставки при выборе 'Рассрочка'."""
        if text == 'Рассрочка':
            self.rate_input.opacity = 0
            self.rate_input.disabled = True
        else:
            self.rate_input.opacity = 1
            self.rate_input.disabled = False

    def perform_calculation(self, instance):
        """Функция-заглушка для расчётов"""
        pass


class BankApp(App):
    def build(self):
        return BankAppGUI()


if __name__ == '__main__':
    BankApp().run()