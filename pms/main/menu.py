'''
Created on Jul 9, 2013

@author: wzw7yn
'''
import wx

ID_IMPORT = wx.ID_ANY
ID_EXPORT = wx.ID_ANY

def MainMenu():
    menu_bar = wx.MenuBar()
    # File Menu
    file_menu = wx.Menu();
    #file_menu.Append(wx.NewId(), "New")
    file_menu.Append(wx.ID_NEW)
    file_menu.Append(wx.ID_OPEN)

    file_menu.Append(wx.ID_SEPARATOR)
    file_menu.Append(wx.ID_CLOSE)
    #file_menu.Append(wx.ID_CLOSE_ALL)
    file_menu.Append(wx.ID_SEPARATOR)
    file_menu.Append(wx.ID_SAVE)
    file_menu.Append(wx.ID_SAVEAS)
    file_menu.Append(wx.ID_SEPARATOR)
    file_menu.Append(ID_IMPORT, "Import")
    file_menu.Append(ID_EXPORT, "Export")
    file_menu.Append(wx.ID_SEPARATOR)
    file_menu.Append(wx.ID_PREFERENCES)
    file_menu.Append(wx.ID_SEPARATOR)
    file_menu.Append(wx.ID_EXIT)
    #file_menu.Append(wx.NewId(), "Exit")
    #Edit Menu
    edit_menu = wx.Menu()
    edit_menu.Append(wx.ID_UNDO)
    edit_menu.Append(wx.ID_REDO)
    edit_menu.Append(wx.ID_SEPARATOR)
    edit_menu.Append(wx.ID_COPY)
    edit_menu.Append(wx.ID_CUT)
    edit_menu.Append(wx.ID_PASTE)
    edit_menu.Append(wx.ID_SEPARATOR)
    edit_menu.Append(wx.ID_DELETE)
    edit_menu.Append(wx.ID_SELECTALL)
    edit_menu.Append(wx.ID_SEPARATOR)
    edit_menu.Append(wx.ID_FIND)

        #Edit Menu
    view_menu = wx.Menu()
    view_menu.Append(wx.ID_VIEW_DETAILS, "Details")
    view_menu.Append(wx.ID_VIEW_LARGEICONS, "Large Icons")
    view_menu.Append(wx.ID_VIEW_LIST, "List")
    view_menu.Append(wx.ID_VIEW_SMALLICONS, "Small Icons")
    view_menu.Append(wx.ID_SEPARATOR)
    view_menu.Append(wx.ID_ZOOM_100)
    view_menu.Append(wx.ID_ZOOM_FIT)
    view_menu.Append(wx.ID_ZOOM_IN)
    view_menu.Append(wx.ID_ZOOM_OUT)

        #Edit Menu
    view_menu = wx.Menu()
    view_menu.Append(wx.ID_VIEW_DETAILS, "Details")
    view_menu.Append(wx.ID_VIEW_LARGEICONS, "Large Icons")
    view_menu.Append(wx.ID_VIEW_LIST, "List")
    
    # Main menu bar
    menu_bar.Append(file_menu, "File")
    menu_bar.Append(edit_menu, "Edit")
    menu_bar.Append(view_menu, "View")

    return menu_bar
