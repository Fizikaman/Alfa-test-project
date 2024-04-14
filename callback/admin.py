from django.contrib import admin


class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "created",
        "updated",
    )
    search_fields = (
        "name",
        "email",
    )


class GameAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "players",
        "created",
        "updated",
    )
    search_fields = (
        "name",  # в задание поиска по играм не было, но пусть будет. так удобнее.
        "players__name"
    )
    inlines = [PlayerAdmin]
    list_display_links = (
        "name",
        "players",
    )

    # чуть-чуть оптимизации не помешает
    def get_queryset(self, request):
        queryset = super(GameAdmin, self).get_queryset(request)
        queryset = queryset.select_related("players").only(
            "id",
            "name",
            "email",
        )
        return queryset
