# Docker for a postgresql image 

FROM postgres:alpine

ENV POSTGRES_PASSWORD=#Caliente2512
ENV DIRPATH=/content_metrics
WORKDIR ${DIRPATH}
COPY ./youtube_channel_stats.sql .
COPY create_table.sh .
EXPOSE 5432
