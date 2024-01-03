use std::fs;
use std::ops::Range;

#[derive(Debug)]
struct AlmanacMap {
    ranges:Vec<SmallRange>,
}

impl AlmanacMap {
    fn build_map (map_str:&str) -> Self {
        let mut map_lines = map_str.lines();
        let _map_header = map_lines.next();
        let ranges:Vec<SmallRange> = map_lines.map(|line| SmallRange::build_range(line)).collect();
        AlmanacMap{
            ranges:ranges,
        }
    }

    fn convert_range (&self, y:&Range<isize>) -> Vec<Range<isize>> {
        let mut converted:Vec<Range<isize>> = [].to_vec();
        let mut tobe_converted:Vec<Range<isize>> = [y.start..y.end].to_vec();
        for i in &self.ranges {
            let mut temp:Vec<Range<isize>> = [].to_vec();
            converted.append(&mut tobe_converted.iter().filter_map(|x| {
                match (x.contains(&i.start),x.contains(&i.end)) {
                    (true,true) => {temp.push(x.start..i.start);
                                temp.push(i.end..x.end);
                                Some(i.start+i.modifier..i.end+i.modifier)},
                    (true,false) => {temp.push(x.start..i.start);
                                    Some(i.start+i.modifier..x.end+i.modifier)},
                    (false,true) => {temp.push(i.end..x.end);
                                    Some(x.start+i.modifier..i.end+i.modifier)},
                    (false,false) =>    
                        if x.start > i.end || x.end < i.start{
                            temp.push(x.start..x.end);
                            None
                        }else{
                            Some(x.start+i.modifier..x.end+i.modifier)
                        },
            }}).collect());
            tobe_converted = temp;
        }
        converted.append(&mut tobe_converted);
        converted.into_iter().filter(|x| !(x.start-x.end==0) ).collect()
    }
}

#[derive(Debug)]
struct SmallRange {
    start:isize,
    end:isize,
    modifier:isize,
}

impl SmallRange {
    fn build_range (range_str:&str) -> Self {
        let values:Vec<isize> = range_str.split_whitespace().filter_map(|x| x.parse::<isize>().ok()).collect();
        SmallRange {
            start:values[1],
            end:values[1]+values[2],
            modifier:values[0]-values[1],
        }
    }
}

pub fn day5_1() {

    let contents = fs::read_to_string("inputs/day5")
        .expect("Should have been able to read the file");
    let headerincl = contents.split_once("\n\n").unwrap();
    let header = headerincl.0;
    let tables = headerincl.1;
    let (start, end): (Vec<(usize, isize)>, Vec<(usize, isize)>) = header
        .split_whitespace()
        .filter_map(|x| 
            x.parse::<isize>().ok())
        .enumerate()
        .partition(|(index, _)| index % 2 == 0);
        
    let mut seed_ranges:Vec<Range<isize>> = [].to_vec();
    for x in start.iter().zip(end.iter()) {
        seed_ranges.push(x.0.1..x.0.1+x.1.1);
    }

    let maps:Vec<AlmanacMap> = tables.split("\n\n").map(|x| AlmanacMap::build_map(x)).collect();
    for map in &maps {
        let mut new_ranges:Vec<Range<isize>> = [].to_vec();
        for seed_range in seed_ranges.iter() {
            new_ranges.append(&mut map.convert_range(seed_range));
        }
        seed_ranges = new_ranges;
    }
    println!("{}", seed_ranges.iter().map(|x| x.start).min().unwrap());
}