1;

function [M] = randomCube()
% Generate and plot  4x4x4 cube filledd with rando 1s and 0s

	figure
	hold on
	M = zeros([4,4,4]);
	for p = [1:4]
		for r = [1:4]
			for c = [1:4]
				rnd = randi([0,1]);
				M(r,c,p) = rnd;
				if(rnd == 1)
					scatter3(r,c,5-p, 'MarkerFaceColor',[0 .75 .75], 'SizeData', 200)
				end
			end
		end
	end
	axis([0, 5, 0, 5, 0, 5]);
	view(54,30)
	display(M)
end
%-----------------------------------------------------------------
% repCount:  Create numeric cube counting 1:16 on 1st page
% 17:32 on second page, 33:48 on third page, 49:64 on last page.
rcpCount = @() rot90(fliplr(reshape([1:64], 4, 4, 4)), 1);

pg = @(n) floor((n - 1) / 16) + 1;
row = @(n) floor(mod((n-1),16)/4) + 1;
col = @(n) mod((n-1), 4)+1;
%-----------------------------------------------------------------

function [r, c, p] = rowcolpage(n)
% Find row, column and page from cell in repCount

    r = floor(mod((n-1),16)/4) + 1;
    c = mod((n-1), 4)+1;
    p = floor((n - 1) / 16) + 1;
end
%-----------------------------------------------------------------

#{
   Example Usage:
M = repCount()
% Pick any number in M.
[r, c, p] = rowcolpage(number)
#}
%-----------------------------------------------------------------

% Matrix Manipulatiion functions
ordercols = @(mat, a,b,c,d) cat(2,mat(:,a,:),mat(:,b,:),mat(:,c,:),mat(:,d,:));
orderrows = @(mat, a,b,c,d) cat(1,mat(a,:,:),mat(b,:,:),mat(c,:,:),mat(d,:,:));
orderpgs = @(mat, a,b,c,d) cat(3,mat(:,:,a),mat(:,:,b),mat(:,:,c),mat(:,:,d));
trans = @(mat) ordercols(orderrows(orderpgs(mat, 4,3,2,1), 4,3,2,1), 4,3,2,1);
coord = @(n) [floor(mod((n-1),16)/4)+1,mod((n-1),4)+1,floor((n-1)/16)+1];
% sersum = @(B) strcat("0X",dec2hex(sum(B.*2.^[length(B)-1:-1:0])));

%Example sersum Usage:  sersum([1,1,0,1,0,1,0,1])); 
%						returns 0XD5
%-----------------------------------------------------------------

function plotCube(H)
$ Plot Cube from 4xx4 matrix of 1s and 0s.

    figure
    set(gca, 'view', [54, 30])
    axis([0, 5, 0, 5, 0, 5])
	hold on;
    for p = [1:4]
        for r = [1:4]
            for c = [1:4]
                if (H(r,c,5-p) == 1)
                scatter3(r,c,p,'MarkerFaceColor',[0 .75 .75],'SizeData',200)
 				end
			end
		end
	end
end
%-----------------------------------------------------------------

function [M] = hexCube(B)
% Generate 16 character Hex String from 4x4x4 cube

	%sersum = @(B) strcat(" ", dec2hex(sum(B.*2.^[length(B)-1:-1:0])));
	sersum = @(B) dec2hex(sum(B.*2.^[length(B)-1:-1:0]));	
	M = [];
	for p = [1:4]
		for r = [1:2:4]
			M = [M, [sersum(B(r,:,p))]]
			M = [M, [sersum(B(r+1,:,p))]
			% M = [M, [sersum(bin2dec(B(r,:,p)))]];
			% M = [M, [sersum(bin2dec(B(r+1,:,p)))]];
		end
	
		% M = [[M], [sersum(reshape(B(1:2,:,p)',1,8))]];
		% M = [M, [" "]];
		% M = [[M], [sersum(reshape(B(3:4,:,p)',1,8))]];
		% M = [M, [" "]];
	end
end
%-----------------------------------------------------------------

function [bc, B] = bitLen(H)
% Return vector of bit lengths of 16 Hex digits.

	bc = [];
	B = [];
	for c = [1:16]
		bc = [bc, length(dec2bin(hex2dec(H(c))))];
	end
end
%-----------------------------------------------------------------

function [cube] = fillCube(H)
% Generate 4,4,4 binary cube from 16 character Hex String.

	rowBins = [];
	Z = zeros(16,4);
	for n = [1:16]
		rowBins = dec2bin(hex2dec(H(n)));
		bc = length(dec2bin(hex2dec(H(n))));
		chpos = 1;
		for p = [5-bc:4]
			Z(n,p) = str2num(rowBins(chpos));
			chpos += 1;
		end
	end
	% display(Z)
	cube = zeros(4,4,4);
	for p = [1:4]
		for r = [1:4]
			cube(r,:,p) = Z((p-1)*4+r,:);
		end
	end	
end
%-----------------------------------------------------------------

#{
M = circshift(M, [1,0,0]) % row + 1
M = circshift(M, [0,1,0]) % col + 1
M = circshift(M, [0,0,1]) % page + 1

M(1,:,:) % Row 1 on 4 pages
M(:,1,:) % Col 1 on 4 pages
M(:,:,1) % Page 1 
#}
%-----------------------------------------------------------------

