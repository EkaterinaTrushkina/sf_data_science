# Проект 3. Предсказание оценки отеля booking.com

## Оглавление
[1. Описание проекта](https://github.com/EkaterinaTrushkina/sf_data_science/tree/main/project_3#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)

[2. Какой кейс решаем](https://github.com/EkaterinaTrushkina/sf_data_science/tree/main/project_3#%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)

[3. Краткая информация о данных](https://github.com/EkaterinaTrushkina/sf_data_science/tree/main/project_3#%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)

[4. Этапы работы над проектом](https://github.com/EkaterinaTrushkina/sf_data_science/tree/main/project_3#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)

[5. Результат](https://github.com/EkaterinaTrushkina/sf_data_science/tree/main/project_3#%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)

[6. Выводы](https://github.com/EkaterinaTrushkina/sf_data_science/tree/main/project_3#%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)

### Описание Проекта
Представьте, что вы работаете дата-сайентистом в компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов обнаружения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель ведёт себя нечестно, и его стоит проверить.


:arrow_up:[к оглавлению](https://github.com/EkaterinaTrushkina/sf_data_science/tree/main/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Какой кейс решаем
Нужно считать файл с резюме, после этого провести разведывательный анализ и очистку данных, проект состоит из 4х частей
- базовый анализ структуры данных
- преобразование данных
- разведывательный анализ
- очистка данных

### Краткая информация о данных
файл с исходными данными расположен здесь - https://drive.google.com/file/d/1Qj0iYEbD64eVAaaBylJeIi3qvMzxf2C_/view?usp=sharing
Данные скачаны с booking.com c следующей информацией
- hotel_address — адрес отеля;
- review_date — дата, когда рецензент разместил соответствующий отзыв;
- average_score — средний балл отеля, рассчитанный на основе последнего комментария за последний год;
- hotel_name — название отеля;
- reviewer_nationality — страна рецензента;
- negative_review — отрицательный отзыв, который рецензент дал отелю;
- review_total_negative_word_counts — общее количество слов в отрицательном отзыв;
- positive_review — положительный отзыв, который рецензент дал отелю;
- review_total_positive_word_counts — общее количество слов в положительном отзыве.
- reviewer_score — оценка, которую рецензент поставил отелю на основе своего опыта;
- total_number_of_reviews_reviewer_has_given — количество отзывов, которые рецензенты дали в прошлом;
- total_number_of_reviews — общее количество действительных отзывов об отеле;
- tags — теги, которые рецензент дал отелю;
- days_since_review — количество дней между датой проверки и датой очистки;
- additional_number_of_scoring — есть также некоторые гости, которые просто поставили оценку сервису, но не оставили отзыв. Это число указывает, сколько там действительных оценок без проверки.
- lat — географическая широта отеля;
- lng — географическая долгота отеля.

:arrow_up:[к оглавлению](https://github.com/EkaterinaTrushkina/sf_data_science/tree/main/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Этапы работы над проектом
1. Произведено считывание данных из файла и первичный анализ структуры данных
2. После этого сделаны преобразования для столбцов, чтобы их можно было анализировать и далее использовать для построения моделм
3. Проведен разведывательный анализ данных
   - выделены новые признаки
   - заполнены пропущенные данные
   - произведено кодирование категориальных признаков
   - проведен анализ значимости признаков для модели
   - проведен анализ корреляции
   - проведен отбор признаков
4. Построена модель для прогнозирования оценки отеля

:arrow_up:[к оглавлению](https://github.com/EkaterinaTrushkina/sf_data_science/tree/main/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Результаты
Проведен анализ, преобразование, очистка данных, проектирование модели предсказания отзывов.

:arrow_up:[к оглавлению](https://github.com/EkaterinaTrushkina/sf_data_science/tree/main/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Выводы
Получена модель предсказания рейтинга отелей, которую дальше можно использовать для проверки добросовестности отелей.
:arrow_up:[к оглавлению](https://github.com/EkaterinaTrushkina/sf_data_science/tree/main/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
