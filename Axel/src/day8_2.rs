use std::fs;
use std::collections::HashMap;
use core::cmp::min;

fn gcd(a:usize, b:usize) -> usize{
    let mut ans:usize = 1;
    let limit = min(a,b);
    for i in 2..(limit+1) {
        if a%i == 0 && b%i == 0 {
            ans = i;
        }
    }
    ans
}

fn lcm(a:usize, b:usize) -> usize{
    return a*(b/gcd(a,b));
}

pub fn day8_2() -> Result<usize,String> {
    let contents = fs::read_to_string("inputs/day8")
        .expect("Should have been able to read the file");

    let lines = contents.split_once("\n\n").unwrap();
    let mut nodes = HashMap::new();
    let mut location = Vec::new();
    for line in lines.1.lines() {
        let fullsplitline = line.split_once(" = ").unwrap();
        let entry = fullsplitline.0;
        let exit = fullsplitline.1.trim_matches(&['(', ')'][..]).split_once(", ").unwrap();
        nodes.insert(entry,exit);
        if entry.chars().last().unwrap() == 'A' {
            location.push(entry);
        }
    }
    
    let mut stepperstart = Vec::new();
    for start in location.iter_mut() {
        let mut directions = lines.0.chars().cycle();
        let mut steps = 0;
        loop {
            if start.chars().last().unwrap() == 'Z' {
                break
            }
            steps += 1;
    
            let rightorleft = directions.next().unwrap();
            *start = match rightorleft {
                'R' => Ok(nodes.get(start).unwrap().1),
                'L' => Ok(nodes.get(start).unwrap().0),
                _ => Err("not right or left"),
            }?
        };
        stepperstart.push(steps);
    }

    let mut eerste = stepperstart.pop().unwrap();
    for steps in stepperstart {
        eerste = lcm(eerste,steps)
    }

    Ok(eerste)
}