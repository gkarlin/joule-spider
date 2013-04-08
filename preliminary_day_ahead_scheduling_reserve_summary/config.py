################## START IMPORTS
#################
################
import datetime
from dateutil.relativedelta import relativedelta
################
#################
##################
####################################
##DEFINE DEFAULTS
##
#define url format
url_format = 'http://www.pjm.com/pub/account/dasrpjm/%Y%m.csv'
##
#define sample_date_data 
# example = datetime.datetime(YYYY,M,D)
sample_date = datetime.datetime(2013,3,1) # datetime on march 1 2013
#start capture at august 1st 2008
current_date = datetime.datetime(2008,8,1)
#define url date step
date_step = relativedelta(months=+1)
#Define number of lines from head to strip
strip_lines = 2
#Define End Key Word
end_keyword = 'End of Report'
#define expected header names
expected_fieldnames =     ['EPT Hour Ending', 
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


test_line_dict =      { 'EPT Hour Ending'                               :                                  '03/01/2013 01', 
                        'Total PJM RT Load (MWh)'                       :                                  '81735.110000' , 
                        'GMT Hour Ending'                               :                                  '03/01/2013 06', 
                        'Total PJM DASR Credits ($)'                    :                                            '.00', 
                        'Total PJM Adjusted DASR Obligation (MWh)'      :                                       '6069.600', 
                        'Total PJM Cleared DASR MWh'                    :                                       '6069.600', 
                        'DASRMCP ($/MWh)'                               :                                            '.000'
                       }   


#define expected insert statement
expected_insert  =     ''' INSERT INTO prices    (   
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
#define expected result
expected_result = 'http://www.pjm.com/pub/account/dasrpjm/201303.csv'
########################################

