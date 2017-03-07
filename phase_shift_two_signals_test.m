%calculate phase shitt betweeen two signals, test lot of values
clc
close all
clear all

t=linspace(0,1,10000); %if the lentgh of this vector is not big enought, it will failt for N<500 miserably
T=1./100; %for this case be have 100 oscillations in the whole sample area, thats 100 points per oscillation
f=1./T;
w=2.*pi.*f;

phase=0.7;
for i=1:1000
    phase=2.*pi.*i./1000;
    a=cos(2.*t.*w);
    b=cos(2.*t.*w-phase);

    fa=fft(a);
    fb=fft(b);

    n=find(abs(fa)==max(abs(fa)),1);%we find the higher value of the fft
    disp(n)
    ang_a=angle(fa(n));
    ang_b=angle(fb(n));
    disp((mod(ang_a-ang_b,2.*pi)))
    Ang(i)=((mod(ang_a-ang_b,2.*pi))); %final angle, module 2pi
end
plot(linspace(0,2.*pi,1000),Ang)
%values are the same
