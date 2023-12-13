from datetime import datetime

def convert_to_datetime(date_string):
    try:
        # Define the format of the date string
        date_format = "%B, %d %Y %H:%M:%S"
        
        # Parse the date string using the defined format
        datetime_object = datetime.strptime(date_string, date_format)
        
        return datetime_object
    except ValueError as e:
        # Handle the case where the date string doesn't match the specified format
        print(f"Error: {e}")
        return None

# Example usage:
date_string = "January, 20 2017 03:51:25"

jsondata = {
    "added": "January, 20 2017 03:51:25",
    "published": "January, 09 2017 00:00:00",
}
# converted_datetime = convert_to_datetime(date_string)
converted_datetime = convert_to_datetime(jsondata['published'])

if converted_datetime:
    print(f"Original string: {date_string}")
    print(f"Converted datetime: {converted_datetime}")
else:
    print("Conversion failed.")



'''
extra
def load_data(request):
    try:
        with open(jsonFilePath, 'r') as file:
            data = json.load(file)

            for item in data:
                # Convert date strings to datetime objects
                # item['added'] = datetime.strptime(item['added'], '%B, %d %Y %H:%M:%S')
                # item['published'] = datetime.strptime(item['published'], '%B, %d %Y %H:%M:%S')
                
                # print("Before added items :", item['added'])
                # item['added'] = convert_to_datetime(item['added'])
                # item['published'] = convert_to_datetime(item['published'])

                # "added": "January, 20 2017 03:51:25",
                # "published": "January, 09 2017 00:00:00",
                # print("items :", item , "\n\n")
                # print("After added items :", item['added'] , "\n\n")
                # print("items :", item['published'] , "\n\n")
                if item['intensity'] == "":
                    item['intensity'] = 0
                
                if item['likelihood'] == "":
                    item['likelihood'] = 0
                
                if item['relevance'] == "":
                    item['relevance'] = 0
                
                # Validate and create DashboardData instance
                try:
                    DashboardData.objects.create(**item)
                except ValidationError as e:
                    # Handle validation errors, if any
                    print(f"Validation error for item: {item}. Error: {e}")

        # return render(request, 'success.html', {'message': 'Data loaded successfully'})
        return HttpResponse(f'Message    | Data loaded successfully')
    
    except Exception as e:
        # Handle file read or other exceptions
        # return render(request, 'error.html', {'error_message': str(e)})
        return HttpResponse(f'error_message    | {str(e)}')


'''