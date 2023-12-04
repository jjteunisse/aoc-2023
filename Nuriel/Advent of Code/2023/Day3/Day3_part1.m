clear all; close all; clc;

fid = fopen('D:\Home Projects\GitHub Projects\aoc-2023\Nuriel\Advent of Code\2023\Day3\input.txt','r');
format = '%c';
doc = splitlines(fscanf(fid,format));
M = char(doc{1:length(doc)});
Mt = M';
temp = (double(Mt) > 47) & (double(Mt) < 58);
Numbers.coordNum = find(temp);
Numbers.coordGear = find(~temp & (double(Mt)~=46));

Numbers.coordNumXY(:,2) = floor(Numbers.coordNum/length(M(1,:)))+1;
Numbers.coordGearXY(:,2) = floor(Numbers.coordGear/length(M(1,:)))+1;
Numbers.coordNumXY(:,1) = mod(Numbers.coordNum,length(M(1,:)));
Numbers.coordGearXY(:,1) = mod(Numbers.coordGear,length(M(1,:)));

Numbers.coordNumId = ones(length(Numbers.coordNumXY(:,1)),1);
Numbers.combined(1).Id = Mt(Numbers.coordNum(1));
for i = 2:length(Numbers.coordNumXY(:,1))
    if Numbers.coordNumXY(i,1) == Numbers.coordNumXY(i-1,1)+1
        Numbers.coordNumId(i) = Numbers.coordNumId(i-1);
    else
        Numbers.coordNumId(i) = Numbers.coordNumId(i-1) + 1;
        Numbers.combined(Numbers.coordNumId(i)).Id = '';
    end
    Numbers.combined(Numbers.coordNumId(i)).Id = [Numbers.combined(Numbers.coordNumId(i)).Id Mt(Numbers.coordNum(i))];
end
Numbers.coordNumIdIncl = zeros(Numbers.coordNumId(end),1);

for i = 1:length(Numbers.coordGear)
    temp = abs(Numbers.coordNumXY - Numbers.coordGearXY(i,:));
    Numbers.coordNumIdIncl(Numbers.coordNumId(find((temp(:,1) <= 1) & (temp(:,2) <= 1)))) = 1;
end
list = find(Numbers.coordNumIdIncl == 1);
for i = 1:length(list)
    numbersFinal(i) = str2num(Numbers.combined(list(i)).Id);
end
answer = sum(numbersFinal);