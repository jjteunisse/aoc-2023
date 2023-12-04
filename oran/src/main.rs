mod day1a;
// mod day1b;
mod day2a;
mod day2b;
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
        _ => println!("unknown name"),
    }

    // match 

}
