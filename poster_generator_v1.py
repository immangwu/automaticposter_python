import csv
import random
import pandas as pd
def alignhorizontalcenter(content,font):
    textWidth, textHeight = imgDraw.textsize(content, font=font)
    xText = (width - textWidth) / 2
    return(xText)
##        yText = (height - textHeight) / 2
def rand_color():
    for i in range(3):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb = [r,g,b]
        rgb=tuple(rgb)
    return(rgb)

def colorcombo(i):
    if i==0:
        color1= (0,0,139)
        color2=(0,102,0)
        color3=(170,0,0)
        color5=(255, 255, 255)
    elif i==1:
        color1= (226, 216, 16) # forheader, the management, date,time,venue,department,designations
        color2=(217, 19, 138) # invitation,title,organised by,chiefguest,presided by
        color3=(255, 255, 255)#guestname and principal
        color5=(18, 164, 217) #bg
    elif i==2:
        color1= (207, 21, 120) # forheader, the management, date,time,venue,department,designations
        color2=(255, 255, 255) # invitation,title,organised by,chiefguest,presided by
        color3=(178, 2, 56)#guestname and principal
        color5=(232, 210, 29) #bg
    elif i==3:
        color1= (190, 21, 88) # forheader, the management, date,time,venue,department,designations
        color2=(50, 37, 20) # invitation,title,organised by,chiefguest,presided by
        color3=(231, 88, 116)#guestname and principal
        color5=(251, 203, 201) #bg
    elif i==4:
        color1= (239, 157, 16) # forheader, the management, date,time,venue,department,designations
        color2=(59, 77, 97) # invitation,title,organised by,chiefguest,presided by
        color3=(107, 123, 140)#guestname and principal
        color5=(255, 255, 255) #bg
    elif i==5:
        color1= (255, 110, 64) # forheader, the management, date,time,venue,department,designations
        color2=(30, 61, 89) # invitation,title,organised by,chiefguest,presided by
        color3=(255, 193, 59)#guestname and principal
        color5=(245, 240, 225) #bg
    elif i==6:
         color1= (30, 132, 127) # forheader, the management, date,time,venue,department,designations
         color2=(0, 0, 0) # invitation,title,organised by,chiefguest,presided by
         color3=(30, 132, 127)#guestname and principal
         color5=(236, 193, 156) #bg
    elif i==7:
         color1= (38, 73, 92) # forheader, the management, date,time,venue,department,designations
         color2=(196, 163, 90) # invitation,title,organised by,chiefguest,presided by
         color3=(198, 107, 61)#guestname and principal
         color5=(229, 229, 220) #bg
    elif i==8:
         color1= (138, 48, 127) # forheader, the management, date,time,venue,department,designations
         color2=(121, 167, 211) # invitation,title,organised by,chiefguest,presided by
         color3=(104, 131, 188)#guestname and principal
         color5=(255, 254, 253) #bg
    elif i==9:
         color1= (49, 104, 121) # forheader, the management, date,time,venue,department,designations
         color2=(244, 122, 96) # invitation,title,organised by,chiefguest,presided by
         color3=(127, 231, 220)#guestname and principal
         color5=(206, 215, 216) #bg
    elif i==10:
         color1= (255, 255, 255) # forheader, the management, date,time,venue,department,designations
         color2=(255, 255, 255) # invitation,title,organised by,chiefguest,presided by
         color3=(255, 255, 255)#guestname and principal
         color5=(3, 17, 99) #bg
    colors=[color1,color2,color3,color5]
    return colors
        
        

##colors forheader, the management,
##date,time,venue,department,designations lor1=(0,0,139) colors for
##invitation,title,organised by,chiefguest,presided by lor2=(0,102,0)
##colors for guest name , principal sir lor3=(170,0,0) colors for border
##, line olor4=(204,0,204) Color for background lor5=(255, 255, 255)
import pandas as pd
data = pd.read_excel('Data.xlsx')
###a=(data.loc[[0],['Type of Event','Event Title','Month','Time','am/pm','venue','Organized by','Guest Name','Designation','Department','Institution','City withpincode']])
##ToE=(data.loc[[0],['Type of Event']])
##ET=(data.loc[[0],['Event Title']])
##M=(data.loc[[0],['Month']])
##
##T=(data.loc[[0],['Time']])
##print(T)
##ap=(data.loc[[0],['am/pm']])
##V=(data.loc[[0],['venue']])
##Ob=(data.loc[[0],['Organized by']])
##GN=(data.loc[[0],['Guest Name']])
##D=(data.loc[[0],['Designation']])
##Dp=(data.loc[[0],['Department']])
##In=(data.loc[[0],['Institution']])
##Cp=(data.loc[[0],['City withpincode']])
##Yr=(data.loc[[0],['Year']])
##ToE=ToE.values.tolist(); ToE = str(ToE)[3:-3];
##ET=ET.values.tolist(); ET = str(ET)[3:-3];
##M=M.values.tolist(); M = str(M)[3:-3];
##T=T.values.tolist(); T = str(T)[3:-3];
##ap=ap.values.tolist(); ap = str(ap)[3:-3];
##V=V.values.tolist(); V = str(V)[3:-3];
##Ob=Ob.values.tolist(); Ob = str(Ob)[3:-3];
##D=D.values.tolist(); D = str(D)[3:-3];
##Dp=Dp.values.tolist(); Dp = str(Dp)[3:-3];
##In=In.values.tolist(); In = str(In)[3:-3];
##Cp=Cp.values.tolist(); Cp = str(Cp)[3:-3];
##Yr=Yr.values.tolist(); Yr = str(Yr)[3:-3];
##GN=GN.values.tolist(); GN = str(GN)[3:-3];
import textwrap
    
from PIL import Image, ImageDraw, ImageFont , ImageFilter , ImageOps

width = 1748
height = 2480
font = ImageFont.truetype("BERNHC.ttf", size=60)
font1 = ImageFont.truetype("BERNHC.ttf", size=60)
font2 = ImageFont.truetype("BOOKOSBI.ttf", size=40)
font3 = ImageFont.truetype("BOOKOSI.ttf", size=35)
font4 = ImageFont.truetype("HARLOWSI.ttf", size=100)
font5 = ImageFont.truetype("sylfaen.ttf", size=50)
font6 = ImageFont.truetype("BERNHC.ttf", size=60)
font7 = ImageFont.truetype("BOOKOSI.ttf", size=50)
font8 = ImageFont.truetype("VIVALDII.ttf", size=80)



##with open('Data.csv', 'r') as f:
##    reader = csv.reader(f)
##    i = 0
for i in range(len(data.index)):
    #i += 1
    ##convert the single row into values separate by comma bcoz of csv file
    j=random.randint(0,10)
    colors1=colorcombo(j)
    ##colors forheader, the management, date,time,venue,department,designations
    color1=colors1[0]
    ##colors for invitation,title,organised by,chiefguest,presided by
    color2=colors1[1]
    ##colors for guest name , principal sir
    color3=colors1[2]
    ##colors for border , line
    #color4=(204,0,204)
    ##Color for background
    color5=colors1[3]
    ToE=(data.loc[[i],['Type of Event']])
    ET=(data.loc[[i],['Event Title']])
    M=(data.loc[[i],['Month']])
    Da=(data.loc[[i],['Date']])
    T=(data.loc[[i],['Time']])
    
    ap=(data.loc[[i],['am/pm']])
    Day=(data.loc[[i],['Day']])
    V=(data.loc[[i],['venue']])
    Ob=(data.loc[[i],['Organized by']])
    GN=(data.loc[[i],['Guest Name']])
    D=(data.loc[[i],['Designation']])
    Dp=(data.loc[[i],['Department']])
    In=(data.loc[[i],['Institution']])
    Cp=(data.loc[[i],['City withpincode']])
    Yr=(data.loc[[i],['Year']])
    ToE=ToE.values.tolist(); ToE = str(ToE)[3:-3];
    ET=ET.values.tolist(); ET = str(ET)[3:-3];
    M=M.values.tolist(); M = str(M)[3:-3];
    T=T.values.tolist(); T = str(T)[3:-4];
    print(T)
    ap=ap.values.tolist(); ap = str(ap)[3:-3];
    V=V.values.tolist(); V = str(V)[3:-3];
    Ob=Ob.values.tolist(); Ob = str(Ob)[3:-3];
    D=D.values.tolist(); D = str(D)[3:-3];
    Dp=Dp.values.tolist(); Dp = str(Dp)[3:-3];
    In=In.values.tolist(); In = str(In)[3:-3];
    Cp=Cp.values.tolist(); Cp = str(Cp)[3:-3];
    Yr=Yr.values.tolist(); Yr = str(Yr)[3:-3];
    GN=GN.values.tolist(); GN = str(GN)[3:-3];
    Da=Da.values.tolist(); Da = str(Da)[3:-3];
    Day=Day.values.tolist(); Day = str(Day)[3:-3];

    ##colors for border , line
    color4=rand_color()
    # create a background 
    img = Image.new('RGB', (width, height), color= color5)
    # Convert image to RGBA
    img = img.convert("RGBA")
    # choose the first image snr logo
    im2= Image.open('snr.png')
    # Convert image to RGBA
    im2 = im2.convert("RGBA")
    img.paste(im2, (100, 100), im2)
    img.save('out.png', quality=100)
    img= Image.open('out.png')
    # choose the second image srit logo
     # Convert image to RGBA
    img = img.convert("RGBA")
    # choose the second image srit logo
    im2= Image.open('srit.png')
    # Convert image to RGBA
    im2 = im2.convert("RGBA")
    img.paste(im2, (1400, 110), im2)
    img.save('out.png', quality=100)
    img= Image.open('out.png')
    #invitation border
    border_val=20;
    img = ImageOps.expand(img, border_val, fill=color4)
    imgDraw = ImageDraw.Draw(img)
    #header
    offset=100
    imgDraw.text((alignhorizontalcenter("SRI RAMAKRISHNA INSTITUTE OF TECHNOLOGY",font), offset), "SRI RAMAKRISHNA INSTITUTE OF TECHNOLOGY", font=font, fill=color1,stroke_width=1, stroke_fill=(255, 255, 255))
    offset += font.getsize("SRI RAMAKRISHNA INSTITUTE OF TECHNOLOGY")[1]
    #imgDraw.text((alignhorizontalcenter("INSTITUTE OF TECHNOLOGY",font1), 250), "INSTITUTE OF TECHNOLOGY", font=font1, fill=(0, 0, 0))
    imgDraw.text((alignhorizontalcenter("An Autonomous Institution",font2), offset), "An Autonomous Institution", font=font2, fill=(0, 0, 0),stroke_width=1, stroke_fill=(255, 255, 255))
    offset += font.getsize("An Autonomous Institution")[1]
    imgDraw.text((alignhorizontalcenter("Educational Service: M/s SNR Sons Charitable Trust",font3), offset), "Educational Service: M/s SNR Sons Charitable Trust", font=font3, fill=(0, 0, 0),stroke_width=1, stroke_fill=(255, 255, 255))
    offset += font.getsize("Educational Service: M/s SNR Sons Charitable Trust")[1]
    imgDraw.text((alignhorizontalcenter("Accrediated by NAAC with 'A' Grade",font3), offset), "Accrediated by NAAC with 'A' Grade", font=font3, fill=(0, 0, 0),stroke_width=1, stroke_fill=(255, 255, 255))
    offset += font.getsize("Accrediated by NAAC with 'A' Grade")[1]
    imgDraw.text((alignhorizontalcenter("Approved by AICTE and Affiliated to Anna University, Chennai",font3), offset), "Approved by AICTE and Affiliated to Anna University, Chennai", font=font3, fill=(0, 0, 0),stroke_width=1, stroke_fill=(255, 255, 255))
    offset += font.getsize("Approved by AICTE and Affiliated to Anna University, Chennai")[1]
    imgDraw.text((alignhorizontalcenter("Pachapalayam,Perur Chettipalayam,Coimbatore-641010",font3), offset), "Pachapalayam,Perur Chettipalayam,Coimbatore-641010", font=font3, fill=(0, 0, 0),stroke_width=1, stroke_fill=(255, 255, 255))
    offset += font.getsize("Pachapalayam,Perur Chettipalayam,Coimbatore-641010")[1]
    imgDraw.text((alignhorizontalcenter("Invitation",font4), offset), "Invitation", font=font4, fill=(color2))
    offset += font.getsize("Invitation")[1]
    offset += 50
    imgDraw.line((50,offset, 1750, offset), fill=color4, width=10)
    offset += 80
    
    imgDraw.text((alignhorizontalcenter("The Management,Principal,Staff & Students", font=font5),offset), "The Management,Principal,Staff & Students", fill=color1, font=font5, anchor='lm')
    offset += font.getsize("The Management,Principal,Staff & Students")[1]
    imgDraw.text((alignhorizontalcenter("Cordially invite you for the", font=font5),offset), "Cordially invite you for the", fill=(color1), font=font5, anchor='lm')
    offset += font.getsize("Cordially invite you for the")[1]
    imgDraw.text((alignhorizontalcenter(ToE, font=font5),offset), ToE, fill=(color1), font=font5, anchor='lm')
    #input type of event
    offset += font.getsize(ToE)[1]
    # input title of the event      
    text= ET
    for line in textwrap.wrap(text, width=80):
        margin=alignhorizontalcenter(line, font=font6)
        imgDraw.text((margin, offset), line, font=font6, fill=color2)
        offset += font.getsize(line)[1]

    offset += 40
    #input month date year day time place
    tex= "On "+str(M)+" "+ str(Da)+", "+str(Yr)+ " ("+str(Day)+") at "+ str(T)+" "+ str(ap) +" "+"in "+str(V)
    imgDraw.text((alignhorizontalcenter("On November 02,2022 (Wednesday) at 9.30 am in Seminar Hall II",font=font5), offset), tex, font=font5, fill=(color1))
    offset += font.getsize("On November 02,2022 (Wednesday) at 9.30 am in Seminar Hall II")[1]
    #input organized by
    imgDraw.text((alignhorizontalcenter("Organized by",font6), offset), "Organized by", font=font6, fill=(color2))
    offset += font.getsize("Organized by")[1]
     #input organized by
    # input title of the event      
    text= Ob
    for line in textwrap.wrap(text, width=80):
        margin=alignhorizontalcenter(line, font=font7)
        imgDraw.text((margin, offset), line, font=font7, fill=color1)
        offset += font.getsize(line)[1]

    offset += font.getsize("Department of Electronics and Communication Engineering")[1]
    imgDraw.line((50,offset, 1750, offset), fill=color4, width=10)
    offset += 60
    #offset += font.getsize("Cordially invite you for the")[1]
    imgDraw.text((alignhorizontalcenter("Chief Guest", font=font8),offset), "Chief Guest", fill=(color2), font=font8, anchor='lm')
    offset += font.getsize("Chief Guest")[1]
    #input chief guest name
    imgDraw.text((alignhorizontalcenter(GN,font6), offset), GN, font=font6, fill=(color3))
    offset += font.getsize(GN)[1]
    #input chief guest designation
    imgDraw.text((alignhorizontalcenter(D,font7), offset), D, font=font7, fill=(color1))
    offset += font.getsize(D)[1]
    #input chief guest department
    imgDraw.text((alignhorizontalcenter(Dp,font7), offset), Dp, font=font7, fill=(color1))
    offset += font.getsize(Dp)[1]
    #input chief guest institution
    imgDraw.text((alignhorizontalcenter(In,font7), offset), In, font=font7, fill=(color1))
    offset += font.getsize(In)[1]
    #input chief guest District
    imgDraw.text((alignhorizontalcenter(Cp,font7), offset), Cp, font=font7, fill=(color1))
    offset += font.getsize(Cp)[1]




    #presided by
    offset += 60
    
    imgDraw.text((alignhorizontalcenter("presided by", font=font8),offset), "presided by", fill=(color2), font=font8, anchor='lm')
    offset += font.getsize("presided by")[1]
          
    imgDraw.text((alignhorizontalcenter("Dr.M.Paulraj",font6), offset), "Dr.M.Paulraj", font=font6, fill=(color3))
    offset += font.getsize("Dr.M.Paulraj")[1]
    imgDraw.text((alignhorizontalcenter("Principal,",font7), offset), "Principal,", font=font7, fill=(color1))
    offset += font.getsize("Principal")[1]
    imgDraw.text((alignhorizontalcenter("Sri Ramakrishna Institute of Technology,",font7), offset), "Sri Ramakrishna Institute of Technology,", font=font7, fill=(color1))
    offset += font.getsize("Sri Ramakrishna Institute of Technology,")[1]
    imgDraw.text((alignhorizontalcenter("Coimbatore - 641010",font7), offset), "Coimbatore - 641010", font=font7, fill=(color1))
    offset += font.getsize("Coimbatore - 641010")[1]
    offset += 80
    imgDraw.line((0,offset, 2480, offset), fill=color4, width=20)
    offset += 15

    #offset += font.getsize("Department of Electronics and Communication Engineering")[1]
    #imgDraw.text((alignhorizontalcenter( ToE[1],font7), offset),  ToE, font=font7, fill=(color1))
    img=img.crop((0, 0, width+border_val+20, offset))
    
           
    img.save(f'E:/2022-23_Odd/NAAC WORK/events/generated/result{i}.png')


