import cv2, numpy as np
from PIL import Image
out='experiences/01-arrival/sketch/assets/'
img=cv2.imread('experiences/03-leap/moodboard/leap-collage-walkers-torn-field.png')
H,W=img.shape[:2]
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
sat=hsv[...,1]; val=hsv[...,2]
hue=hsv[...,0]
col=((sat>28)&(((hue>=15)&(hue<=40))|((hue>=85)&(hue<=115)))).astype(np.uint8)
col=cv2.morphologyEx(col,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
# keep largest colour blob = the field/sky in the tear
n,lab,st,cen=cv2.connectedComponentsWithStats(col)
keep=[i for i in range(1,n) if st[i,cv2.CC_STAT_AREA]>150 and 260<cen[i][0]<420]
col=np.isin(lab,keep).astype(np.uint8)
col=cv2.morphologyEx(col,cv2.MORPH_CLOSE,np.ones((15,15),np.uint8))
col=cv2.morphologyEx(col,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
# fill holes (people in front of the field) by filling contour
cnts,_=cv2.findContours(col,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
fill=np.zeros_like(col); cv2.drawContours(fill,cnts,-1,1,-1)
tear_inner=fill
# white paper edge: bright pixels near the colour region
near=cv2.dilate(tear_inner,np.ones((25,25),np.uint8))
white=((val>200)&(sat<40)).astype(np.uint8)&near
tear=cv2.morphologyEx(tear_inner|white,cv2.MORPH_CLOSE,np.ones((7,7),np.uint8))
# people: dark pixels in lower-left area
lum=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
region=np.zeros_like(lum); region[262:470,0:350]=1
dark=((lum<75)&(region>0)).astype(np.uint8)
dark=cv2.morphologyEx(dark,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
n,lab,st,_=cv2.connectedComponentsWithStats(dark)
people=np.zeros_like(dark)
for i in range(1,n):
    if st[i,cv2.CC_STAT_AREA]>60: people[lab==i]=1
people=cv2.dilate(people,np.ones((3,3),np.uint8))
pd=cv2.dilate(people,np.ones((9,9),np.uint8))
plate=cv2.inpaint(img,pd*255,5,cv2.INPAINT_TELEA).astype(np.float32)
rng=np.random.default_rng(1)
grain=rng.normal(0,14,plate.shape[:2]).astype(np.float32)[...,None]
pa=cv2.GaussianBlur(pd.astype(np.float32),(0,0),3)[...,None]
plate=plate+grain*pa
src=np.roll(plate,150,axis=1)
ta=cv2.GaussianBlur(cv2.dilate(tear,np.ones((25,25),np.uint8)).astype(np.float32),(0,0),4)[...,None]
plate=np.clip(plate*(1-ta)+src*ta,0,255)
cv2.imwrite(out+'leap-plate.jpg',plate.astype(np.uint8),[cv2.IMWRITE_JPEG_QUALITY,88])
rgba=cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
t=rgba.copy(); t[...,3]=cv2.GaussianBlur(tear*255,(3,3),0); cv2.imwrite(out+'leap-tear.png',t)
p=rgba.copy(); p[...,3]=cv2.GaussianBlur(people*255,(3,3),0); cv2.imwrite(out+'leap-people.png',p)
ys,xs=np.where(tear>0); print('tear bbox',xs.min(),ys.min(),xs.max(),ys.max())
ys,xs=np.where(people>0); print('people bbox',xs.min(),ys.min(),xs.max(),ys.max())
# logo layers
L=Image.open('../../ref/sor-logo-bird-prints.png').convert('RGB').resize((800,800),Image.LANCZOS)
a=np.array(L).astype(int); r,g,b=a[...,0],a[...,1],a[...,2]
darkm=(r<90)&(g<90)&(b<90)
redness=np.clip((r-(g+b)/2)/255*2.2,0,1)
ring=np.dstack([np.full_like(r,225),np.full_like(r,20),np.full_like(r,20),(redness*255).astype(int)]).astype(np.uint8)
Image.fromarray(ring,'RGBA').save(out+'logo-ring.png',optimize=True)
sw=np.dstack([np.zeros_like(r),np.zeros_like(r),np.zeros_like(r),(darkm*255)]).astype(np.uint8)
im=Image.fromarray(sw,'RGBA'); bb=im.getbbox(); im.crop(bb).save(out+'swallow.png',optimize=True); print('swallow bbox',bb)
Image.open('experiences/02-book/moodboard/kiefer-lead-book-open.webp').save(out+'kiefer-book.webp')
cv2.imwrite(out+'debug-masks.png',np.hstack([tear*255,people*255]))
