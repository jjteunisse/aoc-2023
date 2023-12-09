clear all; close all; clc;

fid = fopen('D:\Home Projects\GitHub Projects\aoc-2023\Nuriel\Advent of Code\2023\Day9\example1.txt','r');
format = '%c';
doc = strsplit(fscanf(fid,format),{'\n'});
answer = int32(0);
for i = 1:length(doc)
    list(i).input = str2num(doc{i});
    list(i).decim(1).derivative = list(i).input(2:end) - list(i).input(1:end-1);
    for j = 2:length(list(i).decim(1).derivative)
        list(i).decim(j).derivative = list(i).decim(j-1).derivative(2:end) - list(i).decim(j-1).derivative(1:end-1);
        if list(i).decim(j).derivative == zeros(length(list(i).decim(j).derivative),1)
            maxList = length(list(i).decim);
            list(i).decim(j).add = 0;
            for k = 1:maxList-1
                list(i).decim(j-k).add = list(i).decim(j-k).derivative(end) + list(i).decim(j-k+1).add;
            end
            break;
        end
    end
    list(i).added = list(i).input(end) + list(i).decim(1).add;
    answer = answer + int32(list(i).added);
end