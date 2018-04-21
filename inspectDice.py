from bs4 import BeautifulSoup
import urllib
import sys
import getopt
import sqlite3
import datetime


def construct_url(base_url,**filters):
    '''

    :param base_url:starting on which filters will be constructed
    :param filters: key word arguments with filters that should be applied for retrieval
                    available key words are job(job title),location(location based search)
    :return: filtered url that will be used with urllib to extract the html
    '''

    if filters.get('job',0)!=0:
        job=filters['job']
    if filters.get('location',0)!=0:
        location=filters['location']

    queried_job="+".join(job.split())
    processed_location=location.split(",")
    filtered_url =base_url+queried_job+"&l="+processed_location[0]+"%2C"+processed_location[1]

    return filtered_url

def parse_url_section(url_section):
    return {'title':url_section.a['title'],"link":url_section.a["href"]}

def parse_short_desc_section(short_desc_section):
    return{"short_desc":short_desc_section.span.string}

def parse_details_section(details_section):
    try:

        dtls={}
        employer_dtls_span=details_section.find_all("li",recursive=False)[0].find_all("span")[1]

        dtls['vendor_name']=employer_dtls_span['title']
        dtls['vendor_url']=employer_dtls_span.a['href']
        dtls['location']=details_section.find_all("li",recursive=False)[1]['title']
        dtls['date_posted']=details_section.find_all("li",recursive=False)[2].find_all("span")[1].string
        sub_details_section = details_section.find_all("li",recursive=False)[4]

        for span in sub_details_section.find_all("span",recursive=False):
            dtls[span['itemprop']]=span.string

        return dtls
    except:
        return dtls




def parse_items(search_results_div):
    """

    :param search_results_div: html div container that has the search results
    :return: details row
    """

    jobs_list=[]

    for o_div in search_results_div.find_all("div",recursive=False):

        contents_div=o_div.find("div")

        logo_section=contents_div.find("div")
        url_section=contents_div.find_all("ul")[0]
        short_desc_section=contents_div.find("li")
        details_section=contents_div.find_all("ul")[1]

        job_record={}

        url_rec=parse_url_section(url_section)
        short_desc_rec=parse_short_desc_section(short_desc_section)
        details_rec=parse_details_section(details_section)

        job_record.update(url_rec)
        job_record.update(short_desc_rec)
        job_record.update(details_rec)

        jobs_list.append(job_record)

    return jobs_list

def persist_jobs(jobs_list):

    jobs_list_reduced_cols=[]

    for row_dict in jobs_list:
        jobs_list_reduced_cols.append((datetime.datetime.now().strftime("%Y%m%d%s%f"),row_dict.get('title',""),row_dict.get('short_desc',""),row_dict.get('link',""),\
                                                                          row_dict.get('employmentType',""),\
                                                                          row_dict.get('location',""),\
                                                                          row_dict.get('skills',""),\
                                                                          row_dict.get('date_posted',""),\
                                                                          row_dict.get('vendor_name',""),\
                                                                          row_dict.get('vendor_url',"")\
                                        ))


    conn = sqlite3.connect("dicedb")

    cursor = conn.cursor()


    insert_sql = sql = '''INSERT INTO dice_jobs(id,
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

    cursor.executemany(insert_sql,jobs_list_reduced_cols)

    conn.commit()



def next_page(url):
    pass



def main(job,location):


    q_url = construct_url("https://www.dice.com/jobs?q=",job=job,location=location)

    print q_url

    # while True:
    #
    #     try:
    #
    #         html_data = urllib.urlopen(q_url).read()
    #
    #         soup = BeautifulSoup(html_data,"html5lib")
    #
    #         search_results_div = soup.find_all("div",id="serp")[0]
    #
    #         jobs_list=parse_items(search_results_div)
    #
    #         persist_jobs(jobs_list)
    #
    #         q_url=next_page(q_url)
    #     except:
    #         break





if __name__=="__main__":
    main('data engineer','nashville,tn')










