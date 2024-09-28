
FROM python:3.8-slim

WORKDIR /action

COPY check_hardcoded_ip.py /action/check_hardcoded_ip.py

CMD ["python", "/action/check_hardcoded_ip.py"]
