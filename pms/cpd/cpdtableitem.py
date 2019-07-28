'''
Created on Feb 27, 2014

@author: wzw7yn
'''
from access.database import DBTableDef


class CPDTableDef(DBTableDef):

    def __init__(self):
        DBTableDef.__init__(self)
        #self.Add(DBAttribDef("cpd_id", "int", pkey=True))
        self.Add("cpd_id", "int", pkey=True)
        self.Add("title", "str")
        self.Add("date_started", "date")
        self.Add("days_taken", "int")
        self.Add("activity_type", "str")
        self.Add("category", "str")
        self.Add("core_cpd_module", "str")
        self.Add("description", "str")
        self.Add("learning_objectives", "str")
        self.Add("reflective_comments", "str")
        self.Add("attached_files", "str")
        self.Add("web_links", "str")



