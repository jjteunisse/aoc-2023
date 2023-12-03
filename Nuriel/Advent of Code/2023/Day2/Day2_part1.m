clear all; close all; clc;

fid = fopen('D:\Home Projects\GitHub Projects\aoc-2023\Nuriel\Advent of Code\2023\Day2\input1.txt','r');
format = '%c';
doc = splitlines(fscanf(fid,format));

maxColors = [12 13 14]; %red green blue

valid = ones(length(doc),1);
for i = 1:length(doc)
    doc_temp = strsplit(doc{i},{'; ',': '});
    for j = 2:length(doc_temp)
        color_temp = strsplit(doc_temp{1,j},', ');
        for k = 1:length(color_temp)
            cell_temp = color_temp{1,k};
            if (cell_temp(end) == 'd') && (str2num(cell_temp(1:end-4)) > maxColors(1))
                valid(i) = 0;
                break;
            elseif (cell_temp(end) == 'n') && (str2num(cell_temp(1:end-6)) > maxColors(2))
                valid(i) = 0;
                break;
            elseif (cell_temp(end) == 'e') && (str2num(cell_temp(1:end-5)) > maxColors(3))
                valid(i) = 0;
                break;
            end
        end
    end
end

answer = sum(find(valid == 1));