# Модель прецедентів

## Загальна схема

```
@startuml

    actor Expert
    actor Client

    usecase "UserManageAccount\nВзаємодія з\nобліковим записом" as UInteraction
    usecase "SurveyInteraction\nВзаємодія з опитуванням" as EInteraction
    usecase "SurveyCreate\nСтворити\nопитування" as SCreate
    usecase "SurveyDelete\nВидалити\nопитування" as SDelete
    usecase "SurveyManageResults\nВзаємодія\nз результатами" as SResults
    usecase "SurveyShareAccess\nПоділитись\nопитуванням" as SShare
    usecase "SurveyUpdate\nОновлення опитування" as SUpdate

    Expert -d-|> Client
    Expert -> EInteraction
    Client -u-> SResults
    Client -r-> SCreate
    Client -d-> UInteraction
    Client -d-> SDelete
    Client -d-> SUpdate
    Client -l-> SShare

@enduml
```

[actors will be here]

## Сценарії використання

### CreateDataSet
| ID | Назва | Учасники | Передумови | Результат | Виключні ситуації | Основний сценарій |
|:----|:------|:---------|:-----------|:---------|:------------------|:-----------------|
| CreateDataSet | Створення набору даних | Data Administrator | None | Новий набір даних створено | Недійсні дані, дублікат набору даних | 1. Data Administrator логіниться, 2. натискає "Створити набір даних", 3. вводить дані про набір даних, 4. натискає "Зберегти" |

```
@startuml
    skinparam ActivityBackgroundColor #f5f5f5

    |Користувач|
    start
    :відкриває інтерфейс створення набору даних;
    :вводить метадані набору даних;
    :вибирає файл для завантаження;
    :відправляє запит на збереження;
    note right #d10000
    <b>Possible error:
        - InvalidDataException
        - FileUploadException
    end note

    |Система|
    :перевіряє формат та цілісність даних;
    :зберігає набір даних у базі даних;
    :публікує набір даних для доступу користувачів;

    |Користувач|
    stop;

@enduml
```

### UpdateDataSet
| ID | Назва | Учасники | Передумови | Результат | Виключні ситуації | Основний сценарій |
|:----|:------|:---------|:-----------|:---------|:------------------|:-----------------|
| UpdateDataSet | Оновлення набору даних | Data Administrator | Набір даних існує | Набір даних оновлено | Недійсні дані, набір даних не знайдено | 1. Data Administrator логіниться, 2. шукає набір даних, 3. натискає "Оновити", 4. вводить оновлені дані, 5. натискає "Зберегти" |

```
@startuml
skinparam ActivityBackgroundColor #f5f5f5

|Користувач|
start
:відкриває інтерфейс оновлення набору даних;
:вводить оновлені метадані;
:вибирає файл для оновлення;
:відправляє запит на оновлення;

note right #d10000
<b>Possible error:
    - InvalidDataException
    - FileUploadException
end note

|Система|
:перевіряє формат та цілісність даних;
:оновлює набір даних у базі даних;
:публікує оновлений набір даних;

|Користувач|
stop;
@enduml
```

### DeleteDataSet
| ID | Назва | Учасники | Передумови | Результат | Виключні ситуації | Основний сценарій |
|:----|:------|:---------|:-----------|:---------|:------------------|:-----------------|
| DeleteDataSet | Видалення набору даних | Data Administrator | Набір даних існує | Набір даних видалено | Набір даних не знайдено, набір даних використовується | 1. Data Administrator логіниться, 2. шукає набір даних, 3. натискає "Видалити", 4. підтверджує видалення |

```
@startuml
skinparam ActivityBackgroundColor #f5f5f5

|Користувач|
start
:відкриває інтерфейс керування наборами даних;
:вибирає набір даних для видалення;
:відправляє запит на видалення;

note right #d10000
<b>Possible error:
    - DataSetNotFoundException
    - PermissionDeniedException
end note

|Система|
:перевіряє наявність набору даних;
:перевіряє права доступу;
:видаляє набір даних із бази;
:оновлює доступні набори даних;

|Користувач|
stop;
@enduml
```

### ViewDataSet
| ID | Назва | Учасники | Передумови | Результат | Виключні ситуації | Основний сценарій |
|:----|:------|:---------|:-----------|:---------|:------------------|:-----------------|
| ViewDataSet | Перегляд набору даних | Data Administrator, Data Consumer | Набір даних існує | Дані про набір даних відображаються | Набір даних не знайдено | 1. Користувач логіниться, 2. шукає набір даних, 3. натискає "Переглянути" |

```
@startuml
skinparam ActivityBackgroundColor #f5f5f5

|Користувач|
start
:відкриває інтерфейс перегляду наборів даних;
:вибирає набір даних для перегляду;
:відправляє запит на отримання даних;

note right #d10000
<b>Possible error:
    - DataSetNotFoundException
    - PermissionDeniedException
end note

|Система|
:перевіряє наявність набору даних;
:перевіряє права доступу;
:отримує дані з бази;
:відображає набір даних користувачеві;

|Користувач|
stop;
@enduml
```

[AddUser will be here]
[UpdateUser will be here]
[RemoveUser will be here]
[AssignPermissions will be here]

### UploadDataSet
| ID | Назва | Учасники | Передумови | Результат | Виключні ситуації | Основний сценарій |
|:----|:------|:---------|:-----------|:---------|:------------------|:-----------------|
| UploadDataSet | Завантаження набору даних | Data Contributor | Користувач має права на завантаження даних | Набір даних завантажено | Недійсні дані, дублікат набору даних, помилка завантаження | 1. Користувач логіниться, 2. натискає кнопку "Завантажити набір даних", 3. вибирає файл для завантаження, 4. вводить метадані про набір даних, 5. натискає кнопку "Завантажити" |

```
@startuml
skinparam ActivityBackgroundColor #f5f5f5

|Користувач|
start
:відкриває інтерфейс завантаження набору даних;
:вводить метадані набору даних;
:вибирає файл для завантаження;
:відправляє запит на завантаження;

note right #d10000
<b>Possible error:
    - InvalidDataException
    - FileUploadException
    - PermissionDeniedException
end note

|Система|
:перевіряє формат та цілісність даних;
:перевіряє права доступу;
:зберігає набір даних у базі;
:публікує набір даних для доступу користувачів;

|Користувач|
stop;
@enduml
```

### ValidateDataSet
| ID | Назва | Учасники | Передумови | Результат | Виключні ситуації | Основний сценарій |
|:----|:------|:---------|:-----------|:---------|:------------------|:-----------------|
| ValidateDataSet | Валідація набору даних | Data Administrator, Data Contributor | Користувач має права Data Administrator або Data Contributor      | Набір даних успішно перевірено на відповідність стандартам.  | Користувач не має прав для виконання операції. Набір даних не відповідає встановленим вимогам. | 1. Користувач ініціює перевірку набору даних через інтерфейс. 2. Система перевіряє набір даних на наявність помилок (формат, повнота даних, коректність значень). 3. У разі помилок система повідомляє користувача про виявлені проблеми. 4. Якщо перевірка пройшла успішно, система підтверджує, що набір даних є валідним. |


```
@startuml
skinparam ActivityBackgroundColor #f5f5f5

|Користувач|
start
:відкриває інтерфейс перевірки набору даних;
:вибирає набір даних для перевірки;
:відправляє запит на перевірку набору даних;

note right #d10000
<b>Possible error:
    - InvalidDataException
    - DataIntegrityException
end note

|Система|
:перевіряє формат набору даних;
:перевіряє цілісність даних;
:перевіряє відповідність вимогам;
:повідомляє користувача про результат перевірки;

|Користувач|
stop;
@enduml
```

### PublishDataSet
| ID | Назва | Учасники | Передумови | Результат | Виключні ситуації | Основний сценарій |
|:----|:------|:---------|:-----------|:---------|:------------------|:-----------------|
| PublishDataSet   | Публікація набору даних   | Data Administrator, Data Contributor | Користувач має права Data Administrator або Data Contributor      | Набір даних успішно опубліковано та доступний для користувачів | Користувач не має прав для виконання операції. Набір даних не відповідає вимогам публікації. | 1. Користувач ініціює публікацію. 2. Система перевіряє набір даних. 3. Якщо перевірка пройшла успішно, набір даних публікується. |

```
@startuml
skinparam ActivityBackgroundColor #f5f5f5

|Користувач|
start
:відкриває інтерфейс публікації набору даних;
:вибирає набір даних для публікації;
:відправляє запит на публікацію;

note right #d10000
<b>Possible error:
    - PermissionDeniedException
    - DataSetNotFoundException
end note

|Система|
:перевіряє наявність набору даних;
:перевіряє права доступу користувача;
:публікує набір даних для доступу користувачів;
:оновлює статус набору даних;

|Користувач|
stop;
@enduml
```

[SearchDataSetswill be here]
[FilterDataSets will be here]
[ViewDataSetDetails will be here]

### DownloadDataSet
| ID | Назва | Учасники | Передумови | Результат | Виключні ситуації | Основний сценарій |
|:----|:------|:---------|:-----------|:---------|:------------------|:-----------------|
| DownloadDataSet | Завантаження набору даних | Data Consumer    | Користувач має права Data Consumer, набір даних доступний для завантаження | Набір даних успішно завантажено на пристрій користувача | Користувач не має прав для завантаження набору даних. Набір даних недоступний для завантаження. Проблеми з інтернет-з'єднанням. | 1. Користувач логіниться в систему. 2. Користувач шукає необхідний набір даних за допомогою пошуку або фільтрів. 3. Користувач натискає кнопку "Завантажити" для вибраного набору даних. 4. Система перевіряє доступність набору даних і дозволяє завантажити файл. |

```
@startuml
skinparam ActivityBackgroundColor #f5f5f5

|Користувач|
start
:відкриває інтерфейс завантаження набору даних;
:вибирає набір даних для завантаження;
:відправляє запит на завантаження;

note right #d10000
<b>Possible error:
    - DataSetNotFoundException
    - PermissionDeniedException
end note

|Система|
:перевіряє наявність набору даних;
:перевіряє права доступу користувача;
:генерує запит на завантаження файлу;
:передає файл користувачеві;

|Користувач|
stop;
@enduml
```