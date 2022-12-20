# Описать класс Button, конструктор класса принимает width, height, text.

class Button:

        color = 'white' # Объявить атрибут класса color со значением white.

        def __init__(self, text: str, width: int, height: int) -> None:

           # Проверить аргументы на соответствие типам, в случае если типы не верные,
           # вызвать исключение TypeError.

           if not isinstance(text, str):
                raise TypeError('TypeError')
           if not isinstance(width, int):
               raise TypeError('TypeError')
           if not isinstance(height, int):
               raise TypeError('TypeError')

           # Объявить атрибуты объекта  на основании аргументов конструктора

           self.text = text
           self.width = width
           self.height = height

           is_pressed.property = False # Объявить атрибут объекта is_pressed со значением False.

           # Объявить метод класса для изменения атрибута класса white
           # с проверкой типа аргумента поступающего на вход метода,
           # а также на проверку того, входит ли данное значение в список
           # допустимых значений, в противном случае вызвать соответствующее исключение

           @classmethod
           def change_color(cls, new_color: str) -> None:
               cls.color = new_color.title()

               if not isinstance(new_color, str):
                   raise TypeError('TypeError')

        # Объявить метод объекта press изменяющий атрибут объекта is_pressed на противоположное значение.
        def press(self,  is_pressed) -> None:
            self.is_pressed =  True

        # Написать магический метод str возвращающий текст кнопки.
        def __str__(self):
            return f"{self.text_button}"