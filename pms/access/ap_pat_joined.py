'''
Created on Jan 21, 2014

@author: wzw7yn
'''
import sqlite3 as lite
import sys
from access.database import Database
from sqlbuilder import SqlInsertBuilder
from sqlbuilder import SqlUpdateBuilder
#from sqlbuilder import SqlSingleWhereBuilder
#from utils.configreader import ConfigReader

class AppointmentPatentTable(Database):

    db_path = ""

    IDX_TIME = 0
    IDX_PATENT_ID = 1
    IDX_APPOINTMENT_PERIOD = 2
    IDX_PAYMENT_ID = 3
    IDX_PATENT_ID = 4
    IDX_APPOINTMENT_ID = 5
    IDX_TITLE = 6
    IDX_FIRST_NAME = 7
    IDX_SURNAME = 8
    IDX_ADDRESS = 9
    IDX_TOWN = 10
    IDX_POST_CODE = 11
    IDX_HOME_PHONE = 12
    IDX_WORK_PHONE = 13
    IDX_MOBILE = 14
    IDX_PREFERED_PHONE = 15
    IDX_EMAIL = 16
    IDX_GENDER = 17
    IDX_NHS_NO = 18
    IDX_DATE_OF_BIRTH = 19
    IDX_GP_ID = 20

    @staticmethod
    def SetConfig(path):
        AppointmentPatentTable.db_path = path





    def select(self, selectStr, whereStr):
        select = 'select %s' + selectStr + ' from gps where %s ' % whereStr + ';'
        try:
            con = lite.connect(AppointmentPatentTable.db_path)
            cur = con.cursor();
            cur.execute(select)
            data = cur.fetchone()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            self.disconnect()

        return data[0]

    def get_id(self, first_name, surname):
        try:
            con = lite.connect(AppointmentPatentTable.db_path)

            cur = con.cursor();
            select = 'select gps_id from gps where first_name = \'%s\' ' % first_name + 'and surname = \'%s\'' % surname + ';'
            cur.execute(select)
            data = cur.fetchone()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            self.disconnect()

        return data[0]


    def remove(self, idx):

        select = 'delete from gps where gps_id = \'%s\' ' % idx + ';'
        try:
            con = lite.connect(AppointmentPatentTable.db_path)
            cur = con.cursor();
            cur.execute(select)
            con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            self.disconnect()

    def showAll(self):
        select = 'select * from Appointment, patent where Appointment.patent_id = patent.patent_id;'
        return self.execfetchall(select)

    def showItem(self, pid):
        select = 'select * from gps where gp_id = \'%s\' ' % pid + ';'
        return self.executeFetchone(select)

    def getItem(self, idx, data):
        return data[idx]

