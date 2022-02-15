# Este archivo causa un FileNotFound exception

def main():
    open("folder/img/SolarSystem.png")
# No se supone que debe tener ningun try
if __name__ == '__main__':
    main()