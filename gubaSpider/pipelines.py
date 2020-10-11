# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from gubaSpider.items import GubaspiderItem,ContentspiderItem,AuthorspiderItem


class GubaspiderPipeline(object):
    # 打开数据库
    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME','guba')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', '123456')

        self.db_conn =pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        if isinstance(item,ContentspiderItem):
            self.insert_content_db(item)
        elif isinstance(item,GubaspiderItem):
            self.insert_main_db(item)
        elif isinstance(item,AuthorspiderItem):
            self.insert_author_db(item)
        return item

    #插入数据
    def insert_main_db(self, item):
        values = (
            item['read_number'],
            item['command_number'],
            item['title'],
            item['title_url'],
            item['author'],
            item['author_url'],
            item['date']
        )
        try:
            sql = 'INSERT INTO main_info VALUES(%s,%s,%s,%s,%s,%s,%s)'
            self.db_conn.ping(reconnect=True)


            self.db_cur.execute(sql, values)
            self.db_conn.commit()

        except Exception as e :
            print(e)
            self.db_conn.commit()
            self.db_conn.close()


    def insert_content_db(self, item):
        values = (
            item['title_url'],
            item['content'],
        )
        try:
            sql = 'INSERT INTO content_info VALUES(%s,%s)'
            self.db_conn.ping(reconnect=True)
            self.db_cur.execute(sql, values)
            self.db_conn.commit()

        except Exception as e :
            print(e)
            self.db_conn.commit()
            self.db_conn.close()

    def insert_author_db(self, item):
        values = (
            item['author_url'],
            item['following_number'],
            item['follower_number']
        )
        try:
            sql = 'INSERT INTO author_info VALUES(%s,%s,%s)'
            self.db_conn.ping(reconnect=True)
            self.db_cur.execute(sql, values)
            self.db_conn.commit()

        except Exception as e :
            print(e)

            self.db_conn.commit()
            self.db_conn.close()
