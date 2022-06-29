import glob, shutil

class getFiles:
    def __init__(self, extension, target):
        self.Ex = extension
        self.allFolders = []
        self.allFiles = []
        self.target = target
        self.error = []
        self.Coped = 0
    def findAllFolders(self):
        Old = -1
        New = 0
        while Old < New:
            Old = len(self.allFolders)
            if len(self.allFolders) == 0:
                all = glob.glob('*')
                self.getFiles('')
                for i in all:
                    if '.' not in i and i != self.target:
                        self.allFolders.append(i)
                        self.getFiles(i)
                self.findAllFolders()
            else:
                for i in self.allFolders:
                    new = glob.glob(f'{i}\\*')
                    for i in new:
                        if '.' not in i and i not in self.allFolders:
                            self.allFolders.append(i)
                            self.getFiles(i)
            New = len(self.allFolders)

    def getFiles(self, path):
        newFiles = glob.glob(f'{path}\\*.{self.Ex}')
        self.allFiles += newFiles
        self.copyFiles(newFiles)


    def copyFiles(self, newFiles):

        for i in newFiles:
            x = i.split('\\')[-1]
            xx = i.split('\\')[-2]
            try:
                shutil.copyfile(i, f'{self.target}\\{xx}-{x}')
                self.Coped += 1
            except:
                self.error.append(i)
            print(f'\r [~] Done find {self.Ex} >> Folders={len(self.allFolders)} | Files={len(self.allFiles)} | Coped={self.Coped} .', end='')


extension = input('enter extension for files you need : ')
target = input('Enter Folder To Copy in it : ')
start = getFiles(extension, target)
start.findAllFolders()
if len(start.error) != 0:
    print(f'''
     [~] Sorry Can't Copy this Files :( 
    {start.error}''')