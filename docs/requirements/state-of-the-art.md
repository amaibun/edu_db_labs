# Аналіз предметної області

## Вступ

Системи управління відкритими даними - це спеціалізовані системи, призначені для керування, зберігання та надання доступу до відкритих даних. Відкриті дані - це дані, які можуть бути вільно використані, поширені та модифіковані будь-ким.

## Основні визначення

1. **RDBMS (Relational Database Management System)** - це тип бази даних, який використовує реляційну модель даних. 
Реляційна модель даних заснована на концепції таблиць, рядків і стовпців, де дані організовані у вигляді таблиць з визначеними стовпцями і рядками. RDBMS забезпечує можливість виконання запитів SQL (Structured Query Language) для маніпуляції даними.
2. **NoSQL** - це тип бази даних, який не використовує традиційну реляційну модель даних. 
NoSQL бази даних розроблені для обробки великих обсягів даних і забезпечують гібридну модель зберігання даних, яка може включати ключ-значення, документи, графові дані тощо.
3. **Графові бази даних** - це тип бази даних, який використовує графову модель даних. 
Графова модель даних заснована на концепції вузлів (або об'єктів) і ребер (або зв'язків) між ними. Графові бази даних розроблені для зберігання і обробки даних, які мають складну структуру зв'язків, наприклад, соціальні мережі, рекомендаційні системи тощо.

## Підходи та способи вирішення завдання

### Підходи

**Централізований підхід:** цей підхід передбачає створення централізованої системи управління відкритими даними, яка зберігає та керує всіма даними в одному місці.

**Децентралізований підхід:** цей підхід передбачає створення децентралізованої системи управління відкритими даними, яка складається з декількох незалежних вузлів, які зберігають та керують даними окремо.

**Гібридний підхід:** цей підхід поєднує централізований та децентралізований підходи, створюючи систему управління відкритими даними, яка складається з централізованого вузла та декількох децентралізованих вузлів.

### Методи зберігання і управління даними

**Бази даних:** відносно структуровані дані зберігаються у базах даних, таких як реляційні бази даних (RDBMS), NoSQL-бази даних, графові бази даних тощо.

**Файлові системи:** дані зберігаються у файлах на диску, таких як текстові файли, зображення, відео тощо.

**Об'єктні сховища:** дані зберігаються у вигляді об'єктів, таких як об'єктні бази даних, сховища даних у хмарі тощо.

**Блокчейн:** дані зберігаються у вигляді блоків, які пов'язані між собою за допомогою криптографічних алгоритмів.

## Порівняльна характеристика існуючих засобів вирішення завдання

|        |Functionality|Usability|Reliability|Perfomance|Supportability|
|--------|-------------|---------|-----------|----------|--------------|
|CKAN    |підтримка різних форматів даних, пошук, фільтрація|інтуїтивний інтерфейс, але деякі функції можуть бути складними для використання|стабільна робота, мінімум помилок|швидкий доступ до даних, але деякі операції можуть бути повільними|документація, форуми, підтримка спільноти|
|DKAN    |підтримка різних форматів даних, пошук, фільтрація, візуалізація даних|інтуїтивний інтерфейс, але деякі функції можуть бути складними для використання|стабільна робота, мінімум помилок|швидкий доступ до даних, швидка візуалізація даних|документація, форуми, підтримка спільноти, підтримка розробників|
|Data.gov|підтримка різних форматів даних, пошук, фільтрація, візуалізація даних|інтуїтивний інтерфейс, але деякі функції можуть бути складними для використання|стабільна робота, мінімум помилок|швидкий доступ до даних, швидка візуалізація даних|окументація, форуми, підтримка спільноти, підтримка розробників|

## Висновки

У цьому огляді різних систем управління відкритими даними, включаючи CKAN, DKAN, Data.gov було розглянуто їхні переваги і недоліки. Кожна система пропонує широкий спектр функцій для роботи з даними, включаючи пошук, фільтрацію, візуалізацію та інше.

Жодна система не є ідеальною і кожна має свої недоліки. Наприклад, CKAN і DKAN мають обмеження щодо кількості даних, які можуть бути оброблені, тоді як Data.gov має складніший інтерфейс, який може бути складними для використання для тих, хто не має досвіду роботи з відкритими даними.

Враховуючи ці недоліки, було прийнято рішення про розробку власної системи управління відкритими даними, яка б поєднувала найкращі функції існуючих систем і не мала їхніх обмежень.

## Посилання

1. [CKAN](https://ckan.org/)
2. [DKAN](https://www.drupal.org/project/dkan/)
3. [Data.gov](https://data.gov/)