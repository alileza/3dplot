FROM czentye/matplotlib-minimal:3.1.2

COPY . /app

ENTRYPOINT [ "python3" ]
CMD ["/app/main.py"]