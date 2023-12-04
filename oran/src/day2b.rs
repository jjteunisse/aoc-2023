use std::{fs::read_to_string, str::FromStr};

use anyhow::Result;

const INPUT: &str = "inputs/day2";

struct Roll {
    red: u32,
    blue: u32,
    green: u32,
}

#[derive(Debug)]
struct ParseRollError;

impl FromStr for Roll {
    type Err = ParseRollError;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        let colors = s.split(", ");
        let mut red = 0;
        let mut green = 0;
        let mut blue = 0;

        for c in colors {
            let (amt, color) = c.split_once(" ").unwrap();

            match color {
                "green" => green = amt.parse().unwrap(),
                "blue" => blue = amt.parse().unwrap(),
                "red" => red = amt.parse().unwrap(),
                _ => return Err(ParseRollError),
            }
        }
        Ok(Roll { red, blue, green })
    }
}

pub fn solve() -> Result<u32> {
    let input = read_to_string(INPUT)?;

    let sum = input
        .lines()
        .map(|line| {
            let (_, second_part) = line.split_once(": ").unwrap();

            let rolls: Vec<_> = second_part
                .split("; ")
                .map(|roll| Roll::from_str(roll).unwrap())
                .collect();

            let maxes = rolls.iter().fold((0, 0, 0), |acc, x| {
                (acc.0.max(x.red), acc.1.max(x.blue), acc.2.max(x.green))
            });

            maxes.0 * maxes.1 * maxes.2
        })
        .sum();

    Ok(sum)
}
