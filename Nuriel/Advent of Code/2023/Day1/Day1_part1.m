clear all; close all; clc;

fid = fopen('D:\Home Projects\GitHub Projects\aoc-2023\Nuriel\Advent of Code\2023\Day1\input.txt');
format = '%c';
doc = strsplit(fscanf(fid,format));
answer = 0;
for i = 1:length(doc)-1
    doc{2,i} = double(char(doc{1,i}));
    doc{3,i} = char(doc{2,i}(find((doc{2,i} < 58) & (doc{2,i} > 47))));
    doc{4,i} = [doc{3,i}(1) doc{3,i}(end)];
    doc{5,i} = str2num(doc{4,i});
    answer = answer + doc{5,i};
end