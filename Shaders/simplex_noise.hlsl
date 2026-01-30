// This is a custom node simplex cloud noise
// Note that using a texture it´s waaay faster than computing this math per pixel.

const float DPX = 0.03;
const float2x2 rot45 = float2x2(0.707, 0.707, -0.707, 0.707);
const float2 SCALE = float2(5.9, 2.7);
const float2 SCALE2 = float2(7.9, 7.3);

const float3 c1 = float3(.6, .4, .49);
const float3 c2 = float3(.3, .22, .27);

struct MyFunctions{
    float2 hash(float2 p)
  {
        p = float2( dot(p,float2(127.1,311.7)),
                    dot(p, float2 (269.5,183.3)));
    return -1.0 + 2.0*frac(sin(p)*43758.5453123);
  }

    float noise(float2 p)
    {
        const float K1 = 0.366025404;
        const float K2 = 0.211324865;

        float2 i = floor( p + (p.x+p.y)*K1 );
        float2 a = p - i + (i.x+i.y)*K2;
        float2 o = step(a.yx,a.xy);    
        float2 b = a - o + K2;
        float2 c = a - 1.0 + 2.0*K2;

        float3  h = max( 0.5-float3(dot(a,a), dot(b,b), dot(c,c) ), 0.0 );
        float3  n = h*h*h*h*float3( dot(a,hash(i+0.0)), dot(b,hash(i+o)), dot(c,hash(i+1.0)));

        return dot(n,float3(70.0,70.0,70.0));

    }

    float fnoise(float2 p)
    {
        float f = 0.0;
        p *= 5.0;
        float2x2 m = float2x2( 1.6,  1.2, -1.2,  1.6 );
        f  = 0.5000*noise( p ); p = mul(m,p);
        f += 0.2500*noise( p ); p = mul(m,p);
        f += 0.1250*noise( p ); p = mul(m,p);
        f += 0.0625*noise( p ); p = mul(m,p);
        return(f);
    }

    float cloud(float2 uv, float cloudy, float sharp, float time)
    {
        uv += 0.05*pow(sin(time+uv.x*4.0),2.0);
        float hh = 0.9+0.1*fnoise(uv*1.7+float2(time*-4.5,time*-3.7));
        float h = 0.9+0.1*fnoise(uv+float2(time*2.1,time*1.7));
        uv += float2(time*0.7,time*0.9);
        float d = cloudy*0.33+0.4*fnoise(uv*0.25)+0.2*h+0.5*hh;
        d = smoothstep(0.5-sharp,0.5+sharp,clamp(d*d,0.0,1.0));

        return (d*h);
    }

};
MyFunctions f;


uv = mul(rot45,(uv.xy));
time = time*0.2;
float cl1 = f.cloud(uv * SCALE, 0.3, 0.15, time);


return cl1;
