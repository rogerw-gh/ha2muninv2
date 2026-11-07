from homeassistant import config_entries

class Ha2MuninConfigFlow(config_entries.ConfigFlow, domain="ha2munin"):
    """Minimal config flow for HA2Munin."""

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="HA2Munin", data={})
        return self.async_show_form(step_id="user")