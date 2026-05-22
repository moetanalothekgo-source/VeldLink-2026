def test_low_power_rollback():
    assert smart_sync(data_packet, 15) == "Paused - State Saved"
