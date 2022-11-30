
def hande_uploaded_file(f):
    with open('./uploads/Car_SAMPLE.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)