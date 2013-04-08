import nose 
from nose.plugins.attrib import attr
#configure django settings to get selenose cases to work... WHY DO I HAVE TO DO THIS?
#configure the default django settings
from spider import *
from unittest import TestCase
import datetime
from dateutil.relativedelta import relativedelta
from connection import connection
####################################
##DEFINE DEFAULTS
##
#define url format
url_format = 'http://www.pjm.com/pub/account/dasrpjm/%Y%m.csv'
##
#define sample_date_data
sample_date = datetime.datetime(2013,3,1) # datetime on march 1 2013
#start capture at august 1st 2008
current_date = datetime.datetime(2008,8,1)
date_step = relativedelta(months=+1)
#Define End Key Word
end_keyword = 'End of Report'

##EXPECTED DATA
expected_url_sequence =   ['http://www.pjm.com/pub/account/dasrpjm/200808.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200809.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200810.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200811.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200812.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200901.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200902.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200903.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200904.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200905.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200906.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200907.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200908.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200909.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200910.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200911.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/200912.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201001.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201002.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201003.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201004.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201005.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201006.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201007.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201008.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201009.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201010.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201011.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201012.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201101.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201102.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201103.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201104.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201105.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201106.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201107.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201108.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201109.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201110.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201111.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201112.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201201.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201202.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201203.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201204.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201205.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201206.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201207.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201208.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201209.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201210.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201211.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201212.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201301.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201302.csv',
                           'http://www.pjm.com/pub/account/dasrpjm/201303.csv'
                          ]  
#define expected field names
expected_fieldnames = ['EPT Hour Ending', 
                           'GMT Hour Ending', 
                           'DASRMCP ($/MWh)', 
                           'Total PJM RT Load (MWh)', 
                           'Total PJM Cleared DASR MWh', 
                           'Total PJM DASR Credits ($)', 
                           'Total PJM Adjusted DASR Obligation (MWh)'
                           ]

insert_string_format = ''' INSERT INTO prices    (   
                                                         ept_hour_ending,
                                                         gmt_hour_ending,
                                                         dasrmcp_usd_per_mwh,
                                                         total_pjm_rt_load_mwh,
                                                         total_pjm_cleared_dasr_mwh,
                                                         total_pjm_dasr_credits_usd,
                                                         total_pjm_adjusted_dasr_obligation_mwh
                                                       )
                                  VALUES               (
                                                         '%(EPT Hour Ending)s:00:00',
                                                         '%(GMT Hour Ending)s:00:00', 
                                                         '%(DASRMCP ($/MWh))s', 
                                                         '%(Total PJM RT Load (MWh))s', 
                                                         '%(Total PJM Cleared DASR MWh)s', 
                                                         '%(Total PJM DASR Credits ($))s', 
                                                         '%(Total PJM Adjusted DASR Obligation (MWh))s'
                                                       );
                           ''' 


test_line_dict =      {'EPT Hour Ending'                               :                                  '03/01/2013 01', 
                        'Total PJM RT Load (MWh)'                       :                                  '81735.110000' , 
                        'GMT Hour Ending'                               :                                  '03/01/2013 06', 
                        'Total PJM DASR Credits ($)'                    :                                            '.00', 
                        'Total PJM Adjusted DASR Obligation (MWh)'      :                                       '6069.600', 
                        'Total PJM Cleared DASR MWh'                    :                                       '6069.600', 
                        'DASRMCP ($/MWh)'                               :                                            '.000'
                       }   


#define expected insert statement
expected_insert  =   ''' INSERT INTO prices    (   
                                                         ept_hour_ending,
                                                         gmt_hour_ending,
                                                         dasrmcp_usd_per_mwh,
                                                         total_pjm_rt_load_mwh,
                                                         total_pjm_cleared_dasr_mwh,
                                                         total_pjm_dasr_credits_usd,
                                                         total_pjm_adjusted_dasr_obligation_mwh
                                                       )
                                  VALUES               (
                                                         '03/01/2013 01:00:00',
                                                         '03/01/2013 06:00:00', 
                                                         '.000', 
                                                         '81735.110000', 
                                                         '6069.600', 
                                                         '.00', 
                                                         '6069.600'
                                                       );

                     '''
########################################



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
                                  strip_lines=2,
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

    #define expected result
    expected_result = 'http://www.pjm.com/pub/account/dasrpjm/201303.csv'
   
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
