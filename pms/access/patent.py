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



class PatentTable(Database):



    IDX_PATENT_ID = 0
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
    IDX_GENDER = 12
    IDX_NHS_NO = 13
    IDX_DATE_OF_BIRTH = 14
    IDX_GP_ID = 15



    def add(self, first_name, surname,
                                address=None,
                                town=None,
                                post_code=None,
                                home_phone=None,
                                work_phone=None,
                                mobile=None,
                                prefered_phone=None,
                                email=None,
                                gender=None,
                                nhs_no=None,
                                date_of_birth=None,
                                gp_id=None):

        if prefered_phone==None:
            prefered_phone='Home'

        builder = SqlInsertBuilder()
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
        builder.addfield( gender , "gender");
        builder.addfield( nhs_no , "nhs_no");
        builder.addfield( date_of_birth , "date_of_birth");
        builder.addfield( gp_id , "gp_id");

        select = 'insert into patent(' + builder.getTokenString() + ') values (' + builder.getValueString() + ');'
        self.execcmd(select)

    def update(self, idx, first_name=None,
			 			 surname=None,
                         address=None,
                         town=None,
                         post_code=None,
                         home_phone=None,
                         work_phone=None,
                         mobile=None,
                         prefered_phone=None,
                         email=None,
                         gender=None,
                         nhs_no=None,
                         date_of_birth=None,
                         gp_id=None):


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
        builder.addfield(gender , "gender");
        builder.addfield(nhs_no , "nhs_no");
        builder.addfield(date_of_birth , "date_of_birth");
        builder.addfield(gp_id , "gp_id");

        select = 'update patent set ' + builder.getValueString() + ' where patent_id = \'%s\' ' % idx + ';'
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
                         email=None,
                         gender=None,
                         nhs_no=None,
                         date_of_birth=None,
                         gp_id=None):

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
        builder.addfield(gender , "gender");
        builder.addfield(nhs_no , "nhs_no");
        builder.addfield(date_of_birth , "date_of_birth");
        builder.addfield(gp_id , "gp_id");
        return builder.getValueString()

    
        
    def selectcolstr(self, first_name=False,
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
                         gender=False,
                         nhs_no=False,
                         date_of_birth=False,
                         gp_id=False):
        
        builder = SqlSelectBuilder()
        builder.addfield(idx, "patent_id");
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
        builder.addfield( gender , "gender");
        builder.addfield( nhs_no , "nhs_no");
        builder.addfield( date_of_birth , "date_of_birth");
        builder.addfield( gp_id , "gp_id");
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
                         gender=False,
                         nhs_no=False,
                         date_of_birth=False,
                         gp_id=False):
        
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
                         gender,
                         nhs_no,
                         date_of_birth,
                         gp_id)
        
        if selectstr == None:
            select = 'select * from patent;'
        else:
            select = 'select ' + selectstr + ' from patent;'
        return self.execfetchall(select)
    
    def __select(self, selectStr=None, whereStr=None):
        select = None
        if whereStr == None:
            if selectStr == None:
                select = 'select * from patent;'
            else:
                select = 'select %s' + selectStr + ' from patent;'
        else:
            if selectStr == None:
                select = 'select * from patent where %s ' % whereStr + ';'
            else:
                select = 'select %s' + selectStr + ' from patent where %s ' % whereStr + ';'
            
        return select
    
    def selectone(self, selectStr=None, whereStr=None):
        select = self.__select(selectStr, whereStr)    
        return self.execfetchone(select)
            
    def selectall(self, selectStr=None, whereStr=None):
        select = self.__select(selectStr, whereStr)    
        return self.execfetchall(select)
    
    def remove(self, idx):
        select = 'delete from patent where patent_id = \'%s\' ' % idx + ';'
        self.execcmd(select)
    
    def deleteall(self):
        cmd = "delete from patent;"
        self.execcmd(cmd) 
    
    def get_id(self, first_name, surname):
        select = 'select patent_id from patent where first_name = \'%s\' ' % first_name + 'and surname = \'%s\'' % surname + ';'
        return self.execfetchone(select)
        
    def showAll(self):
        select = 'select * from patent;'
        return self.execfetchall(select)
       

    def showItem(self, pid):
        select = 'select * from patent where patent_id = \'%s\' ' % pid + ';'
        return self.execfetchone(select)


    def getItem(self, idx, data):
        return data[idx]

if __name__ == "__main__":
    pa = PatentTable()

    print pa.singlewhere(first_name="Iain", surname="Ferguson")

    for i in range(5,13):
        pa.update(i, work_phone='01444-129666', post_code='BN238BJ')
    #row = pa.showItem(id)
    '''
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
    '''
    pa.remove(12)
    id = pa.get_id("Iain Andrew", "Ferguson")
    row = pa.showItem(id)
    print row
    print pa.getItem(PatentTable.IDX_EMAIL, row)
