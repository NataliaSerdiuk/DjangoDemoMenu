from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children',
                               verbose_name='Родительское меню')
    menu_url = models.CharField(max_length=100, blank=True, null=True, unique=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return str(self.name)

    def get_children(self):
        return self.children.all()

    def get_parent_ids(self):
        if self.parent:
            return self.parent.get_parent_ids() + [self.parent.id]
        else:
            return []

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Создать меню'