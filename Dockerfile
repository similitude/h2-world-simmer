FROM similitude/h2-world-docker

MAINTAINER Oliver Lade <oliver@similitude.org>
# See https://groups.google.com/d/topic/h2-database/ZXOCLxNJ2kI/discussion

ENV H2_HOME /opt/h2
ENV H2_DATA /opt/h2-data

ADD /api /api

