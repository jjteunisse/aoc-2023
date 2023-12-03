use std::{collections::HashMap, fs::read_to_string};

use anyhow::Result;
use onig::Regex;

const INPUT: &str = "inputs/day1";
const REGEX: &str = r"([1-9]|one|two|three|four|five|six|seven|eight|nine)";

pub fn solve() -> Result<u32> {
    let map: HashMap<&str, u32> = HashMap::from([
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ]);

    let re_non_consuming = Regex::new(format!(r"(?={})", REGEX).as_str()).unwrap();
    let re_consuming = Regex::new(REGEX).unwrap();

    let input = read_to_string(INPUT)?;

    let result: u32 = input
        .lines()
        .map(|line| {
            let res: Vec<_> = re_non_consuming
                .find_iter(line)
                .map(|(i, _)| match line.chars().nth(i).unwrap().to_digit(10) {
                    Some(digit) => digit,
                    None => {
                        let (_, j) = re_consuming.find(&line[i..]).unwrap();

                        *map.get(&line[i..i + j]).unwrap()
                    }
                })
                .collect();

            let first = res.first().unwrap();
            let last = res.last().unwrap();

            first * 10 + last
        })
        .sum();
    Ok(result)
}
