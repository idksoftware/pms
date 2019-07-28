'''
Created on Jan 21, 2014

@author: wzw7yn
'''
import sqlite3 as lite
import sys
from access.database import Database
from sqlbuilder import SqlSelectBuilder
from sqlbuilder import SqlInsertBuilder
from sqlbuilder import SqlUpdateBuilder
from sqlbuilder import SqlSingleWhereBuilder


class AppointmentTable(Database):

    db_path = ""

    IDX_TIME = 0
    IDX_PATENT_ID = 1
    IDX_APPOINTMENT_PERIOD = 2
    IDX_PAYMENT_ID = 3
    IDX_APPOINTMENT_ID = 4

    @staticmethod
    def SetConfig(path):
        AppointmentTable.db_path = path

    def add(self, time,
                  patent_id=None,
                  appointment_period=None,
                  payment_id=None,
                  appointment_id=None
                  ):


        builder = SqlInsertBuilder()
        builder.addfield(time, "time");
        builder.addfield(patent_id, "patent_id");
        builder.addfield(appointment_period, "appointment_period");
        builder.addfield(payment_id, "payment_id");
        builder.addfield(appointment_id, "appointment_id");


        select = 'insert into appointment (' + builder.getTokenString() + ') values (' + builder.getValueString() + ');'
        self.execcmd(select)

    '''
    def updatelist(self, time, changes):



        builder = SqlUpdateBuilder()

        for item in changes:

            if item == AppointmentTable.IDX_PATENT_ID:
                builder.addfield(changes[item], "patent_id")
            if item == AppointmentTable.IDX_APPOINTMENT_PERIOD:
                builder.addfield(changes[item], "appointment_period")
            if item == AppointmentTable.IDX_PATENT_ID:
                builder.addfield(changes[item], "payment_id")



        select = 'update gps set ' + builder.getValueString() + ' where gp_id = \'%s\' ' % time + ';'
        self.execcmd(select)
    '''

    def update(self, time,
                     patent_id=None,
                     appointment_period=None,
                     payment_id=None,
                     appointment_id=None
                     ):


        builder = SqlUpdateBuilder()

        builder.addfield(patent_id, "patent_id");
        builder.addfield(appointment_period, "appointment_period");
        builder.addfield(payment_id, "payment_id");
        builder.addfield(appointment_id, "appointment_id");

        select = 'update appointment set ' + builder.getValueString() + ' where appointment_id = \'%s\' ' % time + ';'
        self.execcmd(select)

    def singlewhere(self,
                    time=None,
                    patent_id=None,
                    appointment_period=None,
                    payment_id=None,
                    appointment_id=None
                    ):

        builder = SqlSingleWhereBuilder()
        builder.addfield(time, "time");
        builder.addfield(patent_id , "patent_id");
        builder.addfield(appointment_period , "appointment_period");
        builder.addfield(payment_id , "payment_id");
        builder.addfield(appointment_id , "appointment_id");

        return builder.getValueString()

    def selectcolstr(self,
                     time=False,
                     patent_id=False,
                     appointment_period=False,
                     payment_id=False,
                     appointment_id=False
                        ):

        builder = SqlSelectBuilder()
        builder.addfield(time, "time");
        builder.addfield(patent_id, "patent_id");
        builder.addfield(appointment_period , "appointment_period");
        builder.addfield(payment_id , "payment_id");
        builder.addfield(appointment_id , "appointment_id");

        return builder.tostr()

    def selectcols(self,
                    time=False,
                    patent_id=False,
                    appointment_period=False,
                    payment_id=False,
                    appointment_id=False
                        ):

        selectstr = self.selectcolstr(
                    time,
                    patent_id,
                    appointment_period,
                    payment_id,
                    appointment_id
                         )

        if selectstr == None:
            select = 'select * from appointment;'
        else:
            select = 'select ' + selectstr + ' from appointment;'
        return self.execfetchall(select)

    # obsolete
    def select(self, selectStr, whereStr):
        select = 'select %s' + selectStr + ' from appointment where %s ' % whereStr + ';'
        return self.execfetchone(select)

    def selectone(self, selectStr=None, whereStr=None):
        select = self._selectstr('appointment', selectStr, whereStr)
        return self.execfetchone(select)

    def selectall(self, selectStr=None, whereStr=None):
        select = self._selectstr('appointment', selectStr, whereStr)
        return self.execfetchall(select)

    def deleteall(self):
        self._deleteall('appointment')

    def get_id(self, time):
        select = 'select appointment_id from appointment where time = \'%s\' ' % time + ';'
        return self.execfetchone(select)


    def remove(self, idx):
        self._remove('appointment', 'appointment_id', idx)

    def showAll(self):
        return self._showAll('appointment')

    def showItem(self, pid):
        return self._showItem('appointment', 'appointment_id', pid)

    def getItem(self, idx, data):
        return data[idx]


