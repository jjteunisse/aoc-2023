clear all; close all; clc;

fid = fopen('D:\Home Projects\GitHub Projects\aoc-2023\Nuriel\Advent of Code\2023\Day8\input.txt','r');
format = '%c';
doc = strsplit(fscanf(fid,format),{' = (','\n',')',', ',' '});
input.dir = strrep(doc{1,1},'L','2 ');
input.dir = str2num(strrep(input.dir,'R','3 '));
input.startChar = 65;
input.endChar = 90;
input.listID = [];
input.locationPointer = [];

for i = 0:(length(doc)-2)/4-1
    for j = 1:3
        temp = double(doc{1,2+j+4*i});
        input.directions(i+1,j) = str2num(strcat(num2str(temp(1)),num2str(temp(2)),num2str(temp(3))));
        if j == 1
            input.characterization(i+1) = temp(3);
        end
        temp2 = find(input.listID == input.directions(i+1,j));
        if ~isempty(temp2)
            input.directionID(i+1,j) = temp2;
        else
            input.listID = [input.listID input.directions(i+1,j)];
            input.directionID(i+1,j) = length(input.listID);
        end
    end   
    if input.characterization(i+1) == input.startChar
        input.locationPointer = [input.locationPointer i+1];
    end
end
for i = 1:length(input.listID)
    input.listIDpointer(i) = find(input.directions(:,1) == input.listID(i));
end
input.iterationAmount = length(input.locationPointer);
input.locationCounter = zeros(length(input.locationPointer),1);
for z = 1:length(input.locationPointer)
    while ~isequal(input.characterization(input.locationPointer(z)),input.endChar)
        for i = 1:length(input.dir)
            input.locationCounter(z) = input.locationCounter(z) + 1;
            input.locationPointer(z) = input.listIDpointer(input.directionID(input.locationPointer(z),input.dir(i)));
            if isequal(input.characterization(input.locationPointer(z)),input.endChar)
                break;
            end
        end
    end
end
answer = lcm(sym(input.locationCounter));