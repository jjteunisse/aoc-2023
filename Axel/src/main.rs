use std::env;

/*mod day1;
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
mod day8_1;
mod day8_2;
mod day9_1;
mod day9_2;*/
mod day10_1;
mod day10_2;



fn main() {
    let mut args: Vec<String> = env::args().collect();
    let arg:String;
    if args.len() == 1 {
        arg = "".to_string();
    }else{
        arg = args.pop().unwrap();
    }

   


    //usize
    let result:Result<_,_> = match arg.as_str() {
        //"1_2" => day1_2::day1_2(),
        //"4_1" => day4_1::day4_1(),
        //"4_2" => day4_2::day4_2(),
        //"6_1" => day6_1::day6_1(),
        //"6_2" => day6_2::day6_2(),
        //"7_1" => day7_1::day7_1(),
        //"7_2" => day7_2::day7_2(),
        //"8_1" => day8_1::day8_1(),
        //"8_2" => day8_2::day8_2(),
        "10_1" => day10_1::day10_1(),
        "10_2" => day10_2::day10_2(),
        _ => day10_2::day10_2(),
    };



    match result {
        Ok(x) => println!("{}",x),
        Err(err) => println!("{:?}", err),
    };
}