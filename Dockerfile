FROM piptools:latest

ENV PYHTONUNBUFFERED=1
RUN apt-get update \
  && apt-get -y install tesseract-ocr \
  && apt-get -y install tesseract-ocr-fra
  #&& apt-get -y install ffmpeg libsm6 libxext6 

ADD requirements.txt ./
RUN pip install -r requirements.txt

ENV PYTHONPATH="/home"
