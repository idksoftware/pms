'''
Created on Jan 28, 2014

@author: wzw7yn
'''
import sqlite3 as lite
import sys
from access.database import Database
from sqlbuilder import SqlSelectBuilder
from sqlbuilder import SqlInsertBuilder
from sqlbuilder import SqlUpdateBuilder
from sqlbuilder import SqlSingleWhereBuilder


class PaymentTable(Database):

    db_path = ""
    '''
    payment_id              integer primary key,
    patent_id               integer,
    appointment_id          integer,
    amount                  float,
    paid                    char(1),
    paid_at_apointment      char(1),
    date_paid               date,
    invoiced                char(1),
    date_invoiced           date,
    billed_to_other         char(1),
    billed_to_id            integer

     payment_id
    patent_id
    appointment_id
    amount
    paid
    paid_at_apointment
    date_paid
    invoiced
    date_invoiced
    billed_to_other
    billed_to_id

    '''

    IDX_PAYMENT_ID              = 0,
    IDX_PATENT_ID               = 1,
    IDX_APPOINTMENT_ID          = 2,
    IDX_AMOUNT                  = 3,
    IDX_PAID                    = 4,
    IDX_PAID_AT_APOINTMENT      = 5,
    IDX_DATE_PAID               = 6,
    IDX_INVOICED                = 7,
    IDX_DATE_INVOICED           = 8,
    IDX_BILLED_TO_OTHER         = 9,
    IDX_BILLED_TO_ID            = 10

    @staticmethod
    def SetConfig(path):
        PaymentTable.db_path = path

    def add(self,
                  patent_id=None,
                  appointment_id=None,
                  amount=None,
                  paid=None,
                  paid_at_apointment=None,
                  date_paid=None,
                  invoiced=None,
                  date_invoiced=None,
                  billed_to_other=None,
                  billed_to_id=None
                  ):


        builder = SqlInsertBuilder()
        builder.addfield( patent_id , "patent_id");
        builder.addfield( appointment_id , "appointment_id");
        builder.addfield( amount , "amount");
        builder.addfield( paid , "paid");
        builder.addfield( paid_at_apointment , "paid_at_apointment");
        builder.addfield( date_paid , "date_paid");
        builder.addfield( invoiced , "invoiced");
        builder.addfield( date_invoiced , "date_invoiced");
        builder.addfield( billed_to_other , "billed_to_other");
        builder.addfield( billed_to_id , "billed_to_id");

        select = 'insert into payment (' + builder.getTokenString() + ') values (' + builder.getValueString() + ');'
        self.execcmd(select)

    '''
    def updatelist(self, time, changes):



        builder = SqlUpdateBuilder()

        for item in changes:

            if item == PaymentTable.IDX_PATENT_ID:
                builder.addfield(changes[item], "patent_id")
            if item == PaymentTable.IDX_APPOINTMENT_PERIOD:
                builder.addfield(changes[item], "appointment_period")
            if item == PaymentTable.IDX_PATENT_ID:
                builder.addfield(changes[item], "payment_id")



        select = 'update gps set ' + builder.getValueString() + ' where gp_id = \'%s\' ' % time + ';'
        self.execcmd(select)
    '''

    def update(self, payment_id,
                  patent_id=None,
                  appointment_id=None,
                  amount=None,
                  paid=None,
                  paid_at_apointment=None,
                  date_paid=None,
                  invoiced=None,
                  date_invoiced=None,
                  billed_to_other=None,
                  billed_to_id=None
                  ):


        builder = SqlUpdateBuilder()
        builder.addfield( payment_id , "payment_id");
        builder.addfield( patent_id , "patent_id");
        builder.addfield( appointment_id , "appointment_id");
        builder.addfield( amount , "amount");
        builder.addfield( paid , "paid");
        builder.addfield( paid_at_apointment , "paid_at_apointment");
        builder.addfield( date_paid , "date_paid");
        builder.addfield( invoiced , "invoiced");
        builder.addfield( date_invoiced , "date_invoiced");
        builder.addfield( billed_to_other , "billed_to_other");
        builder.addfield( billed_to_id , "billed_to_id");

        select = 'update payment set ' + builder.getValueString() + ' where payment_id = \'%s\' ' % payment_id + ';'
        self.execcmd(select)

    def singlewhere(self,
                  payment_id=None,
                  patent_id=None,
                  appointment_id=None,
                  amount=None,
                  paid=None,
                  paid_at_apointment=None,
                  date_paid=None,
                  invoiced=None,
                  date_invoiced=None,
                  billed_to_other=None,
                  billed_to_id=None
                  ):

        builder = SqlSingleWhereBuilder()
        builder.addfield( payment_id , "payment_id");
        builder.addfield( patent_id , "patent_id");
        builder.addfield( appointment_id , "appointment_id");
        builder.addfield( amount , "amount");
        builder.addfield( paid , "paid");
        builder.addfield( paid_at_apointment , "paid_at_apointment");
        builder.addfield( date_paid , "date_paid");
        builder.addfield( invoiced , "invoiced");
        builder.addfield( date_invoiced , "date_invoiced");
        builder.addfield( billed_to_other , "billed_to_other");
        builder.addfield( billed_to_id , "billed_to_id");

        return builder.getValueString()

    def selectcolstr(self,
                  payment_id=None,
                  patent_id=None,
                  appointment_id=None,
                  amount=None,
                  paid=None,
                  paid_at_apointment=None,
                  date_paid=None,
                  invoiced=None,
                  date_invoiced=None,
                  billed_to_other=None,
                  billed_to_id=None
                        ):

        builder = SqlSelectBuilder()
        builder.addfield( payment_id , "payment_id");
        builder.addfield( patent_id , "patent_id");
        builder.addfield( appointment_id , "appointment_id");
        builder.addfield( amount , "amount");
        builder.addfield( paid , "paid");
        builder.addfield( paid_at_apointment , "paid_at_apointment");
        builder.addfield( date_paid , "date_paid");
        builder.addfield( invoiced , "invoiced");
        builder.addfield( date_invoiced , "date_invoiced");
        builder.addfield( billed_to_other , "billed_to_other");
        builder.addfield( billed_to_id , "billed_to_id");

        return builder.tostr()

    def selectcols(self, payment_id=False,
                  patent_id=False,
                  appointment_id=False,
                  amount=False,
                  paid=False,
                  paid_at_apointment=False,
                  date_paid=False,
                  invoiced=False,
                  date_invoiced=False,
                  billed_to_other=False,
                  billed_to_id=False
                         ):

        selectstr = self.selectcolstr(payment_id,
                  patent_id,
                  appointment_id,
                  amount,
                  paid,
                  paid_at_apointment,
                  date_paid,
                  invoiced,
                  date_invoiced,
                  billed_to_other,
                  billed_to_id
                         )

        if selectstr == None:
            select = 'select * from gps;'
        else:
            select = 'select ' + selectstr + ' from payment;'
        return self.execfetchall(select)

    # obsolete
    def select(self, selectStr, whereStr):
        select = 'select %s' + selectStr + ' from payment where %s ' % whereStr + ';'
        return self.execfetchone(select)
    def selectone(self, selectStr=None, whereStr=None):
        select = self._selectstr('payment', selectStr, whereStr)
        return self.execfetchone(select)

    def selectall(self, selectStr=None, whereStr=None):
        select = self._selectstr('payment', selectStr, whereStr)
        return self.execfetchall(select)

    def deleteall(self):
        self._deleteall('payment')

    def get_id(self, appointment_id):
        select = 'select payment_id from payment where appointment_id = \'%s\' ' % appointment_id + ';'
        return self.execfetchone(select)

    def remove(self, idx):
        self._remove('payment', 'payment_id', idx)

    def showAll(self):
        return self._showAll('payment')

    def showItem(self, pid):
        return self._showItem('payment', 'payment_id', pid)


    def getItem(self, idx, data):
        return data[idx]



