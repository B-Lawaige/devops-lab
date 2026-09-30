from app import saluer

def test_saluer_defaut():
    assert saluer() == "Hello Monde depuis mon conteneur Docker sur-mesure !"

def test_saluer_personnalise():
    assert saluer("DevOps") == "Hello DevOps depuis mon conteneur Docker sur-mesure !"