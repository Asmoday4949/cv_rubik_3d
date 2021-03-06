#version 310 es

uniform mat4 uMMatrix;
uniform mat4 uVMatrix;
uniform mat4 uPMatrix;

in vec3 aVertex;
in vec3 aColor;

out vec3 vVertex;
out vec3 vColor;

void main()
{
    gl_Position = uPMatrix * uVMatrix * uMMatrix * vec4(aVertex, 1.0);
    vVertex = aVertex;
    vColor = aColor;
}
