FROM python
EXPOSE 5000
COPY /api/. /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["api.py"]