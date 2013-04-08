import urllib
import csv

from utilities import skipLines


class Spider:

  def __init__(self,**kwargs):
    for item in kwargs.items():
      setattr(self,item[0],item[1])
    
  def generateUrl(self,**kwargs):
    if 'timestamp' in kwargs: 
      self.timestamp = kwargs['timestamp']
    self.current_url = self.timestamp.strftime(self.url_format)

  def createCsvUrl(self,**kwargs):
    #passed from retrieveCsvUrl after self.url_sequence has been populated
    if 'current_url' in kwargs:
      self.current_url = kwargs['current_url']
    #used for test createCsvUrl without testing generateUrlSequence
    else:
      self.generateUrl()
    #open url using standard urllib urlopen method
    self.file_path = 'data/' + self.current_url.split('/').pop()
    import os.path
    if os.path.isfile(self.file_path) == False:
      self.saved_file = urllib.urlretrieve(self.current_url,self.file_path)
      #skip n lines into the file
    self.url_file = open(self.file_path)
    skipLines(self.url_file,self.strip_lines)
    #read file as csv

    self.csv_file = csv.DictReader(self.url_file,delimiter=',')

    
  def processLiveCsv(self):
    for line in self.csv_file:
      if self.end_keyword not in line.values():
        self.current_line = line
        self.generateInsert()
        self.connection.execute(self.insert_string)
    self.url_file.close()
  def retrieveCsvFromUrlSequence(self):
    for current_url in self.url_sequence:
       self.createCsvUrl(current_url=current_url)
       assert self.expected_fieldnames == self.csv_file.fieldnames
       self.processLiveCsv()

  def generateUrlSequence(self):
    self.url_sequence = []
    while self.current_datetime < self.end_datetime:
      current_url = self.generateUrl(timestamp=self.current_datetime)
      self.current_datetime += self.datetime_step
      self.url_sequence.append(self.current_url)
  
  def run(self):
    self.generateUrlSequence()
    self.retrieveCsvFromUrlSequence()

  def generateInsert(self):
    self.insert_string = str(self.insert_string_format)%(self.current_line)
