#version 310 es
precision mediump float;

in vec3 vVertex;
in vec3 vColor;

out vec4 oColor;

void main()
{
    float threshold = 0.85;

    if(abs(vVertex.x) > threshold && abs(vVertex.y) > threshold ||
      abs(vVertex.y) > threshold && abs(vVertex.z) > threshold ||
      abs(vVertex.z) > threshold && abs(vVertex.x) > threshold)
    {
      oColor = vec4(0.15, 0.15, 0.15, 1.0);
    }
    else
    {
      oColor = vec4(vColor, 1.0);
    }
}
