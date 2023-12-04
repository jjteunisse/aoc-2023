clear all; close all; clc;

fid = fopen('D:\Home Projects\GitHub Projects\aoc-2023\Nuriel\Advent of Code\2023\Day2\input1.txt','r');
format = '%c';
doc = splitlines(fscanf(fid,format));

maxRGB = zeros(length(doc),3);

for i = 1:length(doc)
    doc_temp = strsplit(doc{i},{'; ',': '});
    for j = 2:length(doc_temp)
        color_temp = strsplit(doc_temp{1,j},', ');
        for k = 1:length(color_temp)
            cell_temp = color_temp{1,k};
            if (cell_temp(end) == 'd') && (str2num(cell_temp(1:end-4)) > maxRGB(i,1))
                maxRGB(i,1) = str2num(cell_temp(1:end-4));
            elseif (cell_temp(end) == 'n') && (str2num(cell_temp(1:end-6)) > maxRGB(i,2))
                maxRGB(i,2) = str2num(cell_temp(1:end-6));
            elseif (cell_temp(end) == 'e') && (str2num(cell_temp(1:end-5)) > maxRGB(i,3))
                maxRGB(i,3) = str2num(cell_temp(1:end-5));
            end
        end
    end
end
power = maxRGB(:,1).*maxRGB(:,2).*maxRGB(:,3);
answer = sum(power);