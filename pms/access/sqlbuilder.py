'''
Created on Jan 13, 2014

@author: wzw7yn

'''

class SqlSelectBuilder:

    def __init__(self):
        self.tokenStr = None
        self.valueStr = None

    def addfield(self,field, name):
        if field == True:
            if self.tokenStr == None:
                self.tokenStr = ""
            else:
                self.tokenStr = self.tokenStr + ','
            self.tokenStr = self.tokenStr + name



    def tostr(self):
        return self.tokenStr





class SqlInsertBuilder:

    def __init__(self):
        self.tokenStr = None
        self.valueStr = None

    def addfield(self,field, name):
        if field != None:
            if self.tokenStr == None:
                self.tokenStr = ""
            else:
                self.tokenStr = self.tokenStr + ','
            self.tokenStr = self.tokenStr + name

            if self.valueStr == None:
                self.valueStr = ""
            else:
                self.valueStr = self.valueStr + ','
            self.valueStr = self.valueStr + "\'%s\'" % field

    def getTokenString(self):
        return self.tokenStr

    def getValueString(self):
        return self.valueStr




class SqlUpdateBuilder:

    def __init__(self):
        self.valueStr = ""
        self.first = True

    def addfield(self, field, token):
        if field != None:
            if not self.first:
                self.valueStr = self.valueStr + ','
            else:
                self.first = False
            self.valueStr = self.valueStr + token + "=\'%s\'" % field

    def getValueString(self):
        return self.valueStr



class SqlSingleWhereBuilder:

    def __init__(self):
        self.valueStr = ""
        self.first = True

    def addfield(self,field, token):
         if field != None:
            if not self.first:
                self.valueStr = self.valueStr + ' and '
            else:
                self.first = False
            self.valueStr = self.valueStr + token + "=\'%s\'" % field

    def getValueString(self):
        return self.valueStr