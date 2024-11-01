# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from tokped_osa.tokped_table import Base,TokpedTable
from sqlalchemy.orm import Session

class TokpedOsaPipeline:
    def open_spider(self,item):
        self.engine=create_engine('postgresql://user1:user1@27.112.78.177:5430')
        Base.metadata.create_all(self.engine)
    
    def process_item(self, item, spider):
        item=ItemAdapter(item)
        if item['original_price']=="":
            item['original_price']='0'
        with Session(self.engine) as session:
            table=TokpedTable(name=item['name'],
                              url=item['url'],
                              stock=item['stock'],
                              count_sold=item['count_sold'],
                              rating=item['rating'],
                              review=item['review'],
                              price=item['price'],
                              original_price=item['original_price'],
                              shop_name=item['shop_name'],
                              category=item['category'])
            session.add(table)
            session.commit()
        return item
    
    def close_spider(self):
        try:
            with Session(self.engine) as session:
                session.commit()
                session.close()
        except:
            pass
