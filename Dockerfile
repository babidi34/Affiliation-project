FROM babidi34/debian-pelican:latest

COPY pelicanconf.py /opt/site-pelican/
COPY articles/* /opt/site-pelican/content/
WORKDIR /opt/site-pelican
RUN pelican content
EXPOSE 8000

# Lancer Pelican
CMD ["sh", "-c", "pelican content && pelican -l ."]