# -*- coding: utf-8 -*-
import os
import PIL
from docutils import nodes
from docutils.parsers.rst import directives, Directive
from docutils.parsers.rst.directives.images import Image
from pelican import signals
from pelican import contents

thumbnails = []

class Thumbnail(Image):

    def run(self):
        (node,) = directives.images.Image.run(self)
        if not isinstance(node, nodes.reference):
            return [node]
        image_node = node.children[0]

        thumbnail_info = {}
        thumbnail_info['thumbnail_file'] = image_node['uri']
        thumbnail_info['image_file'] = node['refuri']
        if 'scale' in image_node:
            thumbnail_info['scale'] = image_node['scale']
            del image_node['scale']
        if 'width' in image_node:
            thumbnail_info['width'] = image_node['width']
            del image_node['width']
        if 'height' in image_node:
            thumbnail_info['height'] = image_node['height']
            del image_node['height']
        thumbnails.append(thumbnail_info)
        return [node]

def generate_thumbnails(pelican):
    source_path = pelican.settings['PATH']
    output_path = pelican.settings['OUTPUT_PATH']
    for thumb in thumbnails:
        source_file = os.path.join(source_path, './' + thumb['image_file'])
        src_name, src_ext = os.path.splitext(source_file)
        img_src = PIL.Image.open(source_file)
        width_src, height_src = img_src.size

        if 'scale' in thumb:
            width_dst = int(width_src * (thumb['scale']*0.01))
            height_dst = int(height_src * (thumb['scale']*0.01))
        elif 'width' in thumb and not 'height' in thumb:
            width_dst = int(thumb['width'])
            height_dst = int((width_dst/width_src) * height_src)
        elif 'height' in thumb and not 'width' in thumb:
            height_dst = int(thumb['height'])
            width_dst = int((height_dst/height_src) * width_src)
        elif 'height' in thumb and 'width' in thumb:
            width_dst = int(thumb['width'])
            height_dst = int(thumb['height'])
        else:
            width_dst = width_src
            height_dst = height_src
        print("Creating thumbnail %s (%dx%d) from %s (%dx%d)" % (thumb['thumbnail_file'], width_dst, height_dst, thumb['image_file'], width_src, height_src))
        img_dst = img_src.resize((width_dst, height_dst), PIL.Image.ANTIALIAS)
        dst_file = os.path.normpath(os.path.join(output_path, './' + thumb['thumbnail_file']))
        img_dst.save(dst_file)
        print("  file %s created." % (dst_file))


def register():
    signals.finalized.connect(generate_thumbnails)
    directives.register_directive('thumbnail', Thumbnail)
