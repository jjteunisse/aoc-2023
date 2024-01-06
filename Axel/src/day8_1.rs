use std::fs;
use std::collections::HashMap;



pub fn day8_1() -> Result<usize,String> {
    let contents = fs::read_to_string("inputs/day8")
        .expect("Should have been able to read the file");

    let lines = contents.split_once("\n\n").unwrap();
    let mut nodes = HashMap::new();
    let mut location = "AAA";

    for line in lines.1.lines() {
        let fullsplitline = line.split_once(" = ").unwrap();
        let entry = fullsplitline.0;
        let exit = fullsplitline.1.trim_matches(&['(', ')'][..]).split_once(", ").unwrap();
        nodes.insert(entry,exit);
    }

    let mut steps = 0;
    let mut directions = lines.0.chars().cycle();
    loop {
        if location == "ZZZ" {
            break
        }
        steps += 1;
        let rightorleft = directions.next().unwrap();
        location = match rightorleft {
            'R' => Ok(nodes.get(location).unwrap().1),
            'L' => Ok(nodes.get(location).unwrap().0),
            _ => Err("not right or left"),
        }?;
    };



    Ok(steps)
}