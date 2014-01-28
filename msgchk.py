import urllib, json, re, Thermal_Formatter

sky = json.loads(urllib.urlopen('http://sky.madebycm.no:5555/lookup').read())

try:
  sky['none']
  print 'I got nothing'
except:
  t = Thermal_Formatter.Thermal_Formatter()
  msg = sky['msg'].split("\n")
  msglist = []

  print 'New message! (1)'

  for line in msg:
    line = re.sub(' +', ' ' , line)
    msglist.append(['s', line])

  msg = [
      ['l', 'New message! (1)']
    , msglist
  ]
  
  msglist.insert(0, ['l', 'New message! (1)'])
  t.processAndPrint(msglist)