musica = str(input('Digita: ').lower())
def musicas(musica):
    while musica[0] == 'a':
        musica = musica.split()

        if musica[-1] != 'saudade':
            musica = str(input('Digita: ').lower())
            musicas(musica)
        else:
            break

musicas(musica)