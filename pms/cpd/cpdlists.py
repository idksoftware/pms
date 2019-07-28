'''
Created on Feb 28, 2014

@author: wzw7yn
'''
import wx

class WebLinksCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(WebLinksCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(300,100))

        self.InsertColumn(0, "Date")
        self.InsertColumn(1, "Title")
        self.InsertColumn(2, "Link")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 180)
        self.SetColumnWidth(2, 180)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        for row in data:
            wllist = row[0], row[1]
            self.Append(wllist)

class FilesListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(FilesListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(300,100))

        self.InsertColumn(0, "Date")
        self.InsertColumn(1, "Title")
        self.InsertColumn(2, "filename")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 180)
        self.SetColumnWidth(2, 180)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        for row in data:
            fllist = row[0], row[1]
            self.Append(fllist)
            
class HistoryListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(HistoryListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(400,100))

        self.InsertColumn(0, "Date")
        self.InsertColumn(1, "Title")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 180)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        for row in data:
            list = row[0], row[1]
            self.Append(list)