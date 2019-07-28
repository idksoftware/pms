'''
Created on Jan 15, 2014

@author: wzw7yn
'''
'''
This manages the in-memory copy of the database table.
the table consists of rows. each row contains columns
the first column is normaly the row index. This is used to
update the any changed rows
'''
class RowManager:

    def __init__(self,rows):
        self.rows = rows

    def Get(self):
        return self.rows

    def update(self, newrow):
        idx = newrow[0]
        i = 0
        for row in self.rows:
            if row[0] == idx:
                self.rows.pop(i)
                self.rows.insert(i,newrow)
            i = i + 1