#!/usr/bin/python3
# NOTE: Please Change ippath and mainpath to their right location
ippath='/home/pxki/Documents/parch/ips/'
mainpath='/home/pxki/web/'
#ippath='/home/pxki/Documents/doodle/ips/'
print('OSSE 2022 Gen 2')
import os,time,platform
from http.server import BaseHTTPRequestHandler, HTTPServer
if not os.path.isfile(mainpath+'sename'):
 sename=str(input('Please set the Name of the Search Engine: '))
 if sename=='':
  sename=str(platform.system())
 f=open(mainpath+'sename','w')
 f.write(str(sename))
 f.close()
maxse=200
sename=open(mainpath+'sename').read().replace('\n','')
additional='Powered By Raspberry Pi 3 B+'
organisation='Pxki Inc.'
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global message
        urlnum=0
        tac=0
        for a in os.listdir(ippath):
         urlnum+=len(open(ippath+a).readlines())-2
        if os.path.isfile(mainpath+'template.htm'):
         template=open(mainpath+'template.htm').read().replace('+urlnum+',str(urlnum))
        else:
         template='<html><title>'+str(sename)+'</title><center><h1>Doodle</h1><h2>There Are '+str(urlnum)+' Pages Cached</h2><body><form action="/search" method="GET"><input type="text" id="seo" name="seo" minlength="2" maxlength="64" required><button type="submit">Search</button></form>'
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        tmp=''
        path=self.path[1:]
        if path=='favicon.ico':
         pass
        elif path=='font.ttf':
         tmp=open(mainpath+'font.ttf','rb').read()
         self.wfile.write(bytes(tmp))
         tmp=''
        elif path=='':
         message = template
        else:
         message = template
         se=path.replace('search?seo=','')
#         f=open(mainpath+'history_of_search','a')
#         f.write(se+' - '+str(int(time.time()))+' \n')
#         f.close()
         if not os.path.isdir(ippath):
          message+='<h2>Contact your Administrator</h2><h3>Admin First setup not Finished</h3>'
         else:
          for tmp2 in os.listdir(ippath):
           tmp3=open(ippath+tmp2)
           for tmp4 in tmp3.readlines():
            if not tac>=maxse:
             tmp4=tmp4.replace('\n','')
             if not "\\" in tmp4:
              ipname=''
              iptext=''
              num=0
              for tmp5 in tmp4:
               num+=1
               if tmp5=='-':
                ipname=tmp4[:num].replace('-','').replace(' ','')
                iptext=tmp4[num+1:].replace('-','')
                break
             #print(ipname+' ('+str(iptext)+')')
              if se.lower() in iptext.lower():
               tac+=1
               message+='<h3><a target="_blank" href="'
               message+=ipname+'"'
               message+='>'+iptext+'</a></h3>'
            else:
             break
        if not path=='font.ttf':
         footer='<br></br><div class="footer"><b style="font-family:URW Gothic L">Loaded '+str(tac)+' ('+str(additional)+')</b><br><b style="font-family:URW Gothic L">'+organisation+' Copyright 2022-'+str(int(1970+(time.time()//31536000)))+'</b></br></div>'
         message+=footer
         self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 80), handler) as server:
    server.serve_forever()
