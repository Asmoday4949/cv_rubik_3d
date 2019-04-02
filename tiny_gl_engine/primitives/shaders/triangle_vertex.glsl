#version 310 es

uniform mat4 uMMatrix;
uniform mat4 uVMatrix;
uniform mat4 uPMatrix;

in vec3 in_vert;
in vec3 in_color;
out vec3 v_color;    // Goes to the fragment shader

void main() {
    gl_Position = uMMatrix * uVMatrix * uPMatrix * vec4(in_vert, 1.0);
    v_color = in_color;
}
