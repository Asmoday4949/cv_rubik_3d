#version 310 es

uniform mat4 uMMatrix;
uniform mat4 uVMatrix;
uniform mat4 uPMatrix;

in vec3 aVertex;
in vec3 aColor;
out vec3 vColor;    // Goes to the fragment shader

void main()
{
    gl_Position = uMMatrix * uVMatrix * uPMatrix * vec4(aVertex, 1.0);
    vColor = aColor;
}
