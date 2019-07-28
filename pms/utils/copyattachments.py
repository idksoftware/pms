'''
Created on Mar 5, 2014

@author: wzw7yn
'''
import shutil
import os

class Attachments():
    
    def __init__(self, repos):
        self.repos = repos
        
    def copy(self, filesList):
        self.attachment_id = 0
        if os.path.exists(self.repos) == False:
            os.mkdir(self.repos)
            if os.path.exists(self.repos) == False:
                return -1
        self.attIdList = os.listdir(self.repos)
        print self.attIdList
        self.attachment_id = self.GetLastId() + 1
        dirid = "%.4d" % self.attachment_id
        self.idpath = os.path.join(self.repos, dirid)
        os.mkdir(self.idpath)
        self.fnamelist = list()
        for item in filesList:
            fname = os.path.basename(item)
            self.fnamelist.append(fname)
            shutil.copy2(item, os.path.join(self.idpath, fname))        
    
    def GetFilenames(self):
        return self.fnamelist
    
    def GetAttachmentId(self):
        return self.attachment_id
    
    def Delete(self, filen):
        os.unlink(os.path.join(self.idpath, filen))
    
    def GetLastId(self):
        idx = 0
        for item in self.attIdList:
            nid = int(item)
            if idx < nid:
                idx = nid
        return idx  
    
    

if __name__=="__main__":
    #cfg = OptionReader()
    #cfg.read("/home/wzw7yn/workspace/pms/main/options.xml")
    #cfg.write("/home/wzw7yn/workspace/pms/main/test.xml")
    flist = (
            "/home/wzw7yn/test/echo.xml",
            "/home/wzw7yn/test/javalogging.xml",
            "/home/wzw7yn/test/jecho.xml",
            "/home/wzw7yn/test/mission.xml"
            )
    attachments = Attachments("/home/wzw7yn/pms/repos")
    attachments.copy(flist)
    