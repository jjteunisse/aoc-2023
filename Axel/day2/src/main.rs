use std::collections::VecDeque;
use std::fs;

enum Cubes {
    Red(u32),
    Blue(u32),
    Green(u32),
}

fn main() {
    let mut total = 0;
    let contents = fs::read_to_string("input")
        .expect("Should have been able to read the file");
    for line in contents.lines() {
        let mut v: VecDeque<&str> = line.split(&[',',':',';']).collect();
        v = v.iter().map(|z| z.trim()).collect();
        let gameid = v.pop_front().unwrap().trim_start_matches("Game ").parse::<i32>().unwrap();
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
        total += gameid;
        for kubus in kubusv {
            if 
                !match kubus {
                Cubes::Red(a) => if a < 13 {true}else{false},
                Cubes::Green(a) => if a < 14 {true}else{false},
                Cubes::Blue(a) => if a < 15 {true}else{false},
            }{

                println!("{} failed",gameid);
                total -= gameid;
                break;
            }else{
                println!("{} suceeded",gameid)
            }

        }
    }
    println!("{}",total);
}
