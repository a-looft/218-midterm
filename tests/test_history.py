import os
from app.history_facade import HistoryFacade

def test_history_add_save_load(tmp_path):
    file = tmp_path / "test_history.csv"
    history = HistoryFacade(filepath=str(file))

    history.add_record("add", ["1", "2"], 3.0)
    history.save()

    new_history = HistoryFacade(filepath=str(file))
    assert not new_history.df.empty
    assert new_history.df.iloc[0]["command"] == "add"
    assert new_history.df.iloc[0]["result"] == 3.0
