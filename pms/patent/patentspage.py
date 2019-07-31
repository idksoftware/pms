'''
Created on Jan 7, 2014

@author: wzw7yn
'''
import wx
import os

from patenteditdlg import PatentEditDialog

import wx.lib.scrolledpanel as scrolledpanel
from access.patent import PatentTable

class PatentsCtrl(scrolledpanel.ScrolledPanel):
    pageName = "PatentsPage"
    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(PatentsCtrl, self).__init__(parent, style=style)
        self.patentBookCtrl = PatentBookCtrl(self)

        #patentTable = PatentTable()
        #self.rows = patentTable.showAll()
        #self.backupsListCtrl.populateList(self.rows)
        # Layout
        self.__DoLayout()
        self.SetInitialSize()


    def __DoLayout(self):

        title_lbl= wx.StaticText(self, label="Patents")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)


        sizer = wx.GridBagSizer(vgap=2, hgap=2)
        nameLbl = wx.StaticText(self, -1, "Name:")

        title = 'Mr'
        first = 'Iain'
        surname = 'Ferguson'

        nameStr = title + " " + first + " " + surname
        self.name = wx.StaticText(self, -1, nameStr)

        sizer.Add(nameLbl, (1, 1))
        sizer.Add(self.name, (1, 2))

        addressLbl = wx.StaticText(self, -1, "Address:")

        address1 = "16 St Wilfrieds Rd"
        address2 = None
        town = "Burgess Hill"
        county = "West Sussex"
        postcode = "RH158BD"
        if address2 == None:
            address1Str = address1 + " " + town
        else:
            address1Str = address1 + " " + address2 + " " + town
        self.address = wx.StaticText(self, -1, address1Str)

        self.county = wx.StaticText(self, -1, county)
        self.post = wx.StaticText(self, -1, postcode)

        sizer.Add(addressLbl, (2, 1))
        sizer.Add(self.address, (2, 2))
        sizer.Add(self.county, (3, 2))
        sizer.Add(self.post, (4, 2))



        phoneLbl = wx.StaticText(self, -1, "Phone:")
        phoneStr = "Home " + "01444-241048" " Work " + "01273-925723"
        mobileStr = "Mobile " + "+4478912786397"

        sizer.Add(phoneLbl, (5, 1))
        self.phone = wx.StaticText(self, -1, phoneStr)
        self.mobile = wx.StaticText(self, -1, mobileStr)
        sizer.Add(self.phone, (5, 2))
        sizer.Add(self.mobile, (6, 2))

        emailLbl = wx.StaticText(self, -1, "Email:")
        emailStr = "i.ferguson@idk.co.uk"
        self.email = wx.StaticText(self, -1, emailStr)
        sizer.Add(emailLbl, (7, 1))
        sizer.Add(self.email, (7, 2))




        btnszr = wx.StdDialogButtonSizer()
        editbtn = wx.Button(self, wx.ID_EDIT)
        openbtn = wx.Button(self, wx.ID_OPEN)
        editbtn.SetDefault()
        sizer.Add(editbtn, (8, 3))
        sizer.Add(openbtn, (8, 4))

        btnszr.Realize()

        listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        listSizer.Add(self.patentBookCtrl, (1, 1))
        mainSizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 10)
        #mainSizer.Add(btnszr, 0, wx.ALIGN_LEFT, 12)
        mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(mainSizer)

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def OnClicked(self, event):
        self.selected_row = event.GetIndex()
        self.rows[self.selected_row]
        patentEditDialog = PatentEditDialog()
        print "Opening PatentEditDialog"
        patentEditDialog.ShowModal()
        print "Closing PatentEditDialog"
        

    def OnItemSelected(self, event):
        self.selected_row = event.GetIndex()
        val = list()
        for column in range(1,3):
            item = self.patentBookCtrl.GetItem(self.selected_row, column)
            val.append(item.GetText())
        frame = self.GetTopLevelParent()
        frame.PushStatusText(" ".join(val))
        self.rows = self.patentBookCtrl.GetRows()
        row = self.rows[self.selected_row]
        self.AddressUpdate(row)


    def DBStr(self,data):
        if data == None:
            return ""
        return data


    def AddressUpdate(self, row):


        title = self.DBStr(row[PatentTable.IDX_TITLE])
        first = self.DBStr(row[PatentTable.IDX_FIRST_NAME])
        surname = self.DBStr(row[PatentTable.IDX_SURNAME])
        nameStr = ""
        if title == "":
            nameStr = first + " " + surname
        else:
            nameStr = title + " " + first + " " + surname
        self.name.SetLabel(nameStr)

        address = self.DBStr(row[PatentTable.IDX_ADDRESS])
        town = self.DBStr(row[PatentTable.IDX_TOWN])

        address1Str = address + " " + town
        self.address.SetLabel(address1Str)

        county = "West Sussex"
        postcode = self.DBStr(row[PatentTable.IDX_POST_CODE])

        self.county.SetLabel(county)
        self.post.SetLabel(postcode)

        Home = self.DBStr(row[PatentTable.IDX_HOME_PHONE])
        Work = self.DBStr(row[PatentTable.IDX_WORK_PHONE])
        Mobile = self.DBStr(row[PatentTable.IDX_MOBILE])

        phoneStr = "Home " + Home + " Work " + Work

        if Mobile == None:
            mobileStr = "Mobile " + Mobile
        else:
            mobileStr = ""

        self.phone.SetLabel(phoneStr)
        self.mobile.SetLabel(mobileStr)

        email = self.DBStr(row[PatentTable.IDX_EMAIL])
        if email != None:
            self.email.SetLabel(email)
        else:
            self.email.SetLabel("")

class PatentBookCtrl(wx.Notebook):

    def __init__(self, parent):
        super(PatentBookCtrl, self).__init__(parent, size=(500,300))

        self.patentTable = PatentTable()
        self.rows = self.patentTable.showAll()
        self.patentListCtrl = PatentListCtrl(self)
        self.patentListCtrl.populateList(self.rows)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNoteBookPageChanged)

        self.AddPage(self.patentListCtrl, "A")
        self.AddPage(self.patentListCtrl, "B")
        self.AddPage(self.patentListCtrl, "C")
        self.AddPage(self.patentListCtrl, "D")
        self.AddPage(self.patentListCtrl, "E")
        self.AddPage(self.patentListCtrl, "F")
        self.AddPage(self.patentListCtrl, "G")
        self.AddPage(self.patentListCtrl, "H")
        self.AddPage(self.patentListCtrl, "I")
        self.AddPage(self.patentListCtrl, "J")
        self.AddPage(self.patentListCtrl, "K")
        self.AddPage(self.patentListCtrl, "L")
        self.AddPage(self.patentListCtrl, "M")
        self.AddPage(self.patentListCtrl, "N")
        self.AddPage(self.patentListCtrl, "O")
        self.AddPage(self.patentListCtrl, "P")
        self.AddPage(self.patentListCtrl, "Q")
        self.AddPage(self.patentListCtrl, "R")
        self.AddPage(self.patentListCtrl, "S")
        self.AddPage(self.patentListCtrl, "T")
        self.AddPage(self.patentListCtrl, "WXYZ")
        self.AddPage(self.patentListCtrl, "All")




    def GetItem(self, itemId, col=0):
        return self.patentListCtrl.GetItem(itemId, col)

    def GetRows(self):
        return self.rows

    def GetSelectStr(self, idx):
        whereStr = ("\'A%\'", "\'B%\'", "\'C%\'", "\'D%\'", "\'E%\'", "\'F%\'", "\'G%\'", "\'H%\'", "\'I%\'",
                        "\'J%\'", "\'K%\'", "\'L%\'", "\'M%\'", "\'N%\'", "\'O%\'", "\'P%\'" "\'Q%\'", "\'R%\'", "\'S%\'", "\'T%\'", "\'[W-Z]\'")
        return "select * from patent where surname like " + whereStr[idx] + " order by surname;"

    def OnNoteBookPageChanged(self, event):
        pageIdx = self.GetSelection()
        self.rows = self.patentTable.execfetchall(self.GetSelectStr(pageIdx))
        #self.patentListCtrl.ClearAll()
        self.patentListCtrl.populateList(self.rows)
        print pageIdx

class PatentListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(PatentListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(500,300))

        self.InsertColumn(0, "Period")
        self.InsertColumn(1, "Type")
        self.InsertColumn(2, "Volume Set Label")
        self.InsertColumn(3, "Location")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 50)
        self.SetColumnWidth(1, 100)
        self.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        self.rows = data
        self.DeleteAllItems()
        for row in data:
            item = row[1], row[2], row[3], row[4]
            self.Append(item)

    
    def OnClicked(self, event):
        self.selected_row = event.GetIndex()
        self.rows[self.selected_row]
        patentEditDialog = PatentEditDialog()
        patentEditDialog.ShowModal()

    def OnItemSelected(self, event):
        self.selected_row = event.GetIndex()
        val = list()
        for column in range(1,3):
            item = self.GetItem(self.selected_row, column)
            val.append(item.GetText())
        frame = self.GetTopLevelParent()
        frame.PushStatusText(" ".join(val))
    

class MainFrame(wx.Frame):
    
    def __init__(self, parent, id=wx.ID_ANY, title="",pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name ="myFrame"):
        super(MainFrame, self).__init__(parent, id, title, pos, size, style, name)

        self.panel = MainPane(self)
    
class MainPane(wx.Notebook):

    def __init__(self, parent):
        super(MainPane, self).__init__(parent, style=wx.NB_LEFT)

        self.patentsCtrl = PatentsCtrl(self)
        self.AddPage(self.patentsCtrl, "Patents")


class TestApp(wx.App):
    
    def OnInit(self):
        frame = MainFrame(None, title="The Main Frame")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()
