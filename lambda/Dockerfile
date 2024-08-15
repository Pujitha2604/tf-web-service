# Use the AWS Lambda Python runtime base image
FROM public.ecr.aws/lambda/python:3.9

# Copy the function code
COPY server.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (in the format file.handler)
CMD ["server.handler"]
