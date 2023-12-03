use std::collections::VecDeque;
use std::fs;

const NUMBIES: [&str;9] = ["one","two","three","four","five","six","seven","eight","nine"];

fn main() {
    let contents = fs::read_to_string("input")
        .expect("Should have been able to read the file");
    let lineiter = contents.split_ascii_whitespace();
    let mut total:usize = 0;
    for line in lineiter {
        let mut v: VecDeque<&str> = line.split_inclusive(char::is_numeric).collect();
        if v.len() == 1{
            let lonelystr = v.pop_front().unwrap();
            total = total + eval1lang(lonelystr);
        }else {
            let uiteinde = match v.pop_back() {
                Some(v) => v,
                None => "",
            };
            if !uiteinde.contains(char::is_numeric) {
                let numbie = rcheck_numbers(uiteinde);
                if numbie == 0{
                    if v.len() == 1{
                        total = total + eval1lang(v.pop_back().unwrap());
                        continue;
                    }else{
                        let temp:usize = v.pop_back().unwrap().chars().last().unwrap().to_digit(10).unwrap().try_into().unwrap();
                        total = total + temp;
                    }
                }else{
                    total = total + numbie;
                }
            }else{
                let temp:usize = uiteinde.chars().last().unwrap().to_digit(10).unwrap().try_into().unwrap();
                total = total + temp;
            }
            let begin = v.pop_front().unwrap();
            let nummer = check_numbers(begin);
            if nummer == 0{
                let temp:usize = begin.chars().last().unwrap().to_digit(10).unwrap().try_into().unwrap();
                total = total + temp*10;
            }else{
                total = total + nummer*10;
            }
        }
    }
    println!("{}",total);
}

fn eval1lang(begineneind: &str) -> usize {
    if !begineneind.contains(char::is_numeric){
        return check_numbers(begineneind) * 10 + rcheck_numbers(begineneind);
    }else{
        let nummer = check_numbers(begineneind);
        if nummer == 0{
            let temp:usize = begineneind.chars().last().unwrap().to_digit(10).unwrap().try_into().unwrap();
            return temp*11;
        }else{
            let temp:usize = begineneind.chars().last().unwrap().to_digit(10).unwrap().try_into().unwrap();
            return nummer*10 + temp;
        }
    }
}

fn rcheck_numbers(uiteinde: &str) -> usize {
    let mut count = 0;
    let mut realnumbie = 0;
    let mut last_numbie = 0;
    for i in NUMBIES {
        count = count + 1;
        let x = match uiteinde.rfind(i){
            Some(v) => v+1,
            None => 0,
        };
        if x > last_numbie{
            realnumbie = count;
            last_numbie = x;
        }
    }
    return realnumbie;
}

fn check_numbers(begin: &str) -> usize {
    let mut count = 0;
    let mut realnumbie = 0;
    let mut last_numbie = begin.len();
    for i in NUMBIES {
        count = count + 1;
        let x = match begin.find(i){
            Some(v) => v+1,
            None => begin.len(),
        };
        if x < last_numbie.try_into().unwrap(){
            realnumbie = count;
            last_numbie = x;
        }
    }
    return realnumbie.try_into().unwrap();
}
