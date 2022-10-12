import os,time,datetime,platform,sys
from random import randint
#!/usr/bin/python3
# NOTE: Pleasearchterm Change ippath and mainpath to their right location
ippath=['/home/pxki/jobs/parch/medleip/','/home/pxki/jobs/parch/ips/']
mainpath='/home/pxki/web/'
slist=[sys.argv[0]]
#ippath='/home/pxki/Documents/doodle/ips/'
#print('OSsearchterm 2022 Modified For Doodle')
#current_month = strftime('%B')
color="white"
bgcolor="#6b2f65"
#bgcolor='#'+str(randint(111111,333333))
def check(url):
    x=0
    for a in url:
        if os.path.isdir(a):
            x+=1
        else:
            pass
    if x>0:
        return True
    else:
        return False
if not os.path.isfile(mainpath+'sename'):
 sename=str(input('Please set the Name of the Search Engine: '))
 if sename=='':
  sename=str(platform.system())
 f=open(mainpath+'sename','w')
 f.write(str(sename))
 f.close()
port=80
maxse=500//2
seek=0
additional='Powered By RPi 3'
organisation='Pxki LCC.'
debug=True
#aces=['']
faces=['QwQ','qwq','-w-','OwO','UnU','O-U','U-U','X-X','>-<','>w<','ewe','^w^','0v0','0n0']
home=0
page=0
pagestart=0
searchterm=''
pagetrack=0
files=[]
for aa in ippath:
    for a in os.listdir(aa):
        if 'ips' in aa:
         prefix='legacy-'
        else:
         prefix='medle-'
        files.append(prefix+a)
def textnot(ts):
 if home:
  t=['U are Cute!','*Kisses* hehe','Welcome!','Ever Heard of Hyperpop?','i was used to be called Doodle,Hexo hehe','Being a Hacker is Awesome!','Unfiltered Search Results!','Better than Bing lol','School kinda sucks when you do not learn anything lol']
 else:
  t=['404:  Nothing Here bud but u cul','404: Am i smart?.... Nope LOL','404: Am i dumb?.... Maybe','404: Whats the real name of Pxki?','404: I love U <3']
 return t[randint(1,len(t))-1]
vmode=False
def get(crub):
        global message,home,vmode,maxse,pagetrack,page,searchterm
        if os.path.isfile(mainpath+'pause'):
         print('<h1>Sorry!, We are having ongoing maintenance right now. Sorry for the innconvience</h1>Created '+str(str(datetime.datetime.fromtimestamp(os.stat(mainpath+'pause').st_mtime).strftime('%Y/%m/%d %H:%m'))))
         exit()
        vmode=False
        x=''
        for a in sys.argv[1:]:
              x+=a
        urlmsg=x.replace('/','')
#        self.send_response(200)
#        self.send_header('Content-type','text/html')
#        self.end_headers()
        seek=0
        times=time.time()
        sename=open(mainpath+'sename').read().replace('\n','')
        tmp7=datetime.datetime.now()
        month=tmp7.strftime("%m")
        if month=='06':
         titletext='<h2>Happy <span style="color:red;">P</span><span style="color:orange;">r</span><span style="color:yellow;">i</span><span style="color:green;">d</span><span style="color:purple;">e</span> Month <3</h2>'
        else:
         titletext='<h1>Dub9</h1><h2>Welcome Hacker</h2>'
        for tmp in ippath:
            if os.path.isdir(tmp):
                urlnum=0
                for tmp in ippath:
                    if os.path.isfile(tmp+files[-1].replace('legacy-','').replace('medle-','')):
                        urlnum+=(len(open(tmp+files[-1].replace('legacy-','').replace('medle-','')).readlines()))*len(files)
            else:
                urlnum=0
        tac=0
        #for a in files:
        #  urlnum+=len(open(ippath+a).readlines())-2
        if urlmsg=='':
         home=True
         template=open(mainpath+'home.htm').read().replace('+urlnum+',str(urlnum)).replace('+holiday+',titletext).replace('+name+',sename).replace('+bgcolor+',bgcolor).replace('+color+',color)
        else:
         home=False
         if os.path.isfile(mainpath+'template.htm'):
          template=open(mainpath+'template.htm').read().replace('+urlnum+',str(urlnum)).replace('+holiday+',titletext).replace('+name+',sename).replace('+bgcolor+',bgcolor).replace('+color+',color)
         else:
          template='<html><title>'+str(sename)+'</title><center><h1>'+str(sename)+'</h1><h2>There Are '+str(urlnum)+' Pages Cached</h2><body><form action="/search" method="GET"><input type="text" id="seo" name="seo" minlength="2" maxlength="64" required><button type="submit">Search</button></form>'
        tmp=''
        path=urlmsg
        if path=='':
         message = template
        else:
         message = template
#         message+='<div class="body">'
         se=path.replace('+',' ').lower().split('?')[:256]
#         print(se)
         setag=1
         searchterm=se[1].replace('seo=','')
         if len(se)>2:
          setag=se[2]
          if "page=" in setag:
           setag=setag.replace('page=','')
           if setag.isnumeric():
            setag=int(setag)
           else:
            setag=1
         elif len(se)>1:
          searchterm=se[1].replace('seo=','')
          setag=1
         else:
          setag=1
         page=setag
#         f=open(mainpath+'history_of_search','a')
#         f.write(se+' - '+str(int(time.time()))+' \n')
#         f.close()
         template=''
         message=message.replace('+searchname+',searchterm)
         if not check(ippath):
          message+='<h2 style="margin: 30px 0px 0px 10px;">The Database is corrupt or not found</h2>'
          print(message)
          exit()
         else:
          message+='<p style="margin: 30px 0px -5px 10px;;color:white;font-family:URW Gothic L;">You are on Page '+str(page)+'</p>'
         if urlmsg=='?seo=%3Fsource':
          message=open(sys.argv[0]).read()
         elif urlmsg=='?seo=%3Fversion':
          vmode=True
          toki=0
          for a in slist:
            toki+=os.stat(a).st_size
          message='<h1>[Legacy] Dub9 Web v'+str(toki//100)+'.'+str(toki//10)[-1]+'</h1>'
          message+='<a href="/">[Go Home]</a>'
          home=False
          tac=1
         else:
          for tmp2 in files:
           tmp2=tmp2.split('-')
           filetype=tmp2[0]
           tmp2=tmp2[1]
           if filetype=='medle':
               prefix=ippath[0]
               tmp3=open(prefix+tmp2)
           else:
               prefix=ippath[1]
               tmp3=open(prefix+tmp2)
           if not tac>=maxse:
            if searchterm.lower() in open(prefix+tmp2).read().lower():
             for tmp4 in reversed(list(tmp3)):
                if not tac>=maxse:
                 tmp4=tmp4.replace('\n','')
                 if not "\\" in tmp4:
                  iptmp=tmp4.split(' - ')
#                  if len(iptmp)>2:
#                   iptmp[1]=iptmp[1:]
#                  print(iptmp)
                  if len(iptmp)<=1:
                   pass
                  else:
                   iptip=len(iptmp)
                   if iptip>2:
                     iptimey=True
                   else:
                     iptimey=False
                   if iptimey:
                       try:
                           iptime=int(iptmp[0])
                       except Exception:
                           iptime=os.stat(prefix+tmp2).st_mtime
                   else:
                     iptime=os.stat(prefix+tmp2).st_mtime
                   if iptip<3:
                       ipname=iptmp[0].replace(' ','')
                       iptext=iptmp[1]
                   else:
                       ipname=iptmp[1].replace(' ','')
                       iptext=iptmp[2]
                   if len(iptext)<2:
                    iptext='Untited ('+str(ipname)+')'
                  iptmp=''
#                   break

#                num=0
#                exit()
#                for tmp5 in tmp4:
#                 num+=1
#                 if tmp5=='-':
#                  ipname, iptext=tmp4[:num].replace('-','').replace(' ',''), tmp4[num+1:].replace('-','')
#                  iptmp
#                  iptmp=iptext.lower()
#                  if len(iptext)<2:
#                   iptext='Untited URL ('+str(ipname)+')'
#                  break
              #print(ipname+' ('+str(iptext)+')')
                  if "http" in ipname:
                    if searchterm in iptext.lower():
                     tac+=1
                     message+='<br><a target="_blank" href="'
                     message+=ipname+'"'
                     message+='><p style="margin: 0px 0px 0px 10px;color:white;font-family:URW Gothic L;" >'+iptext
#                    if debug==True:
#                     message+=' (in Server '+str(tmp2).replace('.txt','')+')'
                     if 'medle' in prefix:
                         nprefix='Modern'
                     else:
                         nprefix='Legacy'
                     message+='</p></a></br><p style="margin: -15px 0px 0px 10px;font-size:15;font-family:URW Gothic L;color:#d1d1d1;">'+str(datetime.datetime.fromtimestamp(int(iptime)).strftime('%Y/%m/%d %H:%M'))+' - '+str(ipname)+' (Used '+str(nprefix)+' Database)</p>'
                else:
                  pass
            else:
             pass
           else:
            break
        if not 'old'=='server':
         if not vmode:
          if tac <1:
           message+='<h3 style="text-align:center;margin:50px 0px 0px 0px;">'+str(textnot(home))+' '+str(faces[randint(1,len(faces))-1])+'<h3>'
#          message+='<center>'
#          if tac>=maxse:
#           teco=0
#           for a in files:
#            for b in open(ippath+a):
#             if searchterm in b.lower():
#              yes=True
#            if yes:
#             teco+=1
#             message+='<a href="'
#             message+='/search?seo='+se+'?page='+str(teco)
#             message+='">['+str(teco)+']</a>'
#            yes=False
#           message+='</center>'
          if not home:
            for a in range(1,(pagetrack//250)+1):
             message+='<a style="margin:0px -8px 0px 10px;" href="'
             message+='?seo='+searchterm+'?page='+str(a)+'"><button>'+str(a)+'</button></a>'
          footer='<br><br></br></br></center><div class="footer"><b style="font-family:URW Gothic L;margin: 10px 0px 0px 10px;">'+str(tac)+' Urls ('+str(int((time.time()-times)/0.01))+'ms)</b><b style="float:right;margin: 0px 10px 0px 10px;font-family:URW Gothic L;">There Are '+str(urlnum)+' Urls in our Database</b><br><b style="font-family:URW Gothic L;margin: 10px 0px 0px 10px;">'+organisation+' Copyright 2022-'+str(int(1970+(time.time()//31536000)))+'</b><a href="/"><b style="font-family:URW Gothic L;float: right;margin: 0px 10px 0px 10px;color:white;" >Return to Home</b></a></br></div>'
          message+=footer
#         message=message.replace('<center>','').replace('</center>','')
#        if not "version" in se:
        if os.path.isfile(mainpath+'warning'):
         message+='<div class="warn">'+str(open(mainpath+'warning').read())+'</div>'
        if os.path.isfile(mainpath+'notice'):
         message+='<div class="notice">'+str(open(mainpath+'notice').read())+'</div>'
#        self.wfile.write(bytes(message, "utf8"))
        return message
#
#with HTTPServer(('0.0.0.0', port), handler) as server:
#    server.serve_forever()
#try:
print(get(''))
print('<! osu! is my fav game >')
for a in ippath:
    if os.path.isdir(a):
      x=True
    else:
      x=False
if x:
    print('<! URLS:'+str(len(files))+' >')
#except Exception as error:
#  print(str(error))
