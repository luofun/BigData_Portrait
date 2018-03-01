import os, sys, ftplib
from getpass import getpass
from mimetypes import guess_type

nonppassive = False
remotesite = '115.159.95.68'
remotedir='.'
remoteuser='ftpluofun'
remotepass=getpass('Password for %s on %s : '%(remoteuser,remotesite))
localdir='.'
cleanall=input('Clean local directory first?')[:1] in ['y','Y']

print('conecting...')
connection=ftplib.FTP(remotesite)
connection.login(remoteuser,remotepass)
connection.cwd(remotedir)
if nonppassive:
	connection.set_pasv(False)
if cleanall:
	for localname in os.listdir(localdir):
		try:
			print('deleting local',localname)
		except:
			print('cannot delete local',localname)

count=0
remotefiles=connection.nlst()

for remotename in remotefiles:
	if remotename in ('.','..') : continue
	mimetype,encoding=guess_type(remotename)
	mimetype=mimetype or '?/?'
	maintype=mimetype.split('/')[0]
	localpath=os.path.join(localdir,remotename)
	print('downloading', remotename,'to', localpath,end=' ')
	print('as',maintype,encoding or '')
	
	localfile=open(localpath,'wb')
	connection.retrbinary('RETR '+remotename,localfile.write)
	
	localfile.close()
	count+=1
connection.quit()
print('Done:',count,'frist downloaded.')