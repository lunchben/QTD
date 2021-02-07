import os
import re


xmldir = r'E:\VOC\Annotations'
savedir = r'E:\VOC\newXML'

xmllist = os.listdir(xmldir)

for xml in xmllist:
    if '.xml' in xml:
        fo = open(savedir+'/'+'{}'.format(xml), 'w')
    fi = open(xmldir+'/'+'{}'.format(xml), 'r')
    lines = fi.readlines()
    for line in lines:
        ref = re.findall('<name>(.*)</name>', line)
        len = ref.__len__()
        if len != 0:
            string = str(ref)
            realstr = string[2:-2]
            line = line.replace(realstr, 'QT')
            fo.write(line)
        else:
            fo.write(line)
    fo.close()
