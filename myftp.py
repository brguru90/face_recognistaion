import ftplib

#ftp = ftplib.FTP('185.27.134.11', 'epiz_21569788', 'guruven1')
ftp = ftplib.FTP('localhost', 'guru', 'guruven1')
ftp.cwd("./human_faces/")

def download_from_ftp(file_name):
	print("downloading from ftp: "+file_name)
	f = open("./human_faces2/"+file_name, "wb")
	ftp.retrbinary('RETR '+file_name, f.write)
	f.close()
def upload_to_ftp(file_name):
	print("uploading to ftp: "+file_name)
	f = open("./human_faces1/"+file_name,'rb') 
	ftp.storbinary('STOR '+file_name, f) 
	f.close() 
	
def list_files():
  files = []

  def dir_callback(line):
    bits = line.split()

    if ('d' not in bits[0]):
      files.append(bits[-1])

  ftp.dir(dir_callback)
  return files 

def print_file():
	files=list_files()
	for file in files:
		print(file)