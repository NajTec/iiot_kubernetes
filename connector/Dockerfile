FROM gcr.io/triggermesh/knative-lambda-python37
ENV _HANDLER handler.endpoint
COPY . .
RUN if [ -f requirements.txt ]; then pip3.7 install -r requirements.txt ;fi
RUN pip3.7 install requests
ENTRYPOINT ["/opt/aws-custom-runtime"]
