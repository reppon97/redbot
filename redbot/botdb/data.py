BOTDB_DATA = {
    'сколько': {
        'лет': {
            'handler': 'wiki.AgeHandler',
            'morph': True
        },
        'длилась': {
            'handler': 'wiki.DurationHandler',
            'morph': True
        },
        'идет': {
            'handler': 'wiki.DurationHandler',
            'morph': True
        },
        'длится': {
            'handler': 'wiki.DurationHandler',
            'morph': True
        },
    },
    'какой': {
        'вес': {
            'handler': 'wiki.WeightHandler',
            'morph': True
        },
        'рост': {
            'handler': 'wiki.HeightHandler',
            'morph': True
        },
    },
    'когда': {
        'вышла': {
            'handler': 'wiki.ReleaseDateHandler',
            'morph': True
        },
        'вышел': {
            'handler': 'wiki.ReleaseDateHandler',
            'morph': True
        },
        'выйдет': {
            'handler': 'wiki.ReleaseDateHandler',
            'morph': True
        },
        'была': {
            'handler': 'wiki.DurationHandler',
            'morph': True
        },
        'проходила': {
            'handler': 'wiki.DurationHandler',
            'morph': True
        },
    },
    'погода': {
        'handler': 'weather.WeatherHandler',
        'morph': False
    },
    'загугли': {
        'handler': 'google.GoogleHandler',
        'morph': False
    },
    'время': {
        'handler': 'time.TimeHandler',
        'morph': False
    },
}
