import nose 
from nose.plugins.attrib import attr
#configure django settings to get selenose cases to work... WHY DO I HAVE TO DO THIS?
#configure the default django settings
from spider.spider import Spider
from spider.connections import connection
from unittest import TestCase
from config import *



class TestUnits(TestCase):
  def setUp(self):

    ####
    ###

    #end capture one month from today
    end_date = datetime.datetime.now() - date_step
    ##

    #define insert string format

    #Create Spider Instance with appropriate inputs
    self.expected_url_sequence = expected_url_sequence
    current_connection = connection()
    self.spider_instance = Spider(url_format=url_format,
                                  timestamp=sample_date,
                                  strip_lines=strip_lines,
                                  insert_string_format=insert_string_format,
                                  current_datetime = current_date,
                                  datetime_step = date_step,
                                  end_datetime = end_date,
                                  url_sequence = expected_url_sequence,
                                  expected_fieldnames = expected_fieldnames,
                                  end_keyword = end_keyword,
                                  connection=current_connection
                                 )
  def testGenerateUrl(self):
    '''
    Sample URL is: http://www.pjm.com/pub/account/dasrpjm/201303.csv

    Therefor url_format should be 'http://www.pjm.com/pub/account/dasrpjm/%Y%m.csv'
    '''        


   
    #test function
    self.spider_instance.generateUrl()
    
    #retrieve sample url
    sample_url = self.spider_instance.current_url
    
    #Test Assertion
    self.assertEquals(expected_result,sample_url)

  def testCreateCsvUrl(self):

    #execute readCsvUrl and initialize csv file object
    self.spider_instance.createCsvUrl()

    #retrieve actual field names
    result_fieldnames = self.spider_instance.csv_file.fieldnames     
    

    #test assertion
    self.assertEquals(result_fieldnames,self.spider_instance.expected_fieldnames)

  
  def testGenerateInsert(self):

   
      self.spider_instance.current_line =  test_line_dict

      self.spider_instance.generateInsert()

      #test assertion
      self.assertEquals(expected_insert,self.spider_instance.insert_string)
      self.spider_instance.connection.rollBack()
  def testProcessLiveCsv(self):
    self.spider_instance.createCsvUrl()
    self.spider_instance.processLiveCsv()

  def testGenerateUrlSequence(self):
    self.spider_instance.generateUrlSequence()
    self.assertEquals(self.expected_url_sequence,self.spider_instance.url_sequence)

  def testRetrieveCsvFromUrlSeqeuenc(self):
    self.spider_instance.retrieveCsvFromUrlSequence()
    self.spider_instance.connection.closeAndSave()



if __name__ == '__main__':
    nose.main()
