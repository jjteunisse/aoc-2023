mod day1a;
// mod day1b;
mod day2a;
mod day2b;
mod day3a;
mod day3b;
mod day4a;
mod day4b;
mod day6a;
mod day6b;
use std::{env, process::exit};

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() <= 1 {
        println!("pls provide name");
        exit(1);
    }

    match args[1].as_str() {
        "day1a" => println!("{}", day1a::solve().unwrap()),
        // "day1b" => println!("{}", day1b::solve().unwrap()),
        "day2a" => println!("{}", day2a::solve().unwrap()),
        "day2b" => println!("{}", day2b::solve().unwrap()),
        "day3a" => println!("{}", day3a::solve().unwrap()),
        "day3b" => println!("{}", day3b::solve().unwrap()),
        "day4a" => println!("{}", day4a::solve().unwrap()),
        "day4b" => println!("{}", day4b::solve().unwrap()),
        "day6a" => println!("{}", day6a::solve().unwrap()),
        "day6b" => println!("{}", day6b::solve().unwrap()),
        _ => println!("unknown name"),
    }

    // match 

}
