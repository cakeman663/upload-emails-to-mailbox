import re
import smtplib
import time
import email.parser
from os import listdir
from os.path import isfile, join

class Counter:
  def __init__(self, count):
    self.__count = count
    self.__counter = 1

  def get(self):
    print(str(self.__counter) + '\\' + str(self.__count))
    self.__counter += 1


mailbox = 'example@example.pro'
path = '/path/to/dir/with/emails/'

mails = [f for f in listdir(path) if isfile(join(path, f))]

counter = Counter(len(mails))
parser = email.parser.Parser()

for mail in mails:
  counter.get()
  try:
    with open(path + mail, 'r', encoding='utf8', errors = 'replace') as f:
      rawMail = f.read()

    msg = parser.parsestr(rawMail)
    headers = msg._headers.copy()

    notRemove = ['from', 'reply-to', 'content-type', 'content-transfer-encoding', 'date', 'subject', 'mime-version']
    for header in headers:
      if header[0].lower() not in notRemove:
        while header in msg._headers:
          msg._headers.remove(header)

    msg['To'] = mailbox
		
    #headerFrom = msg['From']
    #headerFrom = re.search('<(.*?)>', headerFrom)
    #headerFrom = headerFrom.group(1) if headerFrom else mailbox
    #msg.replace_header('From', headerFrom)

    s = smtplib.SMTP('localhost')
    s.sendmail(msg['From'], msg['To'], str(msg).encode('utf8'))

    time.sleep(0.05)
  except Exception as e:
    print(e)
    with open('not_loaded.log', 'a') as f:
      f.write(mail)
      f.write('\n')