use std::collections::VecDeque;
use std::fs;

enum Cubes {
    Red(u32),
    Blue(u32),
    Green(u32),
}

pub fn day2_1() {
    let mut total = 0;
    let contents = fs::read_to_string("inputs/day2")
        .expect("Should have been able to read the file");
    for line in contents.lines() {
        let mut v: VecDeque<&str> = line.split(&[',',':',';']).collect();
        v = v.iter().map(|z| z.trim()).collect();
        let _gameid = v.pop_front().unwrap().trim_start_matches("Game ").parse::<i32>().unwrap();
        let kubusv:Vec<Cubes> = v.iter().map(|z| {
            let mut pair:VecDeque<&str> = z.split(' ').collect();
            let number = pair.pop_front().unwrap().parse::<u32>().unwrap();
            let color = match pair.pop_back().unwrap(){
                "red" => Cubes::Red(number),
                "blue" => Cubes::Blue(number),
                "green" => Cubes::Green(number),
                _ => Cubes::Green(number),
            };
            color
        }).collect();
        let mut redmin = 0;
        let mut greenmin = 0;
        let mut bluemin = 0;
        println!("{}", "newline:");
        for kubus in kubusv {
            match kubus {
                Cubes::Red(a) => if a > redmin {redmin = a},
                Cubes::Green(a) => if a > greenmin {greenmin = a},
                Cubes::Blue(a) => if a > bluemin {bluemin = a},
            }
            println!("{}", redmin * greenmin * bluemin);
        }
        total = total + redmin * greenmin * bluemin;
    }
    println!("{}",total);
}
