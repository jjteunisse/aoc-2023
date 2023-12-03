clear all; close all; clc;

fid = fopen('D:\Home Projects\GitHub Projects\aoc-2023\Nuriel\Advent of Code\2023\Day1\input2.txt');
format = '%c';
doc = strsplit(fscanf(fid,format));

answer = 0;
for i = 1:length(doc)
    if ~isempty(doc{1,i})
        doc{2,i} = strNumRep(doc{1,i});
        doc{3,i} = double(char(doc{2,i}));
        doc{4,i} = char(doc{3,i}(find((doc{3,i} < 58) & (doc{3,i} > 47))));
        doc{5,i} = [doc{4,i}(1) doc{4,i}(end)];
        doc{6,i} = str2num(doc{5,i});
        answer = answer + doc{6,i};
    end
end



function string_out = strNumRep(string_in)
    check = ["one","two","three","four","five","six","seven","eight","nine"];
    val = [];
    pos = [];
    for i = 1:length(check)
        temp = strfind(string_in,check(i));
        if ~isempty(temp)
            val = [val temp];
            pos = [pos i*ones(1,length(temp))];
        end
    end
    [~,val2] = sort(val,'ascend');
    pos = pos(val2);
    string_temp = string_in;
    for i = 1:length(pos)
        string_temp = strrep(string_temp,check(pos(i)),num2str(pos(i)));
    end
    string_out = string_temp;
end