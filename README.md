# syntaxTree
Инстукция по проведению экспериментов, представленных в работе.

Для начала необходим корпус текстов в .conll формате. Для того, чтобы использовать тот же корпус, что представлен в работе, напишите на почту(zhadaevnikita@mail.ru). 

Для запуска скриптов необходимо установить Python 3.5 и модуль sklearn. 

Чтобы собрать вектора для обучения классификатора, необходимо запустить файл main.py. Если Вы используете свой корпус текстов, то в коде скрипта необходимо изменить переменные documents, txt_tokens, txt_chains на соответствующие документы. Содержание документов должно быть аналогично представленным в эксперименте.

Чтобы посмотреть результаты работы классификаторов, необходимо запустить файл learning.py. 

В работе представлены три разных эксперимента. Чтобы посмотреть результаты каждого эксперимента отдельно, необходимо экранировать строки кода в файле features_extracting.py. Запуск экспериментов реализуется в функции get_features(). Каждый эксперимент отмечен так, как указано в тексте работы. Поэтому для того, чтобы провести некоторые эксперимент отдельно, то необходимо экранировать остальные эксперименты. Изначально запускаются все три одновременно.
