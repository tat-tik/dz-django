from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}


def dish_view(request, dish):
    servings = request.GET.get('servings', 5)
    recipe = {}
    for key, value in DATA.get(dish).items():
        recipe[key] = value * int(servings)
    context = dict.fromkeys(['recipe'], recipe)
    return render(request, 'calculator/index.html', context)