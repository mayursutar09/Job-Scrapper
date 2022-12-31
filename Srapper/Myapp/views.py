from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import json

# Create your views here.
def Indexview(request):
    url ="https://www.naukri.com/jobapi/v3/search?noOfResults=20&location=pune&searchType=adv_1&urlType=search_by_location&k=&l=pune&sort=r&seoKey=jobs-in-pune&src=seo_srp&clusters=wfhType,citiesGid,experience,topCompanyId,industryTypeGid,salaryRange,freshness,roleGid,employement,functionalAreaGid,ugCourseGid,jobType,sortBy"
    formData={"noOfResults": 30,
    "location": "pune",
    "searchType": "adv_1",
    "urlType": "search_by_location",
    "k": "",
    "l": "pune",
    "sort": "r",
    "seoKey": "jobs-in-pune",
    "src": "seo_srp",
    "clusters": "wfhType,citiesGid,experience,topCompanyId,industryTypeGid,salaryRange,freshness,roleGid,employement,functionalAreaGid,ugCourseGid,jobType,sortBy"
    }
    UserHeader={"appid": "135",
    "systemid": "135",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"}
    r=requests.get(url,formData,headers=UserHeader)
    # print(r)
    htmlContent= r.content
    # print(htmlContent)
    soup=BeautifulSoup(htmlContent,'html.parser')
    site_json=json.loads(soup.text)
    data=[]
    for job in site_json["jobDetails"]:
        experience = job["placeholders"][0]
        salary = job["placeholders"][1]
        location = job["placeholders"][2]
        skills=job["keySkills"]
        URL=job['staticUrl']
        # print(f"title - {job['title']}\nexperience - {experience['label']}\n location - {location['label']}\n salary - {salary['label']}")
        data.append({'title':job['title'],'experience':experience['label'],'location':location['label'],'salary':salary['label'],'skills':skills,'URL':URL})
    # print([d.get('salaryRange') for d in site_json['clusters'] if d.get('salaryRange')])

    return render(request,'index.html',{'data':data})