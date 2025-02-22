FROM pytorch/pytorch:2.6.0-cuda12.4-cudnn9-runtime
LABEL authors="JSK Robotics Laboratory, The University of Tokyo"

ADD . /app

WORKDIR /app

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["python3", "audio_identification_service.py"]