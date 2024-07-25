from sdg.open_sdg import open_sdg_build


def alter_meta(meta):
# Automatically detect global indicators.
    if 'indicator_number' in meta:
        indicator_id = meta['indicator_number']
        id_parts = indicator_id.split('.')

        # Automatically set some predicable properties.
        meta['goal_number'] = id_parts[0]
        meta['target_number'] = id_parts[0] + '.' + id_parts[1]
        meta['target_name'] = 'global_targets.' + id_parts[0] + '-' + id_parts[1] + '-title'
        meta['indicator_name'] = 'global_indicators.' + id_parts[0] + '-' + id_parts[1] + '-' + id_parts[2] + '-title'
    return meta

open_sdg_build(config='config_data.yml', alter_meta=alter_meta)


def alter_data(df):
  if "REF_AREA" in df:
    df["GeoCode"]=df["REF_AREA"]=
  return df
 
open_sdg_build(config='config_data.yml', alter_data=alter_data)
