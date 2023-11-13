function [M] = cubeCount(s)
% cubeCount(s) returns s x s x s 3D matrix filled with 1:s^3
    c = [];
    for L = 0 : s - 1
        c = [c ; [reshape(1:s^2, s, s)] + L * s^2];
    end
    M = reshape(c', s, s, s);
end
