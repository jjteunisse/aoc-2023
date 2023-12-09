clear all; close all; clc;

fid = fopen('D:\Home Projects\GitHub Projects\aoc-2023\Nuriel\Advent of Code\2023\Day8\input.txt','r');
format = '%c';
doc = strsplit(fscanf(fid,format),{' = (','\n',')',', ',' '});
input.dir = strrep(doc{1,1},'L','2 ');
input.dir = str2num(strrep(input.dir,'R','3 '));
input.startID = 656565;
input.endID = 909090;
input.listID = [];
for i = 0:(length(doc)-2)/4-1
    for j = 1:3
        temp = double(doc{1,2+j+4*i});
        input.directions(i+1,j) = str2num(strcat(num2str(temp(1)),num2str(temp(2)),num2str(temp(3))));
        temp2 = find(input.listID == input.directions(i+1,j));
        if ~isempty(temp2)
            input.directionID(i+1,j) = temp2;
        else
            input.listID = [input.listID input.directions(i+1,j)];
            input.directionID(i+1,j) = length(input.listID);
        end
    end   
    if input.directions(i+1,1) == input.startID
        input.locationPointer = i+1;
        input.locationCounter = 0;
    end
end
for i = 1:length(input.listID)
    input.listIDpointer(i) = find(input.directions(:,1) == input.listID(i));
end

while input.directions(input.locationPointer,1) ~= input.endID   
    for i = 1:length(input.dir)
        input.locationCounter = input.locationCounter + 1;
        input.locationPointer = input.listIDpointer(input.directionID(input.locationPointer,input.dir(i)));
        if input.directions(input.locationPointer,1) == input.endID  
            break;
        end
    end
end
answer = input.locationCounter;