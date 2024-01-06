use std::collections::VecDeque;
use std::fs;
use std::ops::Add;

#[derive(Debug)]
struct Scratchcard{
    win_num:Vec<u32>,
    your_num:Vec<u32>,
    copies:usize,
}

impl Scratchcard{
    fn calc_total(&mut self) -> usize {
        let mut num_found = 0;
        for i in &self.win_num {
            match self.your_num.iter().position(|x| i == x) {
                Some(x) => {self.your_num.swap_remove(x); num_found += 1},
                None => (),
            }
        }
        num_found
    }
}

pub fn day4_2() -> Result<usize,String> {
    let contents = fs::read_to_string("inputs/day4")
        .expect("Should have been able to read the file");
    let cards:Vec<Scratchcard> = contents.lines().map(|line| {
        let splitline = line.split_once('|').unwrap();
        Scratchcard{
            win_num: splitline.0.split(' ').filter_map(|s| s.parse::<u32>().ok()).collect(),
            your_num: splitline.1.split(' ').filter_map(|s| s.parse::<u32>().ok()).collect(),
            copies: 1,
        }
    }).collect();
    //let total:usize = cards.iter().filter_map(|mut x| x.calc_total()).sum();
    let mut total = 0;
    let mut copies = VecDeque::from([0]);
    for mut i in cards {
        match copies.pop_front() {
            Some(x) => i.copies += x,
            None => (),
        }
        let dingengev = i.calc_total();
        let mut counter = 0;
        for j in copies.iter_mut() {
            if counter < dingengev {
                *j = j.add(i.copies);
            }
            counter += 1;

        }
        while copies.len() < dingengev {
            copies.push_back(i.copies);
        }
        //copies = copies.iter().map(|&x| x = x + 1).collect();
        total += i.copies;
    }
    Ok(total)
}
