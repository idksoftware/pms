'''
Created on Jan 7, 2014

@author: wzw7yn
'''
import wx
import os

from cpdeditdlg import CPDEditDialog
from cpdviewctrl import CPDViewDialog

import wx.lib.scrolledpanel as scrolledpanel
from access.cpd import CPDTable

class CPDCtrl(scrolledpanel.ScrolledPanel):
    pageName = "CPDPage"
    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(CPDCtrl, self).__init__(parent, style=style)

        self.selected_row = 0;



        self.cpdTable = CPDTable()
        self.rows = self.cpdTable.showAll()
        self.cpdListCtrl = CPDListCtrl(self)
        self.cpdListCtrl.populateList(self.rows)

        from cpdtableitem import CPDTableDef
        from access.database import DBTable
        #row = self.rows[self.selected_row]
        #self.cpdTableBind = DBTable(CPDTableDef())
        #self.dbRow = self.cpdTableBind.GetRow(row)

        #self.__DoLayout(self.dbRow)
        #self.SetInitialSize()


    def ___DoLayout(self, dbRow):

        title_lbl= wx.StaticText(self, label="Continuous Professional Development")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)


        #title = dbRow.GetAttr('title')
        title = "Iain"
        titleLbl = wx.StaticText(self, -1, "Title:")
        self.title = wx.StaticText(self, -1, title.GetText(), size=(200, 23))


        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

        grpSizer.Add(titleLbl, (1, 1))
        grpSizer.Add(self.title, (1, 2))

        from cpdviewctrl import CPDViewCtrl
        self.cpdViewCtrl = CPDViewCtrl(self)

        btnszr = wx.StdDialogButtonSizer()
        self.editbtn = wx.Button(self, wx.ID_EDIT)
        self.openbtn = wx.Button(self, wx.ID_OPEN)
        self.editbtn.SetDefault()
        btnszr.Add(self.editbtn)
        btnszr.Add(self.openbtn)

        btnszr.Realize()

        listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        listSizer.Add(self.cpdListCtrl, (1, 1))

        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        #mainSizer.Add(self.cpdViewCtrl, 0, wx.EXPAND | wx.ALL, 10)
        mainSizer.Add(self.cpdViewCtrl, 0, wx.ALL, 10)
        mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)
        mainSizer.Add(btnszr, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

        self.editbtn.Bind(wx.EVT_BUTTON, self.OnEdit)
        self.openbtn.Bind(wx.EVT_BUTTON, self.OnClicked)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)


    def __DoLayout(self, dbRow):

        title_lbl= wx.StaticText(self, label="Continuous Professional Development")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)


        title = dbRow.GetAttr('title')
        titleLbl = wx.StaticText(self, -1, "Title:")
        self.title = wx.StaticText(self, -1, title.GetText(), size=(200, 23))

        date_started = self.dbRow.GetAttr('date_started')
        dateLbl = wx.StaticText(self, -1, "Date Started:")
        self.date_started = wx.StaticText(self, -1, date_started.GetText(), size=(200, 23))

        days_taken = dbRow.GetAttr('days_taken')
        noOfDaysLbl = wx.StaticText(self, -1, "Number of days taken:")
        days = days_taken.GetText()
        self.days_taken = wx.StaticText(self, -1, days, size=(40,25))

        activity_type = dbRow.GetAttr('activity_type')
        activityTypeLbl = wx.StaticText(self, -1, "Activity Type:")
        self.activityType = wx.StaticText(self, -1, activity_type.GetText(), size=(200, 23))


        category = dbRow.GetAttr('category')
        categoryLbl = wx.StaticText(self, -1, "Category:")
        self.category = wx.StaticText(self, -1, category.GetText(), size=(200, 23))

        core_cpd_module = dbRow.GetAttr('core_cpd_module')
        coreCPDModuleLbl = wx.StaticText(self, -1, "Core CPD Module:")
        self.coreCPDModule = wx.StaticText(self, -1, core_cpd_module.GetText(), size=(200, 23))


        description = dbRow.GetAttr('description')
        descriptionLbl = wx.StaticText(self, -1, "Description:")
        self.description = wx.TextCtrl(self, -1, description.GetText(), size=(300, 80), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.moreButton = wx.Button(self, -1, "More", size=(50, 23))


        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

        grpSizer.Add(titleLbl, (1, 1))
        grpSizer.Add(self.title, (1, 2))

        grpSizer.Add(dateLbl, (2, 1))
        grpSizer.Add(self.date_started, (2, 2))

        grpSizer.Add(noOfDaysLbl, (3, 1))
        grpSizer.Add(self.days_taken, (3, 2))

        grpSizer.Add(activityTypeLbl, (4, 1))
        grpSizer.Add(self.activityType, (4, 2))

        grpSizer.Add(categoryLbl, (5, 1))
        grpSizer.Add(self.category, (5, 2))


        grpSizer.Add(coreCPDModuleLbl, (6, 1))
        grpSizer.Add(self.coreCPDModule, (6, 2))

        grpSizer.Add(descriptionLbl, (7, 1))
        grpSizer.Add(self.description, (7, 2)) #wx.FIXED_MINSIZE
        grpSizer.Add(self.moreButton, (7, 3))

        btnszr = wx.StdDialogButtonSizer()
        self.editbtn = wx.Button(self, wx.ID_EDIT)
        self.openbtn = wx.Button(self, wx.ID_OPEN)
        self.editbtn.SetDefault()
        btnszr.Add(self.editbtn)
        btnszr.Add(self.openbtn)

        btnszr.Realize()

        listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        #listSizer.Add(self.backupsListCtrl, (1, 1))
        listSizer.Add(self.cpdListCtrl, (1, 1))
        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        #mainSizer.Add(btnszr, 0, wx.ALIGN_LEFT, 12)
        mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)
        mainSizer.Add(btnszr, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

        self.editbtn.Bind(wx.EVT_BUTTON, self.OnEdit)
        self.openbtn.Bind(wx.EVT_BUTTON, self.OnClicked)
        self.moreButton.Bind(wx.EVT_BUTTON, self.OnMoreClicked)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)


    def OnClicked(self, event):
        self.selected_row = event.GetIndex()
        self.OnEdit(event)


    def OnItemSelected(self, event):
        self.selected_row = event.GetIndex()

        from cpdtableitem import CPDTableDef
        from access.database import DBTable
        row = self.rows[self.selected_row]
        cpdTableBind = DBTable(CPDTableDef())
        self.dbRow = cpdTableBind.GetRow(row)
        self.Update(self.dbRow)


    def OnMoreClicked(self, event):
        from cpdviewctrl import CPDViewDialog
        self.cpdViewDialog = CPDViewDialog(self.selected_row)
        self.cpdViewDialog.ShowModal()

    def OnEdit(self, event):
        #self.selected_row = event.GetIndex()

        print "Opening PatentEditDialog"
        cpdEditDialog = CPDEditDialog(self.selected_row)
        if cpdEditDialog.ShowModal() == wx.ID_OK:
            cpdEditDialog.Update()
            self.rows = self.cpdTable.showAll()
            row = self.rows[self.selected_row]
            self.dbRow = self.cpdTableBind.GetRow(row)
            self.Update(self.dbRow)
            self.cpdListCtrl.populateList(self.rows)

        print "Closing PatentEditDialog"

    def DBStr(self,data):
        if data == None:
            return ""
        return data

    def Update(self, dbRow):


        title = dbRow.GetAttr('title')
        self.title.SetLabel(title.GetText())

        date_started = dbRow.GetAttr('date_started')
        self.date_started.SetLabel(date_started.GetText())



        activity_type = dbRow.GetAttr('activity_type')
        self.activityType.SetLabel(activity_type.GetText())

        category = dbRow.GetAttr('category')
        self.category.SetLabel(category.GetText())

        core_cpd_module = dbRow.GetAttr('core_cpd_module')
        self.coreCPDModule.SetLabel(core_cpd_module.GetText())

        description = dbRow.GetAttr('description')
        self.description.SetLabel(description.GetText())



class CPDListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(CPDListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(500,300))

        self.InsertColumn(0, "Title")
        self.InsertColumn(1, "Date")
        self.InsertColumn(2, "Category")
        self.InsertColumn(3, "Type")
        self.InsertColumn(4, "Core CPD Module")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 50)
        self.SetColumnWidth(2, 100)
        self.SetColumnWidth(3, 100)
        self.SetColumnWidth(4, wx.LIST_AUTOSIZE_USEHEADER)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        self.DeleteAllItems()
        for row in data:
            data = row[CPDTable.IDX_TITLE], row[CPDTable.IDX_DATE_STARTED], row[CPDTable.IDX_CATEGORY], row[CPDTable.IDX_ACTIVITY_TYPE], row[CPDTable.IDX_CORE_CPD_MODULE]
            self.Append(data)

class MainFrame(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title="",pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name ="myFrame"):
        super(MainFrame, self).__init__(parent, id, title, pos, size, style, name)

        self.panel = MainPane(self)

class MainPane(wx.Notebook):

    def __init__(self, parent):
        super(MainPane, self).__init__(parent, style=wx.NB_LEFT)

        self.cpdCtrl = CPDCtrl(self)
        self.AddPage(self.cpdCtrl, "C P D")


class TestApp(wx.App):

    def OnInit(self):
        frame = MainFrame(None, title="The Main Frame")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

from access.database import Database
from utils.configreader import ConfigReader

if __name__=="__main__":
    cfg = ConfigReader()
    cfg.read("/home/wzw7yn/workspace/pms/main/config.xml")
    Database.Open(cfg.GetPath(), cfg.GetUsername(), cfg.GetPassword())
    app = TestApp(False)
    app.MainLoop()
