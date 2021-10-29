


from db.database import Database


class Run:

    def __init__(self):
        self.db = Database()
    
    def table_category(self):
        drop_table = " DROP TABLE IF EXISTS categories; "
        create_table = """ CREATE TABLE categories (
                            BestOfferEnabled integer,
                            AutoPayEnabled integer,
                            CategoryID integer PRIMARY KEY,
                            CategoryLevel integer,
                            CategoryName text,
                            CategoryParentID integer
                        ); """

        self.db.cursor.execute(drop_table)
        self.db.cursor.execute(create_table)