function x = derivative(x0)
% Lorenz system
a = 16;
r = 45;
b = 4;

x = zeros(size(x0));
x(1) = a*(x0(2) - x0(1));
x(2) = r*x0(1) - x0(2) - x0(1)*x0(3);
x(3) = x0(1)*x0(2) - b*x0(3);
end