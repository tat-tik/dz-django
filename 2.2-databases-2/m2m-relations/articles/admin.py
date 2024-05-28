from django.contrib import admin

from .models import Article


class ArticleFormSet(BaseInlineFormSet):
        def clean(self):
        count = 0
        for form in self.forms:
            is_main = form.cleaned_data['is_main']

            if is_main:
                count += 1
            if count>1:
                raise ValidationError ('Основным может быть только один раздел')
            if is_main == False:
                raise ValidationError('Укажите основной раздел')

        return super().clean()




class ScopeAdmin(admin.TabularInline):
    model = Scope
    formset = ArticleFormSet
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeAdmin]

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    pass
