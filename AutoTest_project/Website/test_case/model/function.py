from  selenium import  webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def insert_img(driver,filename):
    fun_path=os.path.dirname(__file__)
    # print(fun_path)

    base_dir=os.path.dirname(fun_path)
    # print(base_dir)

    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')
    # print(base_dir)

    base=base_dir.split('/Website')[0]
    # print(base)

    filepath=base+'/Website/test_report/screenshot/'+filename
    driver.get_screenshot_as_file(filepath)

def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver = 'smtp.qq.com'

    user = '591569065@qq.com'
    password = 'glsslqraigjnbfjg'

    sender = '591569065@qq.com'
    receives = ['lgdnhaonan@sina.com', '3001867527@qq.com']

    subject = 'Web Selenium 自动化测试报告'
    # content = '<html><h1 style="color:red">我要自学网，自学成才！</h1></html>'

    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print("Start send email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send email end!")

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    print("the latest report is " + lists[-1])

    file = os.path.join(report_dir, lists[-1])-
    print(file)
    return file


if __name__=='__main__':
    # insert_img()
    driver=webdriver.Chrome()
    driver.get("http://www.sogou.com")
    insert_img(driver,'sougou.jpg')
    driver.quit()
