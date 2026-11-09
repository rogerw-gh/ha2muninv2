from homeassistant.components.http import HomeAssistantView
from aiohttp.web_response import Response

DOMAIN = "ha2muninv2"

async def async_setup(hass, config):
    hass.http.register_view(MuninAPI())
    return True

class MuninAPI(HomeAssistantView):
    url = "/api/munin"
    name = "api:munin"

    async def get(self, request):
        # Liste de sensors à exporter
        entity_ids = [
            "sensor.system_monitor_processor_use",
            "sensor.system_monitor_memory_usage",
            "sensor.system_monitor_swap_use",
            "sensor.system_monitor_load_1min",
            "sensor.system_monitor_load_5min",
            "sensor.system_monitor_load_15min",
            "sensor.system_monitor_disk_usage",
            "sensor.system_monitor_disk_use",
            "sensor.system_monitor_disk_use_media",
            "sensor.system_monitor_memory_use",
            "sensor.system_monitor_network_throughput_in_enp3s0",
            "sensor.system_monitor_network_out_enp0s18"
        ]
        data = {}
        for eid in entity_ids:
            state = request.app["hass"].states.get(eid)
            data[eid] = state.state if state else "U"
        # Formate pour Munin : un label par ligne, format "<nom>.value <valeur>"
        lines = [f"{eid.replace('sensor.system_monitor_', '')}.value {val}" for eid, val in data.items()]
        return Response(text="\n".join(lines), content_type="text/plain")