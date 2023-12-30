use std::fs;

#[derive(Debug)]
struct Scratchcard{
    win_num:Vec<u32>,
    your_num:Vec<u32>,

}

impl Scratchcard{
    fn calc_total(&mut self) -> Option<usize> {
        let mut num_found = 0;
        for i in &self.win_num {
            match self.your_num.iter().position(|x| i == x) {
                Some(x) => {self.your_num.swap_remove(x); num_found += 1},
                None => (),
            }
        }
        if num_found > 0 {
            Some(2_usize.pow(num_found-1))
        }else{
            None
        }
    }
}

pub fn day4_1() {
    let contents = fs::read_to_string("inputs/day4")
        .expect("Should have been able to read the file");
    let cards:Vec<Scratchcard> = contents.lines().map(|line| {
        let splitline = line.split_once('|').unwrap();
        Scratchcard{
            win_num: splitline.0.split(' ').filter_map(|s| s.parse::<u32>().ok()).collect(),
            your_num: splitline.1.split(' ').filter_map(|s| s.parse::<u32>().ok()).collect(),
        }
    }).collect();
    //let total:usize = cards.iter().filter_map(|mut x| x.calc_total()).sum();
    let mut total = 0;
    for mut i in cards {
        match i.calc_total() {
            Some(x) => total += x,
            None => (),
        }
    }
    println!("{}",total);
}
