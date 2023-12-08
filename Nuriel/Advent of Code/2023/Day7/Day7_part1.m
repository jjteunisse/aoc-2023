clear all; close all; clc;

fid = fopen('D:\Home Projects\GitHub Projects\aoc-2023\Nuriel\Advent of Code\2023\Day7\example1.txt','r');
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
        poker(i).value = int32(1073741824); %2^30
    elseif temp(1) == 4
        poker(i).value = int32(536870912); %2^29
    elseif temp(1) == 3
        if temp(2) == 2
            poker(i).value = int32(268435456); %2^28
        else
            poker(i).value = int32(134217728); %2^27
        end
    elseif (temp(1) == 2) && (temp(2) == 2)
        poker(i).value = int32(67108864); %2^26
    elseif temp(1) == 2
        poker(i).value = int32(33554432); %2^25
    else
        poker(i).value = int32(0); %2^24
    end
    poker(i).value2 = poker(i).value;
    for j = 1:5
        temp = poker(i).hand(j)
        if temp == 'A'
            poker(i).value2 = poker(i).value2 + int32(14*16^(6-j));
        elseif temp == 'K'
            poker(i).value2 = poker(i).value2 + int32(13*16^(6-j));
        elseif temp == 'Q'
            poker(i).value2 = poker(i).value2 + int32(12*16^(6-j));
        elseif temp == 'J'
            poker(i).value2 = poker(i).value2 + int32(11*16^(6-j));
        elseif temp == 'T'
            poker(i).value2 = poker(i).value2 + int32(10*16^(6-j)); 
        else
            poker(i).value2 = poker(i).value2 + int32(str2num(temp)*16^(6-j)); 
        end
    end
    valueList(i) = poker(i).value2;
end
[valueList2 order] = sort(valueList,'ascend');
rank = 1:length(valueList2);
rank(order) = rank;
answer = 0;
for i = 1:length(doc)/2
    poker(i).rank = rank(i);
    poker(i).win = poker(i).bet*poker(i).rank;
    answer = answer + poker(i).win;
end