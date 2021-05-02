FROM python:3.6-slim-buster

RUN pip install scrapy
RUN pip install scrapy-fake-useragent
RUN pip install toripchanger
RUN pip install requests
RUN pip install stem
RUN pip install apscheduler

 
ADD . .
WORKDIR "/app"

#Test 
CMD ["python3", "/tests/ipchanger_works.py" ]
#Running crawler
#CMD ["python3", "/go_spider.py" ]