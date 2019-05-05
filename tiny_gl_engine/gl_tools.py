#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""gl_tools.py: several tools for moderngl """

__author__ = "Lucas Bulloni, Malik Fleury, Bastien Wermeille"
__version__ = "1.0.0"

import moderngl

def create_context():
    """ Create context """
    return moderngl.create_context()

def create_vertices_buffer(vertices):
<<<<<<< HEAD
    """ Create buffer of vertices from array """
    vBuffer = glBuffer(GL_ARRAY_BUFFER, len(vertices), vertices, GL_STATIC_DRAW)
=======
    vBuffer = glBuffer(GL_ARRAY_BUFFER, len(
        vertices), vertices, GL_STATIC_DRAW)
>>>>>>> 0e2cf85e4892b601f6e3c033206fd46cf874f8f4

def load_shaders(context, vertex_shader_filepath, fragment_shader_filepath):
    """ Load shaders (vertex and fragment) """
    vertex_shader = load_file_content(vertex_shader_filepath)
    fragment_shader = load_file_content(fragment_shader_filepath)
    return context.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

def load_file_content(filepath):
    """ Load the content of a file """
    file = open(filepath, 'r')
    content = file.read()
    file.close()
    return content


def print_matrix(matrix):
<<<<<<< HEAD
    """ Print matrix (for debug) """
    for i in range(0,4):
        for j in range(0,4):
=======
    for i in range(0, 4):
        for j in range(0, 4):
>>>>>>> 0e2cf85e4892b601f6e3c033206fd46cf874f8f4
            print(matrix[i * 4 + j], end=" ")
        print()
