
from sqlite3.dbapi2 import Error
from db.database import Database

class Category:

    def __init__(self):
        self.db = Database()
        self.bestofferenabled = 0
        self.autopayenabled = 0
        self.categoryid = 0
        self.categorylevel = 0
        self.categoryname = None
        self.categoryparentid = 0

        
    def value_category(self, category):
        model = self
        if hasattr(category, "BestOfferEnabled"):
            model.bestofferenabled = category.BestOfferEnabled.text
        if hasattr(category, "AutoPayEnabled"):
            model.autopayenabled = category.AutoPayEnabled.text
        if hasattr(category, "CategoryID"):
            model.categoryid = category.CategoryID.text
        if hasattr(category, "CategoryLevel"):
            model.categorylevel = category.CategoryLevel.text
        if hasattr(category, "CategoryName"):
            model.categoryname = category.CategoryName.text
        if hasattr(category, "CategoryParentID"):
            model.categoryparentid = category.CategoryParentID.text
        
        return model


    def get_category(self, category):
        self.db.cursor.execute("""
            SELECT CategoryID, CategoryName, CategoryLevel, CategoryParentID, BestOfferEnabled
            FROM categories
            WHERE CategoryID = ?
        """, (category,))

        return self.db.cursor.fetchone()


    def valide_category(self, category):
        self.db.cursor.execute("SELECT * FROM categories WHERE CategoryID = ?", (category,))
        return self.db.cursor.fetchone()
    
    
    def valide_table(self):
        try:
            self.db.cursor.execute("SELECT EXISTS(SELECT count(*) FROM categories);")
            return self.db.cursor.fetchone()
        except Error:
            return False


    def get_categories(self, id):
        self.db.cursor.execute("""
            SELECT CategoryID, CategoryName, CategoryLevel, CategoryParentID, BestOfferEnabled
            FROM categories
            WHERE CategoryParentID = ? AND CategoryID <> CategoryParentID
            ORDER BY CategoryLevel, CategoryID
        """, (id,))
        
        return self.db.cursor.fetchall()

    def create_categories(self, rows):
        self.db.cursor.executemany('INSERT INTO categories VALUES(?,?,?,?,?,?)', rows)
        self.db.connection.commit()