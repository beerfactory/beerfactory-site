# -*- coding: utf-8 -*- #

from pelican import signals
from pelican import contents

def map_cat_diaply_name(sender, instance):
        if hasattr(instance, 'category'):
            category_name = instance.category.name
            cat_map = instance.settings.get('CAT_DISPLAY_NAME_MAP', {})
            try :
                instance.category.display_name = cat_map[category_name]
            except (KeyError):
                instance.category.display_name = category_name

def register():
        signals.content_object_init.connect(map_cat_diaply_name)