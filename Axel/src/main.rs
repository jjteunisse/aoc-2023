use std::env;

mod day1;
mod day1_2;
mod day2_1;
mod day2;
mod day3;
mod day3_1;
mod day4_1;
mod day4_2;
mod day5_2;
mod day6_1;
mod day6_2;
mod day7_1;
mod day7_2;



fn main() {
    let mut args: Vec<String> = env::args().collect();
    let arg:String;
    if args.len() == 1 {
        arg = "".to_string();
    }else{
        arg = args.pop().unwrap();
    }

    //u32
    let _result:Result<_,_> = match arg.as_str() {
        "1" => day1::day1(),
        "2_1" => day2_1::day2_1(),
        "3" => day3::day3(),
        "3_1" => day3_1::day3_1(),
        _ => Err("no u32 fn found".to_string()),
    };


    //usize
    let result2:Result<_,_> = match arg.as_str() {
        "1_2" => day1_2::day1_2(),
        "4_1" => day4_1::day4_1(),
        "4_2" => day4_2::day4_2(),
        "6_1" => day6_1::day6_1(),
        "6_2" => day6_2::day6_2(),
        "7_1" => day7_1::day7_1(),
        "7_2" => day7_2::day7_2(),
        _ => day7_2::day7_2(),
    };

    //isize
    let _result3:Result<_,_> = match arg.as_str() {
        "5_2" => day5_2::day5_2(),
        _ => Err("no isize fn found".to_string()),
    };

    //i32
    let _result3:Result<_,_> = match arg.as_str(){
        "2" => day2::day2(),
        _ => Err("no i32 fn found".to_string()),
    };

    match result2 {
        Ok(x) => println!("{}",x),
        _ => println!("{}", "ye"),
    };
}