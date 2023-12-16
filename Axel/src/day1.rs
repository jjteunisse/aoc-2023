use std::fs;

pub fn day1() {
    println!("Hello, world!");
    let contents = fs::read_to_string("inputs/day1")
        .expect("Should have been able to read the file");
    let lineiter = contents.split_ascii_whitespace();
    let mut total = 0;
    for line in lineiter {
        let mut firstfound = false;
        let mut laatste = 0;
        for b in line.chars() {
            if firstfound == false {
                if b.is_numeric(){
                    total = total + 10*b.to_digit(10).unwrap();
                    laatste = b.to_digit(10).unwrap();
                    firstfound = true;
                }

            }else{
                if b.is_numeric(){
                    laatste = b.to_digit(10).unwrap();
                }
            }
        }
        total = laatste + total;
    }
    println!("{}",total);
    //println!("{}",contents);
}
