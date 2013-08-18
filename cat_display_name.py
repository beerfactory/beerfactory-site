from pelican import signals
from pelican import contents

def test(sender, instance):
        print("%s : %s content initialized !!" % (sender, instance))

def register():
        signals.content_object_init.connect(test, sender=contents.Article)