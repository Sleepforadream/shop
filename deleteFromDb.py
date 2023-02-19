from sqlalchemy import create_engine, MetaData, Table

# Создаем подключение к базе данных
engine = create_engine('sqlite:///shop.db')

# Создаем объект metadata
metadata = MetaData()

# Получаем список всех таблиц в базе данных
table_names = engine.table_names()

# Удаляем все записи из всех таблиц
for table_name in table_names:
    table = Table(table_name, metadata, autoload=True, autoload_with=engine)
    engine.execute(table.delete())