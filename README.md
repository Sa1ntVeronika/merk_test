Установлен python версии 3.10


Установить виртуальное окружение и активировать его:

`python3 -m venv venv`

`source venv/bin/activate`

В файле capabilities.py необходимо изменить значения platformVersion, deviceName и app на актуальные (ваш девайс/эмулятор, ваш путь к файлу)

Запустить тесты:
`pytest -v --device=phone --html=report.html --self-contained-html`

# Структура проекта


## Locators
В папке хранятся локаторы для взаимодействия с элементами. Локаторы имеют структуру  
   ```
   LOCATOR_NAME = {
    'ios': {
        'method': 'метод поиска для ios',
        'selector': 'селектор для ios'
    },
    'android': {
        'method': метод поиска для ios,
        'selector': 'селектор для ios'
        }
    }
```
## Pages
Описание экранов по паттерну PageObject
BasePage - родительский класс, от которого наследуются остальные экраны  
Основные взаимодействия описываются в нем (скролл, тап, ожидание и т.д)  

Методы на страницах описываются как действия пользователя, зачастую являются "оберткой" над действиями базовой страницы
```
    def enter_profile_name(self, name: str): 
        """Ввод имени профиля {name} в инпут"""
        input = self.get_element(EDIT_PROFILE_NAME)
        self.type_text_to_filed(input, name)
        return self
```
Метод именован как действие пользователя, возвращает экземпляр класса `self` для дальнейшей цепочки действий  

Методы Действия-проверки (asserts) начинают название со слова assert и имеют в себе проверку  
```
    def assert_profile_exist(self, name: str):
        """Проверяем, что профиль с переданным именем существует"""
        profiles = self.get_elements(PROFILE_NAME)
        assert bool([profile for profile in profiles if profile.text == name]), f'Профиль с именем {name} не найден!'
```
## Tests
Тесты пишутся как последовательность действий пользователя, описанных в соответствующих 
 ```
    def test_create_adult_profile(driver_no_reset):
    """Создание взрослого профиля"""
    profile_name = random_string(10)
    SettingsPage(driver_no_reset) \
        .tap_on_tabbar_settings() \
        .tap_on_create_profile_button() \
        .enter_profile_name(profile_name) \
        .save_profile_changes() \
        .assert_profile_exist(profile_name)
 ```
В коде тестов можем создавать дополнительные сущности, необходимые для теста. 
