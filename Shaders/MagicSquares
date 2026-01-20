// This Code goes into a custom node.
// Go to Gifs/MagicSquares.gif to see the result
// Go to Nodes/MagicSquares.png to see node structure

float aspect = View.ViewSizeAndInvSize.y / View.ViewSizeAndInvSize.x;

float2 uv = fragcoord.xy / View.ViewSizeAndInvSize.x;
uv -= float2(0.5, 0.5 * aspect);

float rot = radians(45.0);
float2x2 m = float2x2(
    cos(rot), -sin(rot),
    sin(rot),  cos(rot)
);
uv = mul(uv, m);

uv += float2(0.5, 0.5 * aspect);

float2 pos = uv * 10.0;
float2 rep = frac(pos);

float dist = 2.0 * min(
    min(rep.x, 1.0 - rep.x),
    min(rep.y, 1.0 - rep.y)
);

float2 cell = floor(pos) + 0.5;
float2 center = float2(5.0, 5.0);
float squareDist = length(cell - center);

// inward motion
pos -= normalize(cell - center) * Time * 0.5;

// edge animation
float edge = sin(Time - squareDist * 0.5) * 0.5 + 0.5;

float value = frac(dist * 2.0);
value = lerp(value, 1.0 - value, step(1.0, edge));

edge = pow(abs(1.0 - edge), 2.0);
value = smoothstep(edge - 0.05, edge, 0.95 * value);

value += squareDist * 0.1;

float4 color = lerp(float4(1,1,1,1), float4(0.5,0.75,1,1), value);

return 0.25 * clamp(value, 0.0, 1.0);
