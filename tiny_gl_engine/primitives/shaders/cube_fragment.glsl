#version 310 es
precision mediump float;

in vec3 vVertex;
in vec3 vColor;

out vec4 oColor;

void main()
{
    if(abs(vVertex.x) > 0.95 && abs(vVertex.y) > 0.95 ||
      abs(vVertex.y) > 0.95 && abs(vVertex.z) > 0.95 ||
      abs(vVertex.z) > 0.95 && abs(vVertex.x) > 0.95)
    {
      oColor = vec4(0.0, 0.0, 0.0, 1.0);
    }
    else
    {
      oColor = vec4(vColor, 1.0);
    }
}
