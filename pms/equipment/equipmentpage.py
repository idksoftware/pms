'''
Created on Jan 7, 2014

@author: wzw7yn
'''
import wx
import os

from equipmenteditdlg import EquipmentEditDialog

import wx.lib.scrolledpanel as scrolledpanel
from access.patent import PatentTable

class EquipmentCtrl(scrolledpanel.ScrolledPanel):
    pageName = "CPDPage"
    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(EquipmentCtrl, self).__init__(parent, style=style)
        #self.backupsListCtrl = BackupListCtrl(self)
        self.cpdListCtrl = CPDListCtrl(self)

       
       
      
        self.__DoLayout()
        self.SetInitialSize()


    def __DoLayout(self):

        title_lbl= wx.StaticText(self, label="Equipment Service History")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)


        sizer = wx.GridBagSizer(vgap=2, hgap=2)
        
        lastUpdatedLbl = wx.StaticText(self, -1, "Next service date:")
        self.lastUpdated = '2014/02/12'
        lastUpdatedText = wx.StaticText(self, -1, self.lastUpdated)
        sizer.Add(lastUpdatedLbl, (1, 1))
        sizer.Add(lastUpdatedText, (1, 2))

        titleLbl = wx.StaticText(self, -1, "Equipement:")
        self.title = 'Autoclave 602 xv'
        titleText = wx.StaticText(self, -1, self.title)
        sizer.Add(titleLbl, (2, 1))
        sizer.Add(titleText, (2, 2))

        discriptionLbl = wx.StaticText(self, -1, "Discription:")
        self.discription = 'Autoclave in the main practise'
        discriptionText = wx.StaticText(self, -1, self.discription)
        sizer.Add(discriptionLbl, (3, 1))
        sizer.Add(discriptionText, (3, 2))

        btnszr = wx.StdDialogButtonSizer()
        editbtn = wx.Button(self, wx.ID_EDIT)
        openbtn = wx.Button(self, wx.ID_OPEN)
        editbtn.SetDefault()
        btnszr.Add(editbtn)
        btnszr.Add(openbtn)

        btnszr.Realize()

        listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        #listSizer.Add(self.backupsListCtrl, (1, 1))
        listSizer.Add(self.cpdListCtrl, (1, 1))
        mainSizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 10)
        #mainSizer.Add(btnszr, 0, wx.ALIGN_LEFT, 12)
        mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)
        mainSizer.Add(btnszr, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def OnClicked(self, event):
        self.selected_row = event.GetIndex()
        self.rows[self.selected_row]
        equipmentEditDialog = EquipmentEditDialog()
        print "Opening CPDEditDialog"
        equipmentEditDialog.ShowModal()
        print "Closing CPDEditDialog"
        

    def OnItemSelected(self, event):
        pass
      
    def DBStr(self,data):
        if data == None:
            return ""
        return data

class CPDListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(CPDListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(500,300))

        self.InsertColumn(0, "Type")
        self.InsertColumn(1, "Make")
        self.InsertColumn(2, "Model")
        self.InsertColumn(3, "Next Service")
        self.InsertColumn(4, "Last Service")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 50)
        self.SetColumnWidth(2, 100)
        self.SetColumnWidth(3, 100)
        self.SetColumnWidth(4, wx.LIST_AUTOSIZE_USEHEADER)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        pass
        #for row in data:
            #list = row[1], row[2], row[3], row[4]
            #self.Append(list)

class MainFrame(wx.Frame):
    
    def __init__(self, parent, id=wx.ID_ANY, title="",pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name ="myFrame"):
        super(MainFrame, self).__init__(parent, id, title, pos, size, style, name)

        self.panel = MainPane(self)
    
class MainPane(wx.Notebook):

    def __init__(self, parent):
        super(MainPane, self).__init__(parent, style=wx.NB_LEFT)

        self.equipmentCtrl = EquipmentCtrl(self)
        self.AddPage(self.equipmentCtrl, "Equipment")


class TestApp(wx.App):
    
    def OnInit(self):
        frame = MainFrame(None, title="The Main Frame")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()
