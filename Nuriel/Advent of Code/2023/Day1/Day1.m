clear all; close all; clc;

fid = fopen('D:\Home Projects\Advent of Code\2023\Day1\input.txt');
format = '%c';
doc = strsplit(fscanf(fid,format));
for i = 1:length(doc)
    doc_ASCII{i,1} = double(char(doc{i}));
    doc_ASCII{i,2} = char(doc_ASCII{i,1}(find((doc_ASCII{i,1} < 58) & (doc_ASCII{i,1} > 47))));
    doc_ASCII{i,3} = [doc_ASCII{i,2}(1) doc_ASCII{i,2}(end)];
end