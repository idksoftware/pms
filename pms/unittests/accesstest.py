'''
Created on Jan 29, 2014

@author: wzw7yn
'''
import sys
import os
import unittest

from access.payment import PaymentTable
from access.database import Database
from utils.configreader import ConfigReader

from access.patent import PatentTable
from access.gp import GPTable
from access.appointment import AppointmentTable

import sys
from cStringIO import StringIO

real_stdout = sys.stdout
real_stderr = sys.stderr

sys.stdout = StringIO()
sys.stderr = StringIO()


class AccessTest(unittest.TestCase):
    def setUp(self):
        #rows = sys.path
        #for row in rows:
        #    print row

        cfg = ConfigReader()
        cfg.read("../config.xml")
        Database.Open(cfg.GetPath(), cfg.GetUsername(), cfg.GetPassword())

    def test00(self):
        ''' Initalise Table with date '''
        pa = PatentTable()
        pa.add("Steve", "Dean")
        pa.add("Stephen", "Bennett")
        pa.add("Stephen", "Brunton")
        pa.add("Simon", "Robinson")
        pa.add("Roger", "Smith")
        pa.add("Robert", "Poole")
        pa.add("Robert", "Gardner")
        pa.add("Richard", "Howell")
        pa.add("Richard", "Fewing")
        pa.add("Richard", "Carter")
        pa.add("Peter", "King")
        pa.add("Peter", "Connolly")
        pa.add("Paul", "Limb")
        pa.add("Paul", "Leeming")
        pa.add("Paul", "Hill")
        pa.add("Paul", "Arthurs")
        pa.add("Paul", "Bergin")


        pa.add("Paul", "Arnold")
        pa.add("Nigel", "Williams")
        pa.add("Neville", "Smith")
        pa.add("Neil", "Clark")
        pa.add("Mike T", "Robson")
        pa.add("Michael", "Peirce")
        pa.add("Max", "Borkowski")
        pa.add("Martin", "Kirby")
        pa.add("Mark", "Stanley")
        pa.add("Mark", "Ingram")
        pa.add("Mark", "Collins")
        pa.add("Malcolm", "Stenning")
        pa.add("Louis", "Kenney")
        pa.add("Leon", "Tanner")
        pa.add("Krystyn", "Rogers")
        pa.add("Kevin", "Ellwood")
        pa.add("Steve", "Kersley")
        pa.add("dave","fresdrickson" )

    def test01(self):
        ''' Selete all data '''
        pa = PatentTable()
        rows = pa.selectall()
        n = len(rows)
        assert n == 35, "Need to have 35 rows "



    def test02(self):
        ''' Select first name and surname '''
        pa = PatentTable()

        rows = pa.selectcols(idx=True, first_name=True, surname=True)
        for row in rows:
            print row
        #assert len(rows) == 0, "Table not empty"
    def test03(self):
        pa = PatentTable()
        idx = pa.get_id("Paul", "Limb")
        assert idx != None, "Item not found"
        row = pa.showItem(idx)
        print row
        #print pa.getItem(PatentTable.IDX_EMAIL, row)

    def test04(self):
        pa = PatentTable()

        for i in range(5,13):
            pa.update(i, work_phone='01444-129666', post_code='BN238BJ')

        where = pa.singlewhere(work_phone='01444-129666', post_code='BN238BJ')
        rows = pa.selectall(whereStr=where)
        for row in rows:
            print row

    def test09(self):
        ''' Delete all data '''
        pa = PatentTable()
        pa.deleteall()
        rows = pa.selectall()
        assert len(rows) == 0, "Table not empty"

    '''
    def testPaymentAdd(self):
        self.paymentTable = PaymentTable()
        self.paymentTable.add("1", "0", "38.50", "Y", "Y", "12 12 2013", "Y", "12 12 2013", "Y", "1234")
        self.rows = self.paymentTable.showAll()
        print self.rows
    '''

    def test30(self):
        ''' Initalise Table with date '''
        pa = GPTable()
        pa.add("Steve", "Dean")
        pa.add("Stephen", "Bennett")
        pa.add("Stephen", "Brunton")
        pa.add("Simon", "Robinson")
        pa.add("Roger", "Smith")
        pa.add("Robert", "Poole")
        pa.add("Robert", "Gardner")
        pa.add("Richard", "Howell")
        pa.add("Richard", "Fewing")
        pa.add("Richard", "Carter")
        pa.add("Peter", "King")
        pa.add("Peter", "Connolly")
        pa.add("Paul", "Limb")
        pa.add("Paul", "Leeming")
        pa.add("Paul", "Hill")
        pa.add("Paul", "Arthurs")
        pa.add("Paul", "Bergin")


        pa.add("Paul", "Arnold")
        pa.add("Nigel", "Williams")
        pa.add("Neville", "Smith")
        pa.add("Neil", "Clark")
        pa.add("Mike T", "Robson")
        pa.add("Michael", "Peirce")
        pa.add("Max", "Borkowski")
        pa.add("Martin", "Kirby")
        pa.add("Mark", "Stanley")
        pa.add("Mark", "Ingram")
        pa.add("Mark", "Collins")
        pa.add("Malcolm", "Stenning")
        pa.add("Louis", "Kenney")
        pa.add("Leon", "Tanner")
        pa.add("Krystyn", "Rogers")
        pa.add("Kevin", "Ellwood")
        pa.add("Steve", "Kersley")
        pa.add("dave","fresdrickson" )

    def test31(self):
        ''' Selete all data '''
        pa = GPTable()
        rows = pa.selectall()
        n = len(rows)
        assert n == 35, "Need to have 35 rows "



    def test32(self):
        ''' Select first name and surname '''
        pa = GPTable()

        rows = pa.selectcols(idx=True, first_name=True, surname=True)
        for row in rows:
            print row
        #assert len(rows) == 0, "Table not empty"
    def test33(self):
        pa = GPTable()
        idx = pa.get_id("Paul", "Limb")
        assert idx != None, "Item not found"
        row = pa.showItem(idx)
        print row
        #print pa.getItem(PatentTable.IDX_EMAIL, row)

    def test34(self):
        pa = GPTable()

        for i in range(5,13):
            pa.update(i, home_phone='01444-241048')

        where = pa.singlewhere(work_phone='01444-241048')
        rows = pa.selectall(whereStr=where)
        for row in rows:
            print row

    def test39(self):
        ''' Delete all data '''
        pa = GPTable()
        pa.deleteall()
        rows = pa.selectall()
        assert len(rows) == 0, "Table not empty"

    def test50(self):
        ''' Initalise Table with date '''
        a = AppointmentTable()
        a.add('25-01-2014 11:30',20,30,12)
        a.add('25-01-2014 12:30',1,30,12)
        a.add('25-01-2014 13:30',2,30,12)
        a.add('25-01-2014 14:00',4,30,12)
        a.add('25-01-2014 14:30',5,30,12)
        a.add('25-01-2014 15:00',7,30,12)
        a.add('25-01-2014 15:30',8,30,12)
        a.add('25-01-2014 16:00',11,30,12)
        a.add('25-01-2014 16:30',13,30,12)
        a.add('25-01-2014 17:30',14,30,12)

    def test51(self):
        ''' Selete all data '''
        pa = AppointmentTable()
        rows = pa.selectall()
        n = len(rows)
        assert n == 10, "Need to have 35 rows "



    def test52(self):
        ''' Select first name and surname '''
        pa = AppointmentTable()

        rows = pa.selectcols(time=True, patent_id=True, payment_id=True)
        for row in rows:
            print row
        #assert len(rows) == 0, "Table not empty"
    def test53(self):
        pa = AppointmentTable()
        idx = pa.get_id(time='25-01-2014 16:00')
        assert idx != None, "Item not found"
        row = pa.showItem(idx)
        print row
        #print pa.getItem(PatentTable.IDX_EMAIL, row)

    def test54(self):
        pa = AppointmentTable()

        for i in range(5,13):
            pa.update(i, appointment_id=str(i+200))

        where = pa.singlewhere(appointment_id='200')
        rows = pa.selectall(whereStr=where)
        for row in rows:
            print row

    def test59(self):
        ''' Delete all data '''
        pa = AppointmentTable()
        pa.deleteall()
        rows = pa.selectall()
        assert len(rows) == 0, "Table not empty"
        
    def test70(self):
        ''' Initalise Table with date '''
        '''
        payment_id,
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
        '''
        a = PaymentTable()
        a.add(10,20,38.50,1)
        a.add(11,23,38.50,1)
        a.add(12,24,38.50,1)
        a.add(13,26,38.50,1)
        a.add(14,27,38.50,1)
        a.add(15,28,38.50,1)
        a.add(16,34,38.50,1)
        a.add(17,35,38.50,1)
       
    def test71(self):
        ''' Selete all data '''
        pa = PaymentTable()
        rows = pa.selectall()
        n = len(rows)
        assert n == 8, "Need to have 8 rows "



    def test72(self):
        ''' Select first name and surname '''
        pa = PaymentTable()

        rows = pa.selectcols(payment_id=True, patent_id=True, amount=True)
        for row in rows:
            print row
        #assert len(rows) == 0, "Table not empty"
    def test73(self):
        pa = PaymentTable()
        idx = pa.get_id(34)
        assert idx != None, "Item not found"
        row = pa.showItem(idx)
        print row
        #print pa.getItem(PatentTable.IDX_EMAIL, row)

    def test74(self):
        pa = PaymentTable()

        for i in range(5,13):
            pa.update(i, appointment_id=str(i+200))

        where = pa.singlewhere(appointment_id='200')
        rows = pa.selectall(whereStr=where)
        for row in rows:
            print row

    def test79(self):
        ''' Delete all data '''
        pa = PaymentTable()
        pa.deleteall()
        rows = pa.selectall()
        assert len(rows) == 0, "Table not empty"

def patenttable_suite():
    suite = unittest.TestSuite()
    suite.addTest(AccessTest("test00"))
    suite.addTest(AccessTest("test01"))
    suite.addTest(AccessTest("test02"))
    suite.addTest(AccessTest("test03"))
    suite.addTest(AccessTest("test04"))
    suite.addTest(AccessTest("test09"))
    return suite

def gptable_suite():
    suite = unittest.TestSuite()
    suite.addTest(AccessTest("test30"))
    suite.addTest(AccessTest("test31"))
    suite.addTest(AccessTest("test32"))
    suite.addTest(AccessTest("test33"))
    suite.addTest(AccessTest("test34"))
    suite.addTest(AccessTest("test39"))
    return suite

def appointmenttable_suite():
    suite = unittest.TestSuite()
    suite.addTest(AccessTest("test50"))
    suite.addTest(AccessTest("test51"))
    suite.addTest(AccessTest("test52"))
    suite.addTest(AccessTest("test53"))
    suite.addTest(AccessTest("test54"))
    suite.addTest(AccessTest("test59"))
    return suite

def paymenttable_suite():
    suite = unittest.TestSuite()
    suite.addTest(AccessTest("test70"))
    suite.addTest(AccessTest("test71"))
    suite.addTest(AccessTest("test72"))
    suite.addTest(AccessTest("test73"))
    suite.addTest(AccessTest("test74"))
    suite.addTest(AccessTest("test79"))
    return suite

def main():

    try:

        print "Appointment Tests"
        unittest.TextTestRunner(verbosity=1).run(appointmenttable_suite())

        print "Patent Tests"
        unittest.TextTestRunner(verbosity=1).run(patenttable_suite())

        print "GP Tests"
        unittest.TextTestRunner(verbosity=1).run(gptable_suite())
        
        print "Payment Tests"
        unittest.TextTestRunner(verbosity=1).run(paymenttable_suite())

    finally:
        # Display the test harness output
        real_stdout.write(sys.stdout.getvalue())
        real_stderr.write(sys.stderr.getvalue())


if __name__ == '__main__':

    main()