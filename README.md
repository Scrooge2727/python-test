[![CI/CD GitHub Actions](https://github.com/Scrooge2727/python-test/actions/workflows/main.yml/badge.svg)](https://github.com/Scrooge2727/python-test/actions/workflows/main.yml)
[![Coverage Status](https://coveralls.io/repos/Scrooge2727/python-test/badge.svg?branch=main)](https://coveralls.io/github/Scrooge2727/python-test?branch=main)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=Scrooge2727_python-test&metric=alert_status)](https://sonarcloud.io/dashboard?id=Scrooge2727_python-test)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Scrooge2727_python-test&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Scrooge2727_python-test)
[![Code smells](https://sonarcloud.io/api/project_badges/measure?project=Scrooge2727_python-test&metric=code_smells)](https://sonarcloud.io/dashboard?id=Scrooge2727_python-test)
# python-test
# Аттестационное тестирование
  - Тест А1 (положительный)
    - Начальное состояние: Открытый терминал
    - Действие: Пользователь запускает программу
    - Ожидаемый результат:
        ```            
      	Options:
        1. Add Task
        2. Remove Task
        3. Mark Task as Completed
        4. View All Tasks
        5. Exit

        ```               
  - Тест А2 (негативный)
    - Начальное состояние: Открытый терминал
    - Действие: Пользователь пишет 1 и добавляет новую задачу с заголовком "Покупки" и описанием "Молоко, яйца"
    - Ожидаемый результат: 
      ```                  
     	Task added successfully!
      ```                         
  - Тест А3 (положительный)
    - Начальное состояние: Открытый терминал
    - Действие: Пользователь нажимает 2 и выбирает задачу из списка и пишет её номер
    - Ожидаемый результат: 
        ```                     
      	Task marked as completed!
        ```                      
  - Тест А4 (негативный)
    - Начальное состояние: Открытый терминал
    - Действие: Пользователь пытается удалить задачу с некорректным номером
    - Ожидаемый результат: 
        ```                           
      	Invalid task number.
        ```                           
  - Тест А5 (положительный)
    - Начальное состояние: Открытый терминал
    - Действие: Пользователь нажимает 3 и выбирает задачу и пишет её номер
    - Ожидаемый результат: 
        ```                            
      	Task marked as completed!
        ```                     
  - Тест А6 (негативный)
    - Начальное состояние: Открытый терминал</li>
    - Действие: Пользователь вводит некорректный выбор в меню</li>
    - Ожидаемый результат: 
        ```                       
      	Invalid choice. Please enter a number between 1 and 5.
        ```
# Блочное тестирование
  - Класс Task
    - Тест Б1: test_task_completion
      - Цель: Проверить, что метод mark_as_completed корректно изменяет статус задачи на выполненный.
        ```
        Создать объект Task с заданным заголовком и описанием.
        Проверить, что изначально задача имеет статус "не выполнена".
        Вызвать метод mark_as_completed.
        Проверить, что статус задачи изменился на "выполнена".
          ```
    - Тест Б2: test_task_info
      -  Цель: Проверить, что метод get_task_info корректно возвращает информацию о задаче.
         ```
         Создать объект Task с заданным заголовком и описанием.
         Получить информацию о задаче с помощью метода get_task_info.
         Проверить, что полученная информация соответствует ожидаемой.
         ```
    - Тест Б3: test_task_info2
      - Цель: Проверить, что метод get_task_info корректно работает с числовыми значениями в заголовке и описании.
        ```
        Создать объект Task с числовым заголовком и описанием.
        Получить информацию о задаче с помощью метода get_task_info.
        Проверить, что полученная информация соответствует ожидаемой.
        ```
    - Тест Б4: test_task_default_completion
      - Цель: Проверить, что при создании задачи по умолчанию статус устанавливается как "не выполнена".
        ```
        Создать объект Task без явного указания статуса.
        Проверить, что статус задачи изначально "не выполнена".
        ```  
  - Класс TaskList
    - Тест Б5: test_remove_task
      - Цель: Проверить, что метод remove_task класса TaskList корректно удаляет задачу из списка.
        ```
        Удалить одну из задач с помощью метода remove_task.
        Проверить, что задача была успешно удалена из списка.
        ```
    - Тест Б6: test_get_all_tasks_info
      - Цель: Проверить, что метод get_all_tasks_info класса TaskList возвращает корректную информацию о всех задачах.
        ```
        Вызвать метод get_all_tasks_info.
        Проверить, что полученная информация соответствует ожидаемой.
        ```
    - Тест Б7: test_get_completed_tasks
      - Цель: Проверить, что метод _get_completed_tasks класса TaskList возвращает корректный список выполненных задач.
        ```
        Вызвать метод _get_completed_tasks.
        Проверить, что возвращенный список содержит только выполненные задачи.
        ```
    - Тест Б8: test_remove_nonexistent_task
      - Цель: Проверить, что метод remove_task класса TaskList корректно обрабатывает попытку удаления несуществующей задачи.
        ```
        Попытаться удалить задачу, которая не существует, с помощью метода remove_task.
        Проверить, что метод вызывает исключение ValueError.
        ```
# Интеграционное тестирование
  - Тест И1: test_add_task
    - Цель: Проверить, что метод add_task класса TaskList корректно добавляет задачи в список.
      ```
      Создать объект TaskList.
      Создать несколько объектов Task.
      Добавить задачи в список с помощью метода add_task.
      Проверить, что задачи были успешно добавлены.
      ```
