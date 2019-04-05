#version 310 es
precision mediump float;


in vec3 vColor;
out vec4 oColor;

void main() {
    // We're not interested in changing the alpha value
    oColor = vec4(vColor, 1.0);
}
