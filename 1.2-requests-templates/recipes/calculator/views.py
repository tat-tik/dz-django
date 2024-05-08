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
def recipe_view(request, recipe):
    if recipe == "omlet":
        result = omlet_func()
    elif recipe == "pasta":
        result = pasta_func()
    elif recipe == "buter":
        result = buter_func()

        def omlet_func(request):
            context = {
                'recipe': {
                    'ingredient1': amount1,
                    'ingredient2': amount2,
                    'ingredient3': amount3,
                }
            }
            return render(request, 'calculator/index.html', context)


        def pasta_func(request):
            context = {
                'recipe': {
                    'ingredient1': amount1,
                    'ingredient2': amount2,
                }
            }
            return render(request, 'calculator/index.html', context)

        def buter_func(request):
            context = {
                'recipe': {
                    'ingredient1': amount1,
                    'ingredient2': amount2,
                    'ingredient3': amount3,
                    'ingredient4': amount4
                }
            }
            return render(request, 'calculator/index.html', context)


