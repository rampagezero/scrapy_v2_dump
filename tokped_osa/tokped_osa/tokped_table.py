from sqlalchemy.orm import Mapped,DeclarativeBase
from sqlalchemy import DateTime,Column,Integer,Text
from sqlalchemy.sql import func
import datetime
class Base(DeclarativeBase):
    pass
class TokpedTable(Base):
    __tablename__='TokpedData'
    id=Column(Integer,primary_key=True,auto_increment=True)
    name:Mapped[str]
    url:Mapped[str]
    count_sold:Mapped[str]
    stock:Mapped[str]
    rating:Mapped[int]
    review:Mapped[str]
    price:Mapped[str]
    original_price:Mapped[str]=Column(Text,default=None)
    shop_name:Mapped[str]
    category:Mapped[str]
    date:Mapped[datetime.datetime]= Column(DateTime(timezone=True), server_default=func.now())
