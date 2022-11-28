# Помимо того, что классы служат фабрикой по производству однотипных объектов со сходным поведением, они имеют ещё одну важную особенность — наследование.
#
# Как мы уже видели, объекты, созданные при помощи класса, наследуют атрибуты класса, которые объявлены прямо в теле, а не добавлены в конкретный независимый экземпляр.
#
# Идея наследования класса состоит в том, что новый класс создаётся не на «пустом месте», а на основе уже существующего. В результате наследования все поля и функции из базового класса неявным образом «наследуются» в производном классе.
#
# При описании производного класса используем шаблон:
#
#     class ПроизводныйКласс (БазовыйКласс):
#     # Тело класса
#
#     import datetime
#
#     class Product:
#         max_quantity = 100000
#
#         def __init__(self, name, category, quantity_in_stock):
#             self.name = name
#             self.category = category
#             self.quantity_in_stock = quantity_in_stock
#
#         def is_available(self):
#             return True if self.quantity_in_stock > 0 else False
#
#     class Food(Product):
#         is_critical = True
#         needs_to_be_refreshed = True
#         refresh_frequency = datetime.timedelta(days=1)
#
#     eggs = Food(name="eggs", category="food", quantity_in_stock=5)
#     print(eggs.max_quantity)

#
#
# Важно, если мы назовём атрибут или метод так же, как он называется в родительском классе, он будет переопределён. Рассмотрим на примере:
#
# class Event:
#     def __init__(self, timestamp=0, event_type="", session_id=""):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
#
#     def init_from_dict(self, event_dict):
#         self.timestamp = event_dict.get("timestamp")
#         self.type = event_dict.get("type")
#         self.session_id = event_dict.get("session_id")
#
#     def show_description(self):
#         print("This is generic event.")
#
#
# class ItemViewEvent(Event):
#     type = "itemViewEvent"
#
#     def __init__(self, timestamp=0, session_id="", number_of_views=0):
#         self.timestamp = timestamp
#         self.session_id = session_id
#         self.number_of_views = number_of_views
#
#     def show_description(self):
#         print("This event means someone has browsed an item.")
#
#
# if __name__ == "__main__":
#     test_view_event = ItemViewEvent(timestamp=1549461608000, session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct", number_of_views=6)
#     test_view_event.show_description()
#     print(test_view_event.type)
# Вывод:
#
# This event means someone has browsed an item.
# itemViewEvent
# Что получили:
#
# Переопределили конструктор класса. Теперь мы используем не родительский, а свой, и передаём в него другой набор аргументов. Так у нас получился кастомизированный набор атрибутов: у родительского класса нет атрибута number_of_views.
# Переопределили значение атрибута type с помощью атрибута класса. Теперь при вызове type от экземпляра нашего дочернего класса мы получим значение атрибута type нашего класса ItemViewEvent.
# Переопределили работу метода show_description: теперь он показывает более специфичное для класса описание.