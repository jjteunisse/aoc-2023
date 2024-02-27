use std::error::Error;
use std::fs;

//const LINELEN:usize = 140;
const GALAXYEXPANSION:usize = 999999;


#[derive(Debug)]
struct Galaxy {
    x:usize,
    y:usize
}

fn abs_diff(a: usize, b: usize) -> usize {
    if a > b {
      a - b
    } else {
      b - a
    }
  }

pub fn day11_1() -> Result<usize, Box<dyn Error>> {
    let contents = fs::read_to_string("inputs/day11")
        .expect("Should have been able to read the file");

    let mut blanklines = 0;
    let countedlines:Vec<_> = contents.lines().enumerate().collect();
    let mut galaxys = Vec::new();
    for (y,line) in countedlines.into_iter() {
        if !line.contains('#'){
            blanklines += GALAXYEXPANSION;
        }
        for (x,c) in line.chars().enumerate() {
            match c == '#' {
                true => 
                    galaxys.push(
                        Galaxy{
                            x: x,
                            y: y + blanklines,
                        }
                    ),
                false => (),
            }
        }
    }

    galaxys.sort_by_key(|gal| gal.x);
    let mut blankcolums = 0;
    let mut last = 0;
    galaxys = galaxys.into_iter().map(|mut gal| {
        gal.x += blankcolums;
        let diff = gal.x-last;
        if (diff) > 1 {
            blankcolums += (diff-1)*GALAXYEXPANSION;
            gal.x += (diff-1)*GALAXYEXPANSION
        }
        last = gal.x;
        gal
    }).collect();

    let mut total = 0;

    for (x,gal1) in galaxys.iter().enumerate() {
        for gal2 in &galaxys[x+1..] {
            let len = abs_diff(gal1.x,gal2.x) + abs_diff(gal1.y,gal2.y);
            total += len;
        }
    }
    
    Ok(total)
}