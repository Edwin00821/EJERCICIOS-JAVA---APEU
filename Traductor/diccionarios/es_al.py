import pickle

es = [
    'humanidad',
    'humano',
    'persona',
    'gente',
    'hombre',
    'mujer',
    'bebé',
    'adolescente',
    'caballero',
    'dama',
    'individuo',
    'salud',
    'cuerpo',
    'pierna',
    'pie',
    'talón',
    'espinilla',
    'rodilla',
    'muslo',
    'cabeza',
    'cara',
    'boca',
    'labio',
    'diente',
    'ojo',
    'nariz',
    'barba',
    'bigote',
    'cabello',
    'oreja',
    'cerebro',
    'estómago',
    'brazo',
    'codo',
    'hombro',
    'uña',
    'mano',
    'muñeca',
    'palma',
    'dedo',
    'abdomen',
    'hígado',
    'músculo',
    'cuello',
    'corazón',
    'mente',
    'alma',
    'espíritu',
    'pecho',
    'cintura',
    'cadera',
    'espalda',
    'sangre',
    'carne',
    'piel',
    'hueso',
    'resfriado',
    'gripe',
    'diarrea',
    'enfermedad',
    'familia',
    'colega',
    'pareja',
    'matrimonio',
    'amor',
    'padre',
    'madre',
    'sobrino',
    'sobrina',
    'criatura',
    'especie',
    'ser',
    'vida',
    'nacimiento',
    'reproducción',
    'muerte',
    'geografía',
    'naturaleza',
    'campo',
    'bosque',
    'desierto',
    'costa',
    'playa',
    'río',
    'luz',
    'energía',
    'animal',
    'perro',
    'gato',
    'vaca',
    'cerdo',
    'oveja',
    'mono',
    'tigre',
    'conejo',
    'dragón',
    'ciervo',
    'rana'
]

al = [
    'Menschheit',
    'Mensch',
    'Person',
    'Personen',
    'Männer',
    'Frau',
    'Baby',
    'Teenager',
    'Ritter',
    'Dame',
    'Individuell',
    'Die',
    'Gesundheit',
    'Körper',
    'Bein',
    'Fuß',
    'Hacke',
    'Schienbein',
    'Knie',
    'Schenkel',
    'Kopf',
    'teuer',
    'Mund',
    'Lippe',
    'Zahn',
    'Auge',
    'Nase',
    'Bart',
    'Schnurrbart',
    'Haar',
    'Ohr',
    'Gehirn',
    'Magen',
    'Arm',
    'Ellbogen',
    'Schulter',
    'Nagel',
    'Hand',
    'Handgelenk',
    'Palme',
    'Finger',
    'Abdomen',
    'Leber',
    'Muskel',
    'Nacken',
    'Herz',
    'Geist',
    'Seele',
    'Geist',
    'Truhe',
    'Taille',
    'Hüfte',
    'der',
    'Rücken',
    'Blut',
    'Fleisch',
    'Haut',
    'Knochen',
    'eine',
    'Erkältung',
    'Grippe',
    'Durchfall',
    'Krankheit',
    'Familie',
    'Kollege',
    'Partner',
    'die',
    'Ehe',
    'Liebe',
    'Papa',
    'Mutter',
    'Neffe',
    'Nichte',
    'Kreatur',
    'Spezies',
    'sein',
    'Leben',
    'Geburt',
    'Reproduktion',
    'Tod',
    'Erdkunde',
    'Natur',
    'Landschaft',
    'Wald',
    'Wüste',
    'Küste',
    'Strand',
    'Fluss',
    'hell',
    'Energie',
    'Tier',
    'Hund',
    'Katze',
    'Kuh',
    'Schweinefleisch',
    'Schaf',
    'Verneigung',
    'Tiger',
    'Hase',
    'Drachen',
    'Hirsch',
    'Frosch'
]

es_al = dict(zip(es, al))

print(es_al)

file = open('es_alDic', 'wb')
pickle.dump(es_al, file)
file.close()