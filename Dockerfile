FROM python
COPY /api/. /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
STOPSIGNAL SIGINT
ENTRYPOINT ["python3"]
CMD ["api.py"]