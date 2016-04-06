% File to produce chaotic data sets in creation of cryptographic key for
% WRTG 3030

h = 0.001;
n = 500000;
x0 = [-13 -12 52];
x = runge_kutta(h,n,x0);

dataFile = fopen('lorenz.txt','w');
for i = 1:n
    fprintf(dataFile,'%d\n',x(i,2));
end
fclose(dataFile);


