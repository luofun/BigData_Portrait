import os,sys,ftplib
from getpass import getpass
from mimetypes import guess_type,add_type

nonppassive = False
remotesite = '115.159.95.68'
remotedir='.'
remoteuser='ftpluofun'
remotepass=getpass('Password for %s on %s : '%(remoteuser,remotesite))
localdir='.'

print('conecting...')
connection=ftplib.FTP(remotesite)
connection.login(remoteuser,remotepass)
connection.cwd(remotedir)
if nonppassive:
	connection.set_pasv(False)

class UploadAll:
	def __init__(self):
		self.fcount=self.dcount=0

	def getcleanall(self):
		return False

	def uploadOne(self,localname,localpath,remotename):
		localfile=open(localpath,'rb')
		connection.storbinary('STOR ' + remotename,localfile)
		localfile.close()

	def uploadDir(self,localdir):
		localfiles=os.listdir(localdir)
		for localname in localfiles:
			localpath=os.path.join(localdir,localname)
			print('uploading', localpath,'to',localname)
			if not os.path.isdir(localpath):
				self.uploadOne(localname,localpath,localname)
				self.fcount+=1
			else:
				try:
					print(localpath)
					self.connection.mkd(localname)
					print('directory created')
				except:
					print('directory not created')
				connection.cwd(localname)
				self.uploadDir(localpath)
				connection.cwd('..')
				self.dcount+=1
				print('directory exited')

if __name__ == '__main__':
	ftpclasstest=UploadAll()
	ftpclasstest.uploadDir(localdir)
	connection.quit()
	print('Done:', ftpclasstest.fcount,'file uploaded and ',ftpclasstest.dcount,'driectory created')