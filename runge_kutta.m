function xState = runge_kutta(h, n, x0)
[rows,cols] = size(x0);
stateVector = zeros(n, cols);
for i = 1:n
    k1 = derivative(x0);
    k2 = derivative(x0 + (h/2)*k1);
    k3 = derivative(x0 + (h/2)*k2);
    k4 = derivative(x0 + h*k3);
    x0 = x0 + (h/6)*(k1 + 2*k2 + 2*k3 + k4);
    x0 = mod(x0, 255);
    stateVector(i,:) = x0;
end
xState = stateVector;
end