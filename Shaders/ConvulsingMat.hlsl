//This goes in a custom node on UE5.
// Pin inputs are uvCoord, uvTilling, t, col, R, quality.

//This could be inclued on a *.usf but I kept it here for consistency.
struct MyFunctions{
    float2x2 rotate2D(float r)
  {
    return float2x2(cos(r), sin(r), -sin(r), cos(r));
  }
};

MyFunctions f;

//float2 R = View.ViewSizeAndInvSize.xy; -> worked better with Filed of View node.
float2 uv = (uvCoord-0.5)*uvTilling;
float2 n = float2(0,0);
float2 q = float2(0,0);
float2 p = uv;
float d = dot(p,p); // -> Only if you want the radial effect. 
float s = 12.0;
float a = 0.0;
float2x2 m = f.rotate2D(5.0);


for (float j = 0.0; j < quality; j++)
{
  p = mul(m,p);
  n = mul(m,n);
  q = p * s + t * 4.0 + sin(t * 4.0 - d * 6.0) * 0.8 + j + n; //This is the real magic.
  a += dot(cos(q)/s, float2(0.2,0.2));
  n -= sin(q);
  s *= 1.2;
}

col = col * (a + 0.2) + a + a - d;

return float4(col,1.0);