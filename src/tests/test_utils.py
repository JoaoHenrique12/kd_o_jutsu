import pytest
import pandas as pd

from ..utils import search_jutsu_df_by_seals_id, search_seals_id_by_jutsu_id, get_seal_name_by_id

@pytest.mark.parametrize("seals_id, ans_jutsus_id",[
    ([10,13],[16]),
    ([10, 6, 1, 10, 5, 6, 11, 8],[95]),
    ([10, 6, 3, 8],[528]),
])
def test_search_jutsu_df_by_seals_id(seals_id, ans_jutsus_id):
    df = search_jutsu_df_by_seals_id(seals_id)
    jutsu_list = df['id'].tolist()

    jutsu_list.sort()
    ans_jutsus_id.sort()

    assert jutsu_list == ans_jutsus_id

@pytest.mark.parametrize("jutsu_id, ans_seals_id",[
    (16, [10,13]),
    (95, [10, 6, 1, 10, 5, 6, 11, 8]),
    (528, [10, 6, 3, 8]),
])
def test_search_seals_id_by_jutsu_id(jutsu_id, ans_seals_id):
    ids_found = search_seals_id_by_jutsu_id(jutsu_id)

    assert ids_found == ans_seals_id

@pytest.mark.parametrize("seal_id, seal_name",[
    (1, 'desconhecido'),
    (2, 'pássaro'),
    (12, 'coelho'),
    (13, 'carneiro'),
])
def test_get_seal_name_by_id(seal_id, seal_name):
    name_found = get_seal_name_by_id(seal_id)
    assert name_found == seal_name
