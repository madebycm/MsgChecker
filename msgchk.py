import urllib, json, subprocess, sys, Thermal_Formatter

sky = json.loads(urllib.urlopen('http://sky.madebycm.no:5555/lookup').read())

try:
  sky['none']
  print 'I got nothing'
except:
  print 'I got!'

  t = Thermal_Formatter.Thermal_Formatter()
  # create
  msg = [
      ['l', 'New message! (1)']
    , ['s', sky['msg']]
  ]
  t.processAndPrint(msg
    )