function [M] = cube3D(La, Ro, Co)
% cube3D(L, R, C) returns 3 D cube filled with range 1:(L*R*C)

    Cv = La * Ro * Co;
    printf(" Layers: %d\n", La);
    printf("   Rows: %d\n", Ro);
    printf("Columns: %d\n", Co);
    
    
    for L = 0:La-1;
        for R = 0:Ro-1;
            for C = 0:Co-1;
                M(L+1,R+1,C+1) = L*R*C + R*C + C;
            end
        end
    end
end
 
%    M(1:L,1:R,1:C) = 1:L * 1:R * 1:C;
    