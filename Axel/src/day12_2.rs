use std::error::Error;
use std::fs;
use std::collections::HashMap;

fn valid_springs(springs:&str, groups:&[usize]) -> bool {
    let gatestrings:Vec<_> = springs.split('.').filter_map(|x| if x != "" {Some(x)}else{None}).collect();
    let mut groupindex = 0;
    for gatestring in gatestrings {
        //println!("gatestring:{:?} groupindex:{:?}",gatestring,groupindex);
        if groupindex >= groups.len() {
            return false;
        }else if gatestring.len() == groups[groupindex]{
            groupindex += 1;
        }else{
            return false;
        }
    }
    if groupindex != groups.len()  {
        return false;
    }

    //println!("spring:{} groups:{:?}",springs,groups);
    true
}

fn build_seq(input:&str, build:&str, seq:&[usize]) -> usize {

    let mut buildstring = build.to_string();

    for (i,spring) in input.chars().enumerate() {
        match spring {
            '?' => {    
                        let mut string1 = buildstring.clone();
                        let mut string2 = buildstring;
                        string1.push('.');
                        string2.push('#');
                        return build_seq(&input[i+1..],&string1,seq) + build_seq(&input[i+1..],&string2,seq);
                    },
            '.' => buildstring.push('.'),
            '#' => buildstring.push('#'),
            _ => println!("{}", "unknown symbol"),
        };
    }
    //println!("input:{}  build:{}   seq{:?}:", input, build, seq);
    if valid_springs(&buildstring,seq) {
        return 1
    }else{
        return 0
    }
    0
}

pub fn day12_2() -> Result<usize, Box<dyn Error>> {
    let contents = fs::read_to_string("inputs/day12")
        .expect("Should have been able to read the file");

    let spring_recs:Vec<_> = contents.lines()
        .filter_map(|line| {
            if let Some(i) = line.split_once(' ') {
                let springs = i.0;
                let spring_grps:Vec<_> = i.1.split(',')
                    .filter_map(|grp| 
                        match grp.parse::<usize>() {
                            Ok(i) => Some(i),
                            Err(e) => {println!("{}", e);None},
                        }
                    ).collect();
                Some((springs,spring_grps))
            }else{
                println!("{}", "line missing space");
                None
            }
        }).collect();

    //println!("{:?}",spring_recs);
    let mut total = 0;
    for record in spring_recs {
        //println!("next:{:?}   total:{}", record,total);
        total += build_seq(record.0,"",&record.1);
    }
    
    

    Ok(total)
}