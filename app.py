import psutil

def get_service(service_name):
    for service in psutil.win_service_iter():
        if service.name().lower() == service_name.lower():
            return service
    return None

if __name__ == "__main__":
    services_to_check = ["Appinfo", "BthAvctpSvc", "tzautoupdate"]
    for service in services_to_check:
        the_service = get_service(service)
        if the_service:
            print(f"{the_service.display_name()} is {the_service.status()}")
        else:
            print(f"{service} not found")