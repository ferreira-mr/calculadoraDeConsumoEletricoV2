from peewee import SqliteDatabase, MySQLDatabase

# DATABASE_PATH = 'database.db'

# database = SqliteDatabase(DATABASE_PATH)

database = MySQLDatabase(
    database='calculadora_db',
    user='root',
    password='root',
    host='localhost',
    port=3306
)


def startup_db():
    database.connect()

    from models.bandeira import BandeiraDB
    from models.dependencia import DependenciaDB
    from models.dispositivo import DispositivoDB
    from models.tipo_consumidor import TipoConsumidorDB
    from models.tipo_dispositivo import TipoDispositivoDB
    from models.unidade_consumidora import UnidadeConsumidoraDB

    database.create_tables(
        [
            UnidadeConsumidoraDB,
            BandeiraDB,
            DependenciaDB,
            DispositivoDB,
            TipoConsumidorDB,
            TipoDispositivoDB,
        ]
    )


def shutdown_db():
    database.close()
