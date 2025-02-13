import psutil
import subprocess

def check_service_status_and_start(service_list, service_to_auto_start, turn_on_feature):
        for service in service_list:
            the_service = get_service(service)
            if the_service:
                service_is_auto_start = the_service.name() in service_to_auto_start and turn_on_feature == False
                print(f"{the_service.display_name()} is {the_service.status()}")
                if the_service.status() == "stopped" and turn_on_feature:
                    print('Attempting to start the service ' + the_service.display_name())
                    try:  
                        result = subprocess.run(["net", "start", the_service.name()], capture_output=True, text=True, check=True)
                    except Exception as e:
                        print(f"An exception as occurred {e}")
                    finally:
                        print(f"{the_service.display_name()} has been started")
                        print(f"{the_service.display_name()} is {the_service.status()}")
                elif the_service.status() == "stopped" and service_is_auto_start:
                    print(f"{the_service.display_name()} is in the list of services to auto start")
                    print("Auto starting the service")
                    result = subprocess.run(["net", "start", the_service.name()], capture_output=True, text=True, check=True)
            else:
                print(f"{service} not found")
            
def get_service(service_name):
    for service in psutil.win_service_iter():
        if service.name().lower() == service_name.lower():
            return service
    return None