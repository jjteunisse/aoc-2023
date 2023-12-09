clear all; close all; clc;

fid = fopen('D:\Home Projects\GitHub Projects\aoc-2023\Nuriel\Advent of Code\2023\Day6\input.txt','r');
format = '%c';
doc = strsplit(fscanf(fid,format),{'\n','Time:','Distance:'});
doc{2} = strrep(doc{2},' ','');
doc{3} = strrep(doc{3},' ','');
input.Tmax = str2num(doc{2});
input.Dmax = str2num(doc{3});
input.temp1 = 0.5*input.Tmax;
epsilon = 1e-10;
input.SolutionRange(:,1) = floor(input.temp1 + 0.5*sqrt(input.Tmax.*input.Tmax - 4*input.Dmax)-epsilon);
input.SolutionRange(:,2) = ceil(input.temp1 - 0.5*sqrt(input.Tmax.*input.Tmax - 4*input.Dmax)+epsilon);
input.Solutions = input.SolutionRange(:,1) - input.SolutionRange(:,2) + 1;
answer = prod(input.Solutions);