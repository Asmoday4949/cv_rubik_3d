#version 310 es

uniform mat4 uMMatrix;
uniform mat4 uVMatrix;
uniform mat4 uPMatrix;

in vec3 aVertex;
in vec4 aColor;

out vec4 vColor;

void main()
{
    gl_Position = uMMatrix * uVMatrix * uPMatrix * vec4(aVertex, 1.0);
    vColor = aColor;
}
