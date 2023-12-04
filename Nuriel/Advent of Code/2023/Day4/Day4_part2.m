clear all; close all; clc;
tic
fid = fopen('D:\Home Projects\GitHub Projects\aoc-2023\Nuriel\Advent of Code\2023\Day4\input.txt','r');
format = '%c';
doc = strsplit(fscanf(fid,format),{' | ',':  ',': ','\n'});

lotAmount = length(doc)/3;
answer1 = 0;
accumulation = ones(lotAmount,1);
for i = 0:lotAmount-1
    winNums(:,i+1) = str2num(doc{2+3*i});
    haveNums(:,i+1) = str2num(doc{3+3*i});
    NumsComm(i+1).val = winNums(ismember(winNums(:,i+1),haveNums(:,i+1)),i+1)';
    NumsComm(i+1).amount = length(NumsComm(i+1).val);
    if NumsComm(i+1).amount > 0
        NumsComm(i+1).value = 2^(NumsComm(i+1).amount-1);
        answer1 = answer1 + NumsComm(i+1).value;
    else
        NumsComm(i+1).value = 0;
    end
end

for i = 1:lotAmount-1
    if i+NumsComm(i).amount <= lotAmount
        endVal = i+NumsComm(i).amount;
    else
        endVal = lotAmount;
    end
    accumulation(i+1:endVal) = accumulation(i+1:endVal) + accumulation(i);
end
answer2 = sum(accumulation);
toc