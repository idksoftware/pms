'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx
import wx.lib.scrolledpanel as scrolledpanel
from wx.calendar import CalendarCtrl
from cpdlists import FilesListCtrl
from cpdlists import WebLinksCtrl
from cpdlists import HistoryListCtrl

'''
class GeneralCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(GeneralCtrl, self).__init__(parent, style=style)

        # Layout
        self.__DoLayout(parent)
        self.SetInitialSize()

    def __DoLayout(self, parent):

        title_lbl= wx.StaticText(self, label="Continuous Professional Development - Details")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)



        titleLbl = wx.StaticText(self, -1, "Title:")
        self.title = wx.StaticText(self, -1, "Some Training:", size=(200, 23))

        date_started = parent.dbRow.GetAttr('date_started')
        dateLbl = wx.StaticText(self, -1, "Date Started:")
        self.date = wx.StaticText(self, -1, date_started.GetText(), size=(200, 23))




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

        learning_objectives = parent.dbRow.GetAttr('learning_objectives')
        learningObjectivesLbl = wx.StaticText(self, -1, "Learning Objectives:")
        self.learningObjectives = wx.TextCtrl(self, -1, learning_objectives.GetText(), size=(300, 80), style=wx.TE_MULTILINE | wx.TE_READONLY)

        reflective_comments = parent.dbRow.GetAttr('reflective_comments')
        reflectiveCommentsLbl = wx.StaticText(self, -1, "Reflective Comments:")
        self.reflectiveComments = wx.TextCtrl(self, -1, reflective_comments.GetText(), size=(300,80), style=wx.TE_MULTILINE | wx.TE_READONLY)
        #self.reflectiveComments = wx.TextCtrl(self, -1, text, size=(300,80), style=wx.TE_MULTILINE)


        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

        grpSizer.Add(titleLbl, (1, 1))
        grpSizer.Add(self.title, (1, 2))

        grpSizer.Add(dateLbl, (2, 1))
        grpSizer.Add(self.date, (2, 2))

        grpSizer.Add(activityTypeLbl, (3, 1))
        grpSizer.Add(self.activityType, (3, 2))

        grpSizer.Add(categoryLbl, (4, 1))
        grpSizer.Add(self.category, (4, 2))


        grpSizer.Add(coreCPDModuleLbl, (5, 1))
        grpSizer.Add(self.coreCPDModule, (5, 2))

        grpSizer.Add(descriptionLbl, (6, 1))
        grpSizer.Add(self.description, (6, 2)) #wx.FIXED_MINSIZE

        grpSizer.Add(learningObjectivesLbl, (7, 1))
        grpSizer.Add(self.learningObjectives, (7, 2))

        grpSizer.Add(reflectiveCommentsLbl, (8, 1))
        grpSizer.Add(self.reflectiveComments, (8, 2))


        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)




class OtherCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(OtherCtrl, self).__init__(parent, style=style)

        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):
        title_lbl= wx.StaticText(self, label="Continuous Professional Development - Other Details")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)



        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.rows = [
                ("2013 12 23", "PNA"),
                ("2013 06 02", "Check-up"),
                ]


        filesListLbl = wx.StaticText(self, -1, "Attached Files:")
        self.filesListCtrl = FilesListCtrl(self)
        self.filesListCtrl.populateList(self.rows)

        self.rows = [
                ("2013 12 23", "PNA"),
                ("2013 06 02", "Check-up"),
                ]


        webLinksLbl = wx.StaticText(self, -1, "Web Links:")
        self.webLinksCtrl = WebLinksCtrl(self)
        self.webLinksCtrl.populateList(self.rows)

        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

        grpSizer.Add(filesListLbl, (2, 1))
        grpSizer.Add(self.filesListCtrl, (2, 2)) #wx.FIXED_MINSIZE

        grpSizer.Add(webLinksLbl, (3, 1))
        grpSizer.Add(self.webLinksCtrl, (3, 2)) #wx.FIXED_MINSIZE

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


        title_lbl= wx.StaticText(self, label="Continuous Professional Development - History")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)




        trainingHistoryLbl = wx.StaticText(self, -1, "Training History:")
        #self.appointments = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(300,100))
        self.rows = [
                ("2013 12 23", "PNA"),
                ("2013 06 02", "Check-up"),
                ]

        self.historyList = HistoryListCtrl(self)
        self.historyList.populateList(self.rows)


        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        grp1Sizer = wx.GridBagSizer(vgap=8, hgap=8)



        grp1Sizer.Add(trainingHistoryLbl, (1, 1))
        grp1Sizer.Add(self.historyList, (1, 2))


        mainSizer.Add(grp1Sizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

'''

class CPDViewDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self, rowIdx):
        wx.Dialog.__init__(self, None, -1, "Continuous Professional Development", size=(600, 600))
        '''
        Constructor
        '''




        self.panel = CPDViewPanel(self, rowIdx)


        sizer = wx.BoxSizer(wx.VERTICAL)
        #btnSizer = wx.StdDialogButtonSizer()
        btnSizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)

        sizer.Add(self.panel, 1, wx.EXPAND)
        #okButton = wx.Button(self, wx.ID_OK, "Ok", pos=(15, 15))
        #okButton.SetDefault()
        #btnSizer.Add(okButton)
        #cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel", pos=(15, 15))
        #btnSizer.Add(cancelButton)
        sizer.Add(btnSizer, 0, wx.ALIGN_RIGHT | wx.ALL, 2)
        #sizer.Add(btnSizer)
        self.SetSizer(sizer)
        #self.SetInitialSize()
        #self.Bind(wx.EVT_BUTTON, self.OnButton)

    #def OnButton(self, event):
        #pos = self.panel.generalCtrl.preferedPhone.Value()
        #return event

class CPDViewPanel(wx.Notebook):
    def __init__(self, parent, rowIdx):
        super(CPDViewPanel, self).__init__(parent, style=wx.LB_BOTTOM)

        from access.cpd import CPDTable
        cpdTable = CPDTable()

        rows = cpdTable.showAll()

        row = rows[rowIdx]
        print row

        from cpdtableitem import CPDTableDef
        from access.database import DBTable

        cpdTableBind = DBTable(CPDTableDef())
        '''
        self.dbRow = cpdTableBind.GetRow(row)
        self.generalCtrl = GeneralCtrl(self)
        self.AddPage(self.generalCtrl, "General")
        self.otherCtrl = OtherCtrl(self)
        self.AddPage(self.otherCtrl, "Other")
        self.historyCtrl = HistoryCtrl(self)
        self.AddPage(self.historyCtrl, "history")
        '''
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