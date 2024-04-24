from .models import CameraData
from rest_framework.response import Response
from .serializer import CameraDataSerializer
from rest_framework.decorators import api_view
from datetime import datetime



@api_view(['GET'])
def cameraData(request):
    camera = CameraData.objects.all()
    serializer = CameraDataSerializer(camera, many=True)
    return Response(serializer.data)



def get_time_of_day(time_string):
    # Convert the time string to a datetime object
    hours, minutes = map(int, time_string.split(':'))
    current_date = datetime.now().replace(hour=hours, minute=minutes)

    # Get the current hours
    current_hours = current_date.hour

    # Check if it's night (after 19:00 and before 12:00)
    if current_hours >= 19 or current_hours < 12:
        return 'night'
    else:
        return 'day'


@api_view(['GET'])
def get_all_summary(request):
    data = CameraData.objects.all()
    cameras_summary_data = []

    for element in data.values('camera_id').distinct():
        filtered_ids = data.filter(camera_id=element['camera_id'])

        filter_day_event = filter_day_night_time(filtered_ids, "day")
        filter_night_event = filter_day_night_time(filtered_ids, "night")

        filter_person_events = filtered_ids.filter(specie_id="person")
        filter_person_day_event = filter_day_night_time(filter_person_events, "day")
        filter_person_night_event = filter_day_night_time(filter_person_events, "night")

        filter_animal_events = filtered_ids.filter(specie_id="animal")
        filter_animal_day_event = filter_day_night_time(filter_animal_events, "day")
        filter_animal_night_event = filter_day_night_time(filter_animal_events, "night")

        filter_vehicle_events = filtered_ids.filter(specie_id="vehicle")
        filter_vehicle_day_event = filter_day_night_time(filter_vehicle_events, "day")
        filter_vehicle_night_event = filter_day_night_time(filter_vehicle_events, "night")

        data_array = {
            "Camera_ID": element['camera_id'],
            "Total_Event_Count": filtered_ids.count(),
            "Day_Event_Count": len(filter_day_event),
            "Night_Event_Count": len(filter_night_event),
            "Person_Event_Count": filter_person_events.count(),
            "Person_Day_Count": len(filter_person_day_event),
            "Person_Night_Count": len(filter_person_night_event),
            "Animal_Event_Count": filter_animal_events.count(),
            "Animal_Day_Count": len(filter_animal_day_event),
            "Animal_Night_Count": len(filter_animal_night_event),
            "Vehicle_Event_Count": filter_vehicle_events.count(),
            "Vehicle_Day_Count": len(filter_vehicle_day_event),
            "Vehicle_Night_Count": len(filter_vehicle_night_event),
        }

        cameras_summary_data.append(data_array)

    return Response(cameras_summary_data)


def filter_day_night_time(data_array, event_type):
    return [data for data in data_array if get_time_of_day(data.Time) == event_type]


def post_create_summary(request):
    # Implement logic to handle POST requests
    pass


