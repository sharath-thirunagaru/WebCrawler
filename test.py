import sqlite3

conn = sqlite3.connect('dicedb')

cursor = conn.cursor()


#cursor.execute("CREATE TABLE dice_jobs_staging(Id,job_title,job_desc,job_url,employment_type,location,skills,date_posted,vendor_name,vendor_url)")

results=cursor.execute("select * from dice_jobs")

for row in results.fetchall():
    print row
#
# # cursor.execute("delete from dice_jobs")
# #
# # conn.commit()