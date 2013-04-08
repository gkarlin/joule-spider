import psycopg2

class connection:
  def __init__(self):
    self.conn = psycopg2.connect(''' host=localhost user=postgres dbname=data password=lister''')
    self.cur = self.conn.cursor()
  def rollBack(self):
    self.conn.rollback()
  def execute(self,query):
    self.cur.execute(query)
  def closeAndSave(self):
    self.conn.commit()
    self.cur.close()
    self.conn.close()
