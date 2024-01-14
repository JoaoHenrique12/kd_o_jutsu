import pandas as pd
from pathlib import Path

base_path = Path(f"{__file__}").resolve().parent

jutsu_path = base_path / 'database/jutsu.csv'
seal_path = base_path / 'database/seal.csv'
jutsu_have_seal_path = base_path / 'database/jutsu_have_seal.csv'

def search_jutsu_df_by_name(name=''):
    df = pd.read_csv(jutsu_path)
    return df[df['title'].str.contains(name, case=False)]

def search_jutsu_df_by_seals_id(seals_id=[]):
    jhs = pd.read_csv(jutsu_have_seal_path)
    jutsus_found = pd.read_csv(jutsu_path)

    jutsu_ids = set(jhs['jutsu_id'])
    for position, seal_id in enumerate(seals_id, 1):
        jutsu_found_at = jhs[(jhs['seal_id'] == seal_id) & (jhs['position'] == position)]
        jutsu_ids = jutsu_ids & set(jutsu_found_at['jutsu_id'])

    jutsus_found = jutsus_found[jutsus_found['id'].isin(jutsu_ids)]

    return jutsus_found

def search_seals_id_by_jutsu_id(jutsu_id):
    df = pd.read_csv(jutsu_have_seal_path)
    seals_at_jutsu_id = df[df['jutsu_id'] == jutsu_id]
    seals_at_jutsu_id = seals_at_jutsu_id.sort_values(by='position')

    return seals_at_jutsu_id.loc[:,'seal_id'].tolist()

def get_seal_name_by_id(seal_id=None):
    df = pd.read_csv(seal_path)
    name = df[df['id'] == seal_id]
    name = name.iloc[0,1].strip().lower()
    return name
