'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx
import os

from wx.adv import PyWizardPage
from wx.adv import Wizard
from wx import FileDialog
from cpdlists import FilesListCtrl
from cpdlists import WebLinksCtrl
from utils.copyattachments import Attachments

class CPD_OtherPage(PyWizardPage):

    def __init__(self, parent, gpInfo):
        PyWizardPage.__init__(self, parent)
        self.prev = self
        self.next = self
        self.__DoLayout()
        self.SetInitialSize()
        self.Bind(Wizard.EVT_WIZARD_PAGE_CHANGED, self.OnPageChanged)
        self.gpInfo = gpInfo
        self.Done = False;

    def SetPrev(self, prev):
        self.prev = prev
        return self.prev

    def SetNext(self, next):
        self.next = next
        return self.next
    def GetNext(self):
        return self.next
    def GetPrev(self):
        return self.prev


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
        self.addButton = wx.Button(self, -1, "Add", size=(50, 23))
        self.deleteButton = wx.Button(self, -1, "Delete", size=(50, 23))

        btnSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer.Add(self.addButton)
        btnSizer.Add(self.deleteButton)

        self.listCtrl.Bind(wx.EVT_LISTBOX_DCLICK , self.OnItemSelected)
        self.listCtrl.Bind(wx.EVT_LISTBOX , self.OnClicked)
        self.addButton.Bind(wx.EVT_BUTTON , self.OnAdd)
        self.deleteButton.Bind(wx.EVT_BUTTON , self.OnDelete)

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
        grpSizer.Add(btnSizer, (2, 3))


        grpSizer.Add(webLinksLbl, (3, 1))
        grpSizer.Add(self.webLinksCtrl, (3, 2)) #wx.FIXED_MINSIZE

        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)


    def OnItemSelected(self, event):
        print "Here 1"

    def OnClicked(self, event):
        self.selection = self.listCtrl.GetSelection()

    def OnAdd(self, event):
        '''
        dialog = AddDialog("Add Option", None)
        if dialog.ShowModal() == wx.ID_OK:
            print dialog.GetOption()
            self.listCtrl.AppendAndEnsureVisible(dialog.GetOption())
        '''
        wildcard = "All Files (*.*) | *.* |" \
                   "source (*.py) | *.py |" \
                   "Doc Files (*.doc) | *.doc"
        dialog = FileDialog(self, "Attach files", os.getcwd(), "", "*.*", FileDialog.OPEN | FileDialog.MULTIPLE)
        if dialog.ShowModal() == wx.ID_OK:
            
            fullList = dialog.GetPaths()
            self.attachments.copy(fullList)
            for item in self.attachments.GetFilenames():
                self.listCtrl.Append(item)
                
        dialog.Destroy()
   
    def OnDelete(self, event):
        fstr = self.listCtrl.GetString(self.selection)
        print fstr
        self.attachments.Delete(fstr)
        self.listCtrl.Delete(self.selection)

    def IsDone(self):
        return self.Done


    def OnPageChanged(self, event):
        print "EVT_WIZARD_PAGE_CHANGED"
        self.Done = True

    def GetPageInfo(self):
        pass
        #return self.gpInfo

