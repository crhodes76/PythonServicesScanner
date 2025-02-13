import psutil
import subprocess

list_of_services = ["Appinfo", "BthAvctpSvc", "tzautoupdate", "IntelAudioService", "cplspcon", "esifsvc"
                    "LSM", "Intel(R) TPM Provisioning Service", "iphlpsvc", "wlidsvc", "WdNisSvc"]
turn_on_feature = False

def get_service(service_name):
    for service in psutil.win_service_iter():
        if service.name().lower() == service_name.lower():
            return service
    return None

if __name__ == "__main__":

    for service in list_of_services:
        the_service = get_service(service)
        if the_service:
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
        else:
            print(f"{service} not found")