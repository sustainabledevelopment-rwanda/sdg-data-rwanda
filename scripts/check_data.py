from sdg.open_sdg import open_sdg_check


def alter_meta(meta):
# Automatically detect global indicators.
    if 'indicator_number' in meta:
        indicator_id = meta['indicator_number']
        id_parts = indicator_id.split('.')

        # Automatically set some predicable properties.
        meta['goal_number'] = id_parts[0]
        meta['target_number'] = id_parts[0] + '.' + id_parts[1]
        meta['target_name'] = 'global_targets.' + id_parts[0] + '-' + id_parts[1] + '-title'


# Validate the indicators.
validation_successful = open_sdg_check(config='config_data.yml', alter_meta=alter_meta)

# If everything was valid, perform the build.
if not validation_successful:
    raise Exception('There were validation errors. See output above.')
