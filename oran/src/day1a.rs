use std::fs::read_to_string;

use anyhow::Result;

const INPUT: &str = "inputs/day1";

pub fn solve() -> Result<u32> {

    let input = read_to_string(INPUT)?;

    let result: u32 = input.lines().map(|line| {
        let digits: Vec<_> = line.chars().filter_map(|c| c.to_digit(10)).collect();

        assert!(digits.len() > 0);

        let first = digits.first().unwrap();
        let last = digits.last().unwrap();

        first * 10 + last
    }).sum();

    Ok(result)
}
