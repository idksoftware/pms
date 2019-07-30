'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx
import wx.lib.scrolledpanel as scrolledpanel
from wx.adv import CalendarCtrl
from cpdlists import FilesListCtrl
from cpdlists import WebLinksCtrl
from cpdlists import HistoryListCtrl
from utils.copyattachments import Attachments

class GeneralCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(GeneralCtrl, self).__init__(parent, style=style)

        # Layout
        self.__DoLayout(parent)
        self.SetInitialSize()

    def __DoLayout(self, parent):


        mainSizer = wx.BoxSizer(wx.VERTICAL)

        title = parent.dbRow.GetAttr('title')
        titleLbl = wx.StaticText(self, -1, "Title:")
        self.title = wx.StaticText(self, -1, title.GetText(), size=(200, 23))

        date_started = parent.dbRow.GetAttr('date_started')
        dateLbl = wx.StaticText(self, -1, "Date Started:")
        self.date_started = wx.StaticText(self, -1, date_started.GetText(), size=(200, 23))

        days_taken = parent.dbRow.GetAttr('days_taken')
        noOfDaysLbl = wx.StaticText(self, -1, "Number of days taken:")
        days = days_taken.GetText()
        self.days_taken = wx.StaticText(self, -1, days, size=(40,25))


        activity_type = parent.dbRow.GetAttr('activity_type')
        activityTypeLbl = wx.StaticText(self, -1, "Activity Type:")
        self.activityType = wx.StaticText(self, -1, activity_type.GetText(), size=(200, 23))


        category = parent.dbRow.GetAttr('category')
        categoryLbl = wx.StaticText(self, -1, "Category:")
        self.category = wx.StaticText(self, -1, category.GetText(), size=(200, 23))

        core_cpd_module = parent.dbRow.GetAttr('core_cpd_module')
        coreCPDModuleLbl = wx.StaticText(self, -1, "Core CPD Module:")
        self.coreCPDModule = wx.StaticText(self, -1, core_cpd_module.GetText(), size=(200, 23))


        description = parent.dbRow.GetAttr('description')
        descriptionLbl = wx.StaticText(self, -1, "Description:")
        self.description = wx.TextCtrl(self, -1, description.GetText(), size=(300, 80), style=wx.TE_MULTILINE | wx.TE_READONLY)

        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

        grpSizer.Add(titleLbl, (1, 1))
        grpSizer.Add(self.title, (1, 2))

        grpSizer.Add(dateLbl, (2, 1))
        grpSizer.Add(self.date_started, (2, 2))

        grpSizer.Add(dateLbl, (3, 1))
        grpSizer.Add(self.days_taken, (3, 2))

        grpSizer.Add(activityTypeLbl, (4, 1))
        grpSizer.Add(self.activityType, (4, 2))

        grpSizer.Add(categoryLbl, (5, 1))
        grpSizer.Add(self.category, (5, 2))


        grpSizer.Add(coreCPDModuleLbl, (6, 1))
        grpSizer.Add(self.coreCPDModule, (6, 2))

        grpSizer.Add(descriptionLbl, (7, 1))
        grpSizer.Add(self.description, (7, 2)) #wx.FIXED_MINSIZE

        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

class OtherCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(OtherCtrl, self).__init__(parent, style=style)

        # Layout
        self.__DoLayout(parent)
        self.SetInitialSize()

    def __DoLayout(self, parent):

        mainSizer = wx.BoxSizer(wx.VERTICAL)



        description = parent.dbRow.GetAttr('description')
        descriptionLbl = wx.StaticText(self, -1, "Description:")
        self.description = wx.TextCtrl(self, -1, description.GetText(), size=(300, 80), style=wx.TE_MULTILINE | wx.TE_READONLY)

        learning_objectives = parent.dbRow.GetAttr('learning_objectives')
        learningObjectivesLbl = wx.StaticText(self, -1, "Learning Objectives:")
        self.learningObjectives = wx.TextCtrl(self, -1, learning_objectives.GetText(), size=(300, 80), style=wx.TE_MULTILINE | wx.TE_READONLY)

        self.reflective_comments = parent.dbRow.GetAttr('reflective_comments')
        reflectiveCommentsLbl = wx.StaticText(self, -1, "Reflective Comments:")
        self.reflective_comments = wx.TextCtrl(self, -1, self.reflective_comments.GetText(), size=(300,80), style=wx.TE_MULTILINE | wx.TE_READONLY)
        #self.reflectiveComments = wx.TextCtrl(self, -1, text, size=(300,80), style=wx.TE_MULTILINE)

        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

        grpSizer.Add(descriptionLbl, (1, 1))
        grpSizer.Add(self.description, (1, 2)) #wx.FIXED_MINSIZE

        grpSizer.Add(learningObjectivesLbl, (2, 1))
        grpSizer.Add(self.learningObjectives, (2, 2))

        grpSizer.Add(reflectiveCommentsLbl, (3, 1))
        grpSizer.Add(self.reflective_comments, (3, 2))


        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)


class HistoryCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(HistoryCtrl, self).__init__(parent, style=style)
        #self.current = "Default"
        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):



        title_lbl= wx.StaticText(self, label="Continuous Professional Development - Other")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.rows = [
                ("2013 12 23", "PNA"),
                ("2013 06 02", "Check-up"),
                ]
        self.attachments = Attachments("/home/wzw7yn/pms/repos")
        afList = list() 
        newOptionLbl = wx.StaticText(self, -1, "Attached Files:")
        self.listCtrl = wx.ListBox(self, -1, (10, 30), (300,80), afList, wx.LB_SINGLE | wx.LB_SORT)
        

        webLinksLbl = wx.StaticText(self, -1, "Web Links:")
        self.webLinksCtrl = WebLinksCtrl(self)
        self.webLinksCtrl.populateList(self.rows)

        text = ""

        reflectiveCommentsLbl = wx.StaticText(self, -1, "Reflective Comments:")
        self.reflective_comments = wx.TextCtrl(self, -1, text, size=(300,80), style=wx.TE_MULTILINE)

        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

        grpSizer.Add(reflectiveCommentsLbl, (1, 1))
        grpSizer.Add(self.reflective_comments, (1, 2))

        grpSizer.Add(newOptionLbl, (2, 1))
        grpSizer.Add(self.listCtrl, (2, 2))

        grpSizer.Add(webLinksLbl, (3, 1))
        grpSizer.Add(self.webLinksCtrl, (3, 2)) #wx.FIXED_MINSIZE

        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)



class CPDViewDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self, rowIdx):
        wx.Dialog.__init__(self, None, -1, "Continuous Professional Development", size=(600, 400))
        '''
        Constructor
        '''
        self.panel = CPDViewCtrl(self, rowIdx)
        sizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        sizer.Add(btnSizer, 0, wx.ALIGN_RIGHT | wx.ALL, 2)
        self.SetSizer(sizer)


class CPDViewCtrl(wx.Notebook):
    def __init__(self, parent, rowIdx):
        super(CPDViewCtrl, self).__init__(parent, size=(500,300), style=wx.LB_BOTTOM)

        from access.cpd import CPDTable
        cpdTable = CPDTable()

        rows = cpdTable.showAll()

        row = rows[rowIdx]
        print row

        from cpdtableitem import CPDTableDef
        from access.database import DBTable

        cpdTableBind = DBTable(CPDTableDef())

        self.dbRow = cpdTableBind.GetRow(row)
        self.generalCtrl = GeneralCtrl(self)
        self.AddPage(self.generalCtrl, "General")
        self.otherCtrl = OtherCtrl(self)
        self.AddPage(self.otherCtrl, "Details")
        self.historyCtrl = HistoryCtrl(self)
        self.AddPage(self.historyCtrl, "Documentation")

class TestApp(wx.App):
    def OnInit(self):
        cpdViewDialog = CPDViewDialog()

        print "Opening CPDEditDialog"
        cpdViewDialog.ShowModal()
        print "Closing CPDEditDialog"
        return True

from access.database import Database
from utils.configreader import ConfigReader

if __name__=="__main__":
    cfg = ConfigReader()
    cfg.read("/home/wzw7yn/workspace/pms/main/config.xml")
    Database.Open(cfg.GetPath(), cfg.GetUsername(), cfg.GetPassword())
    app = TestApp(False)
    app.MainLoop()