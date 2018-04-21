import sqlite3

import datetime

conn = sqlite3.connect("dicedb")

cursor = conn.cursor()


#Create jobs table

cursor.execute("CREATE TABLE dice_jobs(Id,job_title,job_desc,job_url,employment_type,location,skills,date_posted,vendor_name,vendor_url)")

values={u'qualifications': None, u'educationRequirements': u'IT Diploma/Degree/Certification', 'link': u'/jobs/detail/Direct-Customer-%26%2345Big-Data-Engineer-with-Scala%26%2347AWS-exp%26%2345-Hot-position-Accion-Labs-Nashville-TN-37201/10428868/HA%26%2345103328?icid=sr1-1p&q=data+engineer&l=Nashville,tn', u'validThrough': None, u'baseSalary': None, u'workHours': None, u'experienceRequirements': None, 'title': u'Direct Customer -Big Data Engineer with Scala/AWS exp- Hot position', u'employmentType': u'contract', u'industry': u'IT Software', 'short_desc': u'Direct Customer -Big Data Engineer...', 'date_posted': u'2017-11-09T15:34:11Z', u'skills': u'Spark, Scala, REST, AWS', u'responsibilities': None, 'location': u'Nashville, TN', 'vendor_name': u'Accion Labs', 'vendor_url': u'/company/10428868'}



sql = '''INSERT INTO dice_jobs(id,
                               job_title,
                               job_desc,
                               job_url,
                               employment_type,
                               location,
                               skills,
                               date_posted,
                               vendor_name,
                               vendor_url)

                    values(?,?,?,?,?,?,?,?,?,?);

                                '''

cursor.execute(sql,(datetime.datetime.now().strftime("%Y%m%d%s%f"),values['title'],values['short_desc'],values['link'],\
                                                                          values['employmentType'],\
                                                                          values['location'],\
                                                                          values['skills'],\
                                                                          values['date_posted'],\
                                                                          values['vendor_name'],\
                                                                          values['vendor_url']\
                                                                          ))

#cursor.execute("INSERT INTO dice_jobs values(id='201711121510517777055508',job_title=u'Direct Customer -Big Data Engineer with Scala/AWS exp- Hot position',job_desc=u'Direct Customer -Big Data Engineer...',job_url=u'/jobs/detail/Direct-Customer-%26%2345Big-Data-Engineer-with-Scala%26%2347AWS-exp%26%2345-Hot-position-Accion-Labs-Nashville-TN-37201/10428868/HA%26%2345103328?icid=sr1-1p&q=data+engineer&l=Nashville,tn',employment_type=u'contract',location=u'Nashville, TN',skills=u'Spark, Scala, REST, AWS',date_posted=u'2017-11-09T15:34:11Z',vendor_name=u'Accion Labs',vendor_url=u'/company/10428868')")


#
# sql = '''INSERT INTO dice_jobs(id,job_title) values(?,?);'''
#
# cursor.execute(sql,("201711121510517777055508",u'Direct Customer -Big Data Engineer with Scala/AWS exp- Hot position'))
#
# sql ='''DELETE FROM TABLE dice_jobs'''

conn.commit()