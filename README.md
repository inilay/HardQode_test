### ER диаграмма спроектированной базы данных 

![ER](https://github.com/inilay/HardQode_test/blob/master/DataBaseER.png)

### API
- Для отображения всех продуктов пользователя: **api/v1/user_products/<int:id>/**

где <int:id> - id пользователя, все продукты профиля может просматривать владелец или администратор

- Для отображения конкретного продукта пользователя **api/v1/product/<int:id>/**

где <int:id> - id продукта

- Для отображения статистики по продуктам **api/v1/products/**

###  Запуск

```sh 
docker run --name=indiora_hardqode_test --rm -p 8000:8000 $(docker build -q .)
```
