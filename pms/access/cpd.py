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


class CPDTable(Database):

    db_path = ""

    '''
    cpd_id                   integer primary key,
    date_started                    datetime        not null,
    days_taken                    int        ,
    activity_type               varchar(100),
    category                    varchar(100),
    core_cpd_module             varchar(256),
    description                varchar(512),
    learning_objectives         varchar(512),
    reflective_comments         varchar(512),
    attached_files         varchar(512),
    web_links         varchar(512)
    '''
    IDX_CPD_ID               = 0
    IDX_TITLE                = 1
    IDX_DATE_STARTED         = 2
    IDX_DAYS_TAKEN           = 3
    IDX_ACTIVITY_TYPE        = 4
    IDX_CATEGORY             = 5
    IDX_CORE_CPD_MODULE      = 6
    IDX_DISCRIPTION          = 7
    IDX_LEARNING_OBJECTIVES  = 8
    IDX_REFLECTIVE_COMMENTS  = 9
    IDX_ATTACHED_FILES       = 10
    IDX_WEB_LINKS            = 11

    @staticmethod
    def SetConfig(path):
        CPDTable.db_path = path

    def add(self,
                
                title=None,
                date_started=None,
                days_taken=None,
                activity_type=None,
                category=None,
                core_cpd_module=None,
                description=None,
                learning_objectives=None,
                reflective_comments=None,
                attached_files=None,
                web_links=None,
                  ):


        builder = SqlInsertBuilder()
        
        builder.addfield( title, "title");
        builder.addfield( date_started , "date_started");
        builder.addfield( days_taken , "days_taken");
        builder.addfield( activity_type , "activity_type");
        builder.addfield( category , "category");
        builder.addfield( core_cpd_module , "core_cpd_module");
        builder.addfield( description , "description");
        builder.addfield( learning_objectives , "learning_objectives");
        builder.addfield( attached_files , "attached_files");
        builder.addfield( web_links , "web_links");

        select = 'insert into cpd (' + builder.getTokenString() + ') values (' + builder.getValueString() + ');'
        self.execcmd(select)


    def update(self, cpd_id,
                title=None,
                date_started=None,
                days_taken=None,
                activity_type=None,
                category=None,
                core_cpd_module=None,
                description=None,
                learning_objectives=None,
                reflective_comments=None,
                attached_files=None,
                web_links=None,
                  ):


        builder = SqlUpdateBuilder()
        builder.addfield( cpd_id , "cpd_id");
        builder.addfield( title, "title");
        builder.addfield( date_started , "date_started");
        builder.addfield( days_taken , "days_taken");
        builder.addfield( activity_type , "activity_type");
        builder.addfield( category , "category");
        builder.addfield( core_cpd_module , "core_cpd_module");
        builder.addfield( description , "description");
        builder.addfield( learning_objectives , "learning_objectives");
        builder.addfield( attached_files , "attached_files");
        builder.addfield( web_links , "web_links");

        select = 'update cpd set ' + builder.getValueString() + ' where cpd_id = \'%s\' ' % cpd_id + ';'
        self.execcmd(select)

    def singlewhere(self,
                cpd_id=None,
                title=None,
                date_started=None,
                days_taken=None,
                activity_type=None,
                category=None,
                core_cpd_module=None,
                description=None,
                learning_objectives=None,
                reflective_comments=None,
                attached_files=None,
                web_links=None,
                  ):

        builder = SqlSingleWhereBuilder()
        builder.addfield( cpd_id , "cpd_id");
        builder.addfield( title, "title");
        builder.addfield( date_started , "date_started");
        builder.addfield( days_taken , "days_taken");
        builder.addfield( activity_type , "activity_type");
        builder.addfield( category , "category");
        builder.addfield( core_cpd_module , "core_cpd_module");
        builder.addfield( description , "description");
        builder.addfield( learning_objectives , "learning_objectives");
        builder.addfield( attached_files , "attached_files");
        builder.addfield( web_links , "web_links");

        return builder.getValueString()

    def selectcolstr(self,
                cpd_id=None,
                title=None,
                date_started=None,
                days_taken=None,
                activity_type=None,
                category=None,
                core_cpd_module=None,
                description=None,
                learning_objectives=None,
                reflective_comments=None,
                attached_files=None,
                web_links=None,
                        ):

        builder = SqlSelectBuilder()
        builder = SqlSingleWhereBuilder()
        builder.addfield( cpd_id , "cpd_id");
        builder.addfield( title, "title");
        builder.addfield( date_started , "date_started");
        builder.addfield( days_taken , "days_taken");
        builder.addfield( activity_type , "activity_type");
        builder.addfield( category , "category");
        builder.addfield( core_cpd_module , "core_cpd_module");
        builder.addfield( description , "description");
        builder.addfield( learning_objectives , "learning_objectives");
        builder.addfield( attached_files , "attached_files");
        builder.addfield( web_links , "web_links");

        return builder.tostr()

    def selectcols(self, payment_id=False,
                cpd_id=False,
                date_started=False,
                days_taken=False,
                activity_type=False,
                category=False,
                core_cpd_module=False,
                description=False,
                learning_objectives=False,
                reflective_comments=False,
                attached_files=False,
                web_links=False
                         ):

        selectstr = self.selectcolstr(payment_id,
                  cpd_id,
                date_started,
                days_taken,
                activity_type,
                category,
                core_cpd_module,
                description,
                learning_objectives,
                reflective_comments,
                attached_files,
                web_links
                         )

        if selectstr == None:
            select = 'select * from cpd;'
        else:
            select = 'select ' + selectstr + ' from cpd;'
        return self.execfetchall(select)

    # obsolete
    def select(self, selectStr, whereStr):
        select = 'select %s' + selectStr + ' from cpd where %s ' % whereStr + ';'
        return self.execfetchone(select)
    def selectone(self, selectStr=None, whereStr=None):
        select = self._selectstr('cpd', selectStr, whereStr)
        return self.execfetchone(select)

    def selectall(self, selectStr=None, whereStr=None):
        select = self._selectstr('cpd', selectStr, whereStr)
        return self.execfetchall(select)

    def deleteall(self):
        self._deleteall('cpd')

    def get_id(self, cpd_id):
        select = 'select cpd_id from payment where cpd_id = \'%s\' ' % cpd_id + ';'
        return self.execfetchone(select)

    def remove(self, idx):
        self._remove('cpd', 'cpd_id', idx)

    def showAll(self):
        return self._showAll('cpd')

    def showItem(self, pid):
        return self._showItem('cpd', 'cpd_id', pid)


    def getItem(self, idx, data):
        return data[idx]



