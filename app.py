import psutil

def check_service_status(service_name):
    for service in psutil.win_service_iter():
        if service.name().lower() == service_name.lower():
            return service.status()
    return None

if __name__ == "__main__":
    services_to_check = ["Appinfo", "BthAvctpSvc", "tzautoupdate"]
    for service in services_to_check:
        status = check_service_status(service)
        if status:
            print(f"{service} is {status}")
        else:
            print(f"{service} not found")