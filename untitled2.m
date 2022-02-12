clear all;
clc; 
close all;
% Sygnał 
[x, fp] = audioread('coursee.wav');
% Parametry 
N=fp; 
Tp=1/fp; 
x=x(1:N)'; 
i=(0:N-1);
% Przegieg czasowy
figure(1)
plot (i*Tp, x) 
xlabel('t[s]')
ylabel('x')
title("Przebieg czasowy")
%GWM
X_fft = Tp*fft(x, N);
X_gwm = (abs(X_fft(1:N/2)).^2)/N/Tp;
%GWM Plot
figure(2)
title('GWM')
plot(0:N/2 -1, 10*log10(X_gwm));
% filtr 
wp = 100/1000;
ws = 150/1000;
rp = 1;
rs = 20;
[n, wn] = buttord(wp, ws, rp, rs);
[b, a] = butter(n, wn, 'high');
x_f = filter(b, a, x);
% plotting 
X_ffft = Tp*fft(x_f, N);
X_fgwm = (abs(X_ffft(1:N/2)).^2)/N/Tp;
figure(3)
hold on
title('GWM')
plot(0:N/2 -1, 10*log10(X_gwm));
plot(0:N/2 -1, 10*log10(X_fgwm));
hold off
figure(4)
hold on
plot (i*Tp, x) 
plot(i*Tp, x_f)
xlabel('t[s]')
ylabel('x')
title("Przebieg czasowy")
legend('Signal', 'Filtered Signal')
hold off

