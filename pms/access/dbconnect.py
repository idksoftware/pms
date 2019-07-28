'''
Created on Jan 3, 2014

@author: wzw7yn
'''
import sqlite3 as lite
import sys



class DBConnect():


    _single = None
    _version_data = ""

    def __init__(self):
        self.con = None

        if DBConnect._single:
            raise DBConnect._single
        DBConnect._single = self


    @staticmethod
    def Instance():
        if DBConnect._single:
                return DBConnect._single
        DBConnect._single = DBConnect()
        return DBConnect._single

    def open(self):
        try:
            con = lite.connect('/home/wzw7yn/poditry.db')

            cur = con.cursor();
            cur.execute('SELECT SQLITE_VERSION()')
            _version_data = cur.fetchone()


        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)



