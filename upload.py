import os, sys, ftplib
from getpass import getpass
from mimetypes import guess_type

nonppassive = False
remotesite = '115.159.95.68'
remotedir='.'
remoteuser='ftpluofun'
remotepass=getpass('Password for %s on %s : '%(remoteuser,remotesite))
localdir='.'
cleanall=input('Clean remote directory first?')[:1] in ['y','Y']

print('conecting...')
connection=ftplib.FTP(remotesite)
connection.login(remoteuser,remotepass)
connection.cwd(remotedir)
if nonppassive:
	connection.set_pasv(False)
if cleanall:
	for remotename in connection.nlst():
		try:
			print('deleting remote ',remotename)
			connection.delete(remotename)
		except:
			print('cannot delete remote', remotename)
count=0
localfiles=os.listdir(localdir)
for localname in localfiles:
	mimetype,encoding=guess_type(localname)
	mimetype=mimetype or '?/?'
	maintype=mimetype.split('/')[0]
	localpath=os.path.join(localdir,localname)
	print('uploading ',localpath,'to',localname,end=' ')
	print('as', maintype, encoding or '')
	localfile=open(localpath,'rb')
	connection.storbinary('STOR ' + localname,localfile)
	localfile.close()
	count+=1
connection.quit()
print('Done:', count,'file uploaded')
