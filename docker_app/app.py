import time

def saluer(nom="Monde"):
    return f"Hello {nom} depuis mon conteneur Docker sur-mesure !"

if __name__ == "__main__":
    print(saluer())
    # Boucle infinie pour maintenir le conteneur en vie dans Kubernetes
    while True:
        time.sleep(3600)