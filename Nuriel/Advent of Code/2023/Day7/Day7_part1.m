clear all; close all; clc;

fid = fopen('D:\Home Projects\GitHub Projects\aoc-2023\Nuriel\Advent of Code\2023\Day7\input2.txt','r');
format = '%c';
doc = strsplit(fscanf(fid,format),{' | ',':  ',': ','\n',' '});
hand = doc{1,1:2:end-1};

for i = 1:length(doc)/2
    poker(i).hand = doc{1,2*i-1};
    poker(i).bet = str2num(doc{1,2*i});
    poker(i).symbols = unique(poker(i).hand);
    poker(i).amount = histc(poker(i).hand,poker(i).symbols);
    temp = sort(poker(i).amount,'descend')
    if temp(1) == 5
        poker(i).value = 1000000000000;
    elseif temp(1) == 4
        poker(i).value = 10000000000;
    elseif temp(1) == 3
        if temp(2) == 2
            poker(i).value = 100000000;
        else
            poker(i).value = 1000000;
        end
    elseif (temp(1) == 2) && (temp(2) == 2)
        poker(i).value = 10000;
    elseif temp(1) == 2
        poker(i).value = 100;
    else
        poker(i).value = 1;
    end
    poker(i).value2 = poker(i).value;
    for j = 1:5
        temp = poker(i).hand(j)
        if temp == 'A'
            poker(i).value2 = poker(i).value2 + poker(i).value*14;
        elseif temp == 'K'
            poker(i).value2 = poker(i).value2 + poker(i).value*13;
        elseif temp == 'Q'
            poker(i).value2 = poker(i).value2 + poker(i).value*12;
        elseif temp == 'J'
            poker(i).value2 = poker(i).value2 + poker(i).value*11;
        elseif temp == 'T'
            poker(i).value2 = poker(i).value2 + poker(i).value*10;  
        else
            poker(i).value2 = poker(i).value2 + poker(i).value*str2num(temp); 
        end
        poker(i).value = poker(i).value/100;
    end
    valueList(i) = poker(i).value2;
end
[valueList2 order] = sort(valueList,'ascend');
answer = 0;
for i = 1:length(doc)/2
    poker(i).win = poker(i).bet*order(i);
    answer = answer + poker(i).win;
end