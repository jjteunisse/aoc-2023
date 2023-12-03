clear all; close all; clc;

fid = fopen('D:\Home Projects\GitHub Projects\aoc-2023\Nuriel\Advent of Code\2023\Day1\input2.txt');
format = '%c';
doc = strsplit(fscanf(fid,format));

answer = 0;
for i = 1:length(doc)
    if ~isempty(doc{1,i})
        doc{2,i} = strNumRep(doc{1,i});
        answer = answer + doc{2,i};
    end
end



function num_out = strNumRep(string_in)
    check1 = ["one","two","three","four","five","six","seven","eight","nine"];
    check2 = ["1","2","3","4","5","6","7","8","9"];
    val = [];
    pos = [];
    for i = 1:length(check1)
        temp = strfind(string_in,check1(i));
        if ~isempty(temp)
            val = [val temp];
            pos = [pos i*ones(1,length(temp))];
        end
    end
    for i = 1:length(check2)
        temp = strfind(string_in,check2(i));
        if ~isempty(temp)
            val = [val temp];
            pos = [pos i*ones(1,length(temp))];
        end
    end
    maximum = pos(find(val == max(val)));
    minimum = pos(find(val == min(val)));
    num_out = double(append(string(minimum),string(maximum)));
end