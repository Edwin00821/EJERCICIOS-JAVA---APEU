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

fra = [
    'humanité',
    'Humain',
    'la personne',
    'personnes',
    'Hommes',
    'Femme',
    'bébé',
    'Ado',
    'Chevalier',
    'Dame',
    'individu',
    'Santé',
    'Corps',
    'jambe',
    'le pied',
    'talon',
    'tibia',
    'genou',
    'la cuisse',
    'Tête',
    'visage',
    'bouche',
    'lèvre',
    'dent',
    'œil',
    'nez',
    'barbe',
    'moustache',
    'Cheveu',
    'oreille',
    'cerveau',
    'estomac',
    'bras',
    'coude',
    'épaule',
    'ongle',
    'main',
    'poignet',
    'palmier',
    'doigt',
    'abdomen',
    'foie',
    'le muscle',
    'cou',
    'coeur',
    'dérange',
    'âme',
    'esprit',
    'buste',
    'taille',
    'hanche',
    'dos',
    'du sang',
    'viande',
    'peau',
    'os',
    ',un froid',
    'grippe',
    'diarrhée',
    'maladies',
    'famille',
    'collègue',
    'partenaire',
    'mariage',
    'amour',
    'papa',
    'mère',
    'neveu',
    'la nièce',
    'créature',
    'espèces',
    'être',
    'la vie',
    'naissance',
    'la reproduction',
    'décès',
    'géographie',
    'la nature',
    'Campagne',
    'Forêt',
    'désert',
    'côte',
    'plage',
    'fleuve',
    'lumière',
    'énergie',
    'animal',
    'chien',
    'chat',
    'vache',
    'porc',
    'Mouton',
    'arc',
    'tigre',
    'lapin',
    'dragon',
    'cerf',
    'grenouille'
]

es_fra = dict(zip(es, fra))

print(es_fra)

file = open('es_fraDic', 'wb')
pickle.dump(es_fra, file)
file.close()
