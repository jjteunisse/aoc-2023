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
    let max_red = 12;
    let max_green = 13;
    let max_blue = 14;

    let mut sum: u32 = 0;

    let input = read_to_string(INPUT)?;

    for line in input.lines() {
        let (first_part, second_part) = line.split_once(": ").unwrap();

        let (_, game_id) = first_part.split_once(" ").unwrap();

        let rolls: Vec<_> = second_part
            .split("; ")
            .map(|x| Roll::from_str(x).unwrap())
            .collect();

        let legal = rolls
            .iter()
            .all(|x| x.red <= max_red && x.green <= max_green && x.blue <= max_blue);

        if legal {
            let game_id: u32 = game_id.parse().unwrap();
            sum += game_id;
        }
    }

    Ok(sum)
}
