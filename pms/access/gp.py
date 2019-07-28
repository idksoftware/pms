'''
Created on Jan 3, 2014

@author: wzw7yn
'''
import sqlite3 as lite
import sys
from access.database import Database
from sqlbuilder import SqlSelectBuilder
from sqlbuilder import SqlInsertBuilder
from sqlbuilder import SqlUpdateBuilder
from sqlbuilder import SqlSingleWhereBuilder



class GPAttrib:


    def __init__(self):
        self.text = ''
        self.ctrl = None

    def IsChanged(self):
        if self.ctrl == None:
            return False
        if self.text != self.ctrl.GetValue():
            return True
        return False

    def GetText(self):
        if self.ctrl == None:
            return False
        return self.ctrl.GetValue()


class GPTableData:
    def __init__(self):
        self.row = list()
        for i in range(0, 12):
            self.row.append(GPAttrib())

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


class GPTable(Database):

    db_path = ""

    IDX_GP_ID = 0
    IDX_TITLE = 1
    IDX_FIRST_NAME = 2
    IDX_SURNAME = 3
    IDX_ADDRESS = 4
    IDX_TOWN = 5
    IDX_POST_CODE = 6
    IDX_HOME_PHONE = 7
    IDX_WORK_PHONE = 8
    IDX_MOBILE = 9
    IDX_PREFERED_PHONE = 10
    IDX_EMAIL = 11


    @staticmethod
    def SetConfig(path):
        GPTable.db_path = path

    def add(self, first_name, surname,
                                address=None,
                                town=None,
                                post_code=None,
                                home_phone=None,
                                work_phone=None,
                                mobile=None,
                                prefered_phone=None,
                                email=None):


        builder = SqlInsertBuilder()
        builder.addfield(first_name, "first_name");
        builder.addfield(surname, "surname");
        builder.addfield(address, "address");
        builder.addfield(town, "town");
        builder.addfield(post_code, "post_code");
        builder.addfield(home_phone, "home_phone");
        builder.addfield(work_phone, "work_phone");
        builder.addfield(mobile, "mobile");
        builder.addfield(prefered_phone, "prefered_phone");
        builder.addfield(email, "email");

        select = 'insert into gps (' + builder.getTokenString() + ') values (' + builder.getValueString() + ');'
        self.execcmd(select)

    '''
    def updatelist(self, idx, changes):



        builder = SqlUpdateBuilder()

        for item in changes:
            if item == GPTable.IDX_TITLE:
                builder.addfield(changes[item], "title")
            if item == GPTable.IDX_FIRST_NAME:
                builder.addfield(changes[item], "first_name")
            if item == GPTable.IDX_SURNAME:
                builder.addfield(changes[item], "surname")
            if item == GPTable.IDX_ADDRESS:
                builder.addfield(changes[item], "address")
            if item == GPTable.IDX_TOWN:
                builder.addfield(changes[item], "town")
            if item == GPTable.IDX_POST_CODE:
                builder.addfield(changes[item], "post_code")
            if item == GPTable.IDX_HOME_PHONE:
                builder.addfield(changes[item], "home_phone")
            if item == GPTable.IDX_WORK_PHONE:
                builder.addfield(changes[item], "work_phone")
            if item == GPTable.IDX_MOBILE:
                builder.addfield(changes[item], "mobile")
            if item == GPTable.IDX_PREFERED_PHONE:
                builder.addfield(changes[item], "prefered_phone")
            if item == GPTable.IDX_EMAIL:
                builder.addfield(changes[item], "email")


        select = 'update gps set ' + builder.getValueString() + ' where gp_id = \'%s\' ' % idx + ';'
        self.execcmd(select)
    '''

    def update(self, idx,
                    first_name=None,
			 		surname=None,
                    address=None,
                    town=None,
                    post_code=None,
                         home_phone=None,
                         work_phone=None,
                         mobile=None,
                         prefered_phone=None,
                         email=None):



        builder = SqlUpdateBuilder()
        builder.addfield(first_name, "first_name");
        builder.addfield(surname , "surname");
        builder.addfield(address , "address");
        builder.addfield(town , "town");
        builder.addfield(post_code , "post_code");
        builder.addfield(home_phone , "home_phone");
        builder.addfield(work_phone , "work_phone");
        builder.addfield(mobile , "mobile");
        builder.addfield(prefered_phone , "prefered_phone");
        builder.addfield(email , "email");

        select = 'update gps set ' + builder.getValueString() + ' where gp_id = \'%s\' ' % idx + ';'
        self.execcmd(select)

    def singlewhere(self, first_name=None,
                        surname=None,
                        address=None,
                         town=None,
                         post_code=None,
                         home_phone=None,
                         work_phone=None,
                         mobile=None,
                         prefered_phone=None,
                         email=None):

        builder = SqlSingleWhereBuilder()
        builder.addfield(first_name, "first_name");
        builder.addfield(surname , "surname");
        builder.addfield(address , "address");
        builder.addfield(town , "town");
        builder.addfield(post_code , "post_code");
        builder.addfield(home_phone , "home_phone");
        builder.addfield(work_phone , "work_phone");
        builder.addfield(mobile , "mobile");
        builder.addfield(prefered_phone , "prefered_phone");
        builder.addfield(email , "email");

        return builder.getValueString()

    def selectcolstr(self,
                        idx=False,
                        first_name=False,

                        surname=False,
                        address=False,
                        town=False,
                        post_code=False,
                        home_phone=False,
                        work_phone=False,
                        mobile=False,
                        prefered_phone=False,
                        email=False,
                        ):

        builder = SqlSelectBuilder()
        builder.addfield(idx, "gp_id");
        builder.addfield(first_name, "first_name");
        builder.addfield(surname , "surname");
        builder.addfield(address , "address");
        builder.addfield(town , "town");
        builder.addfield(post_code , "post_code");
        builder.addfield(home_phone , "home_phone");
        builder.addfield(work_phone , "work_phone");
        builder.addfield(mobile , "mobile");
        builder.addfield(prefered_phone , "prefered_phone");
        builder.addfield(email , "email");

        return builder.tostr()

    def selectcols(self, first_name=False,
                         idx=False,
                         surname=False,
                         address=False,
                         town=False,
                         post_code=False,
                         home_phone=False,
                         work_phone=False,
                         mobile=False,
                         prefered_phone=False,
                         email=False,
                         ):

        selectstr = self.selectcolstr(first_name,
                         idx,
                         surname,
                         address,
                         town,
                         post_code,
                         home_phone,
                         work_phone,
                         mobile,
                         prefered_phone,
                         email,
                         )

        if selectstr == None:
            select = 'select * from gps;'
        else:
            select = 'select ' + selectstr + ' from gps;'
        return self.execfetchall(select)

    # obsolete
    def select(self, selectStr, whereStr):
        select = 'select %s' + selectStr + ' from gps where %s ' % whereStr + ';'
        return self.execfetchone(select)

    def selectone(self, selectStr=None, whereStr=None):
        select = self._selectstr('gps', selectStr, whereStr)
        return self.execfetchone(select)

    def selectall(self, selectStr=None, whereStr=None):
        select = self._selectstr('gps', selectStr, whereStr)
        return self.execfetchall(select)

    def deleteall(self):
        self._deleteall('gps')

    def get_id(self, first_name, surname):
        #select = 'select gps_id from gps where first_name = \'%s\' ' % first_name + 'and surname = \'%s\'' % surname + ';'
        #return self.execfetchone(select)
        return self._get_id('gps', 'gp_id', first_name, surname)

    def remove(self, idx):
        #select = 'delete from gps where gps_id = \'%s\' ' % idx + ';'
        #self.execcmd(select)
        self._remove('gps', 'gp_id', idx)

    def showAll(self):
        #select = 'select * from gps;'
        #return self.execfetchall(select)
        return self._showAll('gps')

    def showItem(self, pid):
        #select = 'select * from gps where gp_id = \'%s\' ' % pid + ';'
        #return self.execfetchone(select)
        return self._showItem('gps', 'gp_id', pid)

    def getItem(self, idx, data):
        return data[idx]

class GPHistoryTable(Database):

    db_path = ""

    IDX_GP_ID       = 0
    IDX_DATETIME    = 1
    IDX_NOTE        = 2

    def add(self, gp_id, datetime, note):

        builder = SqlInsertBuilder()
        builder.addfield(gp_id, "gp_id")
        builder.addfield(datetime, "datetime")
        builder.addfield(note, "note")

        select = 'insert into gp_history (' + builder.getTokenString() + ') values (' + builder.getValueString() + ');'
        self.execcmd(select)

    def update(self, idx, datetime, note):

        builder = SqlUpdateBuilder()
        builder.addfield(datetime, "datetime")
        builder.addfield(note, "note");

        select = 'update gp_history set ' + builder.getValueString() + ' where gp_id = \'%s\' ' % idx + ';'
        self.execcmd(select)

    def selectone(self, idx, datetime):
        select = 'setect * from gp_history  where gp_id = \'%s\' ' % idx + ' and datetime = \'%s\' ' % str(datetime) + ';'
        return self.execfetchone(select)

    def selectall(self, idx):
        select = 'select * from gp_history where gp_id = \'%s\' ' % idx + ';'
        return self.execfetchall(select)
