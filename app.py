import Modules.services_module as services_module
import json

with open("config.json", "r") as file:
    config = json.load(file)

list_of_services = config["services_list"]
turn_on_feature = True if config["turn_on_feature"] == "True" else False

service_to_auto_start = config["service_to_auto_start"]

if __name__ == "__main__":
    services_module.check_service_status_and_start(list_of_services, service_to_auto_start, turn_on_feature)
