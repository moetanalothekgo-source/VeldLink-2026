def smart_sync(data, power_level):
    if power_level < 20:
        pause_sync()
        save_state_locally()
    else:
        transmit_to_aws(data)
