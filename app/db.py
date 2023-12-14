# модель создания pydantic и таблици SQLAlchemy
import databases
import ormar
import sqlalchemy
# забрать из файла конфиг настройки
from .config import settings
# создаем обект класса Database  и устанавливаем ему bdb_url
database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    # создается подкласс?????
    class Meta(BaseMeta):
        tablename = "users"
    # создание столюцов таблици и утсновка ограничений на их поляи значения по умолчанию
    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    active: bool = ormar.Boolean(default=True, nullable=False)

# создание экземпляра класса engine с параметрами setitings
engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)