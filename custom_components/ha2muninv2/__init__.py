from .http import async_setup as setup_view

async def async_setup(hass, config):
    await setup_view(hass, config)
    return True

async def async_setup_entry(hass, entry):
    await setup_view(hass, {})
    return True
    