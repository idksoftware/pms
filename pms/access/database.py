'''
Created on Jan 13, 2014

@author: wzw7yn
'''
import sqlite3 as lite
import sys
import wx

class DBAttribDef:

    def __init__(self, lable, valueType, default=None, maxValue=None, minValue=None, pkey=False ):

        self.lable= lable
        self.valueType = valueType
        self.max = maxValue
        self.min = minValue
        self.default = default
        self.pkey = pkey

    '''
    def __init__(self, lable, valueType):

        self.lable= lable
        self.valueType = valueType
        self.max = None
        self.min = None
        self.default = None
        self.pkey = None
    '''
    def GetLable(self):
        return self.lable

    def GetDefault(self):
        return self.default

    def GetValeType(self):
        return self.valueType
    
    def IsPKey(self):
        return self.pkey

class Attrib:


    def __init__(self, dbAttribDef, text):
        self.dbAttribDef = dbAttribDef
        self.text = text
        self.ctrl = None

    def SetCtrl(self, ctrl):
        self.ctrl = ctrl

    def GetCtrl(self):
        return self.ctrl

    def IsChanged(self):
        if self.ctrl == None:
            return False
        typeStr = self.dbAttribDef.GetValeType()
        if typeStr == 'str':
            if self.text != self.ctrl.GetValue():
                return True
        elif typeStr == 'date':
            date = wx.DateTime()
            date.ParseDate(self.text)
            if date != self.ctrl.GetValue():
                return True
        elif typeStr == 'int':
            if self.text != str(self.ctrl.GetValue()):
                return True
        return False

    def GetCurText(self):
        if self.dbAttribDef.IsPKey():
            return self.text
        
        if self.IsChanged() == True:
            typeStr = self.dbAttribDef.GetValeType()
            if typeStr == 'str':
                return self.ctrl.GetValue()
            elif typeStr == 'date':
                date = self.ctrl.GetValue()
                return str(date)
            elif typeStr == 'int':
                return str(self.GetText())

    def GetText(self):
        typeStr = self.dbAttribDef.GetValeType()
        if self.ctrl != None:
            typeStr = self.dbAttribDef.GetValeType()
            if typeStr == 'int':
                return str(self.ctrl.GetValue())
            return self.ctrl.GetValue()
        if self.text == None:
            if self.dbAttribDef.GetDefault() == None:
                return ""
            else:
                return self.dbAttribDef.GetDefault()
        else:
            if typeStr == 'int':
                return str(self.text)
            return self.text

    def GetDef(self):
        return self.dbAttribDef

class DBTableDef:

    def __init__(self):
        self.list = list()

    def Add(self, lable, valueType, default=None, maxValue=None, minValue=None, pkey=False ):
        attr = DBAttribDef(lable, valueType, default, max, min, pkey)
        self.list.append(attr)

    def GetAttribs(self):
        return self.list


class DBRow:

    def __init__(self, attrList):
        self.attrList = attrList

    def GetAttr(self, lable):
        for attr in self.attrList:
            lstr = attr.GetDef().GetLable()
            if lstr == lable:
                return attr

class DBTable:
    def __init__(self, dbTableItemDef):
        self.dbTableItemDef = dbTableItemDef



    def GetRow(self, row):
        deflist = self.dbTableItemDef.GetAttribs()
        attrlist = list()
        i = 0;
        for item in deflist:
            attrlist.append(Attrib(item,row[i]))
            i = i + 1
        arow = DBRow(attrlist)
        return arow

    def Set(self, idx, text, ctrl):
        self.row[idx].text = text
        self.row[idx].ctrl = ctrl

    def updateList(self):
        self.changeList = {}
        i = 0
        for item in self.row:
            if item.IsChanged():
                self.changeList[i] = item.GetText()
            i = i + 1
        return self.changeList

class Database():


    db_path = None
    db_username = None
    db_password = None
    db_con = None

    @staticmethod
    def Open(path, user, pw):
        Database.db_path = path
        Database.db_username = user
        Database.db_password = pw


    @staticmethod
    def GetPath(self):
        return Database.db_path

    @staticmethod
    def GetUsername(self):
        return Database.db_username

    @staticmethod
    def GetPassword(self):
        return Database.db_password

    def connect(self):
        if Database.db_con != None:
            return Database.db_con
        try:
            Database.db_con = lite.connect(Database.db_path)
            #cur = Database.db_con.cursor();
            #cur.execute('SELECT SQLITE_VERSION()')
            #data = cur.fetchone()
            #print "SQLite version: %s" % data
            return Database.db_con

        except lite.Error, e:
            print "Database Error %s:" % e.args[0]
            sys.exit(1)


    def disconnect(self):
        if Database.db_con != None:
            Database.db_con.close()
            Database.db_con = None

    def _selectstr(self, table, selectStr=None, whereStr=None):
        select = None
        if whereStr == None:
            if selectStr == None:
                select = 'select * from ' + table + ';'
            else:
                select = 'select %s' + selectStr + ' from ' + table + ';'
        else:
            if selectStr == None:
                select = 'select * from ' + table + ' where %s ' % whereStr + ';'
            else:
                select = 'select %s' + selectStr + ' from ' + table + ' where %s ' % whereStr + ';'

        return select

    def _deleteall(self, table):
        cmd = 'delete from ' + table + ';'
        self.execcmd(cmd)

    def _get_id(self, table, tid, first_name, surname):
        select = 'select ' + tid + ' from ' + table + ' where first_name = \'%s\' ' % first_name + 'and surname = \'%s\'' % surname + ';'
        return self.execfetchone(select)

    def _remove(self, table, tid, idx):
        select = 'delete from ' + table + ' where ' + tid + ' = \'%s\' ' % idx + ';'
        self.execcmd(select)

    def _showAll(self, table):
        select = 'select * from ' + table + ';'
        return self.execfetchall(select)

    def _showItem(self, table, tid, pid):
        select = 'select * from ' + table + ' where ' + tid + ' = \'%s\' ' % pid + ';'
        return self.execfetchone(select)

    def _getItem(self, idx, data):
        return data[idx]

    def selectall(self, selectStr):

        try:
            con = self.connect()
            cur = con.cursor();
            cur.execute(selectStr)
            data = cur.fetchall()
        except lite.Error, e:
            print "Database Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            self.disconnect()

        return data

    def execfetchall(self,cmd):

        try:
            con = self.connect()
            cur = con.cursor();
            cur.execute(cmd)
            rows = cur.fetchall()
            con.commit()
            return rows

        except lite.Error, e:
            print "Database Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            self.disconnect()

    def execfetchone(self, cmd):
        try:
            con = self.connect()
            cur = con.cursor();
            cur.execute(cmd)
            rows = cur.fetchone()
            con.commit()
            return rows

        except lite.Error, e:
            print "Database Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            self.disconnect()



    def execcmd(self, cmd):
        try:
            con = self.connect()
            cur = con.cursor();
            cur.execute(cmd)
            con.commit()

        except lite.Error, e:
            print "Database Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            self.disconnect()
