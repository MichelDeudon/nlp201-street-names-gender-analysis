import pandas as pd


def test_load_street_names(url: str = "https://data.montpellier3m.fr/sites/default/files/ressources/20220905_bal_213401722_villedemontpellier.csv"):
    """
    Args:
        url: str, a link pointing a csv file of street names, e.g., at data.montpellier3m.fr or opendata.paris.fr
    """
    
    # read dataset (Montpellier street names)
    df = pd.read_csv(url, sep=";")
    assert len(df) >0
    assert 'lat' in df
    assert 'long' in df
    assert 'voie_nom' in df


def test_load_names_gender(url: str = "https://static.data.gouv.fr/resources/liste-de-prenoms/20141127-154433/Prenoms.csv"):
    """
    Args:
        url: str, a link pointing a csv file of names and gender, e.g., at data.gouv.fr
    """
    
    # read dataset (prenoms et genre from data.gouv.fr)
    names = pd.read_csv(url, encoding = "latin", sep=";", usecols=["01_prenom", "02_genre"], index_col="01_prenom")
    names = names.to_dict()['02_genre'] # mapping from name to gender, ex: Anne -> 'f' (or 'm', 'm,f')
    assert len(names) >0
    assert "marie" in names
