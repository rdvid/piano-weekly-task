FROM ubuntu:22.04
RUN apt-get update  \
    && apt-get -y install curl tar
RUN curl -o lilypond.tar.gz https://gitlab.com/lilypond/lilypond/-/releases/v2.24.3/downloads/lilypond-2.24.3-linux-x86_64.tar.gz
RUN tar -xf lilypond.tar.gz
COPY requirements.txt .
RUN pip install --upgrade pip  \
    && install -r requirements.txt
COPY . .
WORKDIR /controller
ENTRYPOINT ["python", ".\test.py"]

# TODO: fix dockerfile config - issues w/ alpine apk installer
# curl path
# https://gitlab.com/lilypond/lilypond/-/releases/v2.24.3/downloads/lilypond-2.24.3-linux-x86_64.tar.gz