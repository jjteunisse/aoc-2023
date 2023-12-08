use std::{collections::HashSet, fs::read_to_string, ops::Range, str::FromStr};

use anyhow::Result;

const INPUT: &str = "inputs/day4";

#[derive(Debug)]
struct Game {
    winning: HashSet<u32>,
    numbers: HashSet<u32>,
}

impl FromStr for Game {
    type Err = anyhow::Error;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        let cardgame = s.split(": ").skip(1).next().unwrap();

        let mut cardgame = cardgame.split(" | ");
        let winning = cardgame.next().unwrap();
        let numbers = cardgame.next().unwrap();

        let winning: HashSet<u32> = winning
            .split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();
        let numbers: HashSet<u32> = numbers
            .split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();

        Ok(Game { winning, numbers })
    }
}

fn parse_input() -> Result<Vec<Game>> {
    let input = read_to_string(INPUT)?;

    Ok(input
        .lines()
        .map(|line| Game::from_str(line).unwrap())
        .collect())
}

pub fn solve() -> Result<u32> {
    let cards = parse_input()?;

    let count = cards
        .into_iter()
        .map(|card| {
            let matches = card.winning.intersection(&card.numbers).count() as u32;

            match matches {
                0 => 0,
                _ => 2u32.pow(matches - 1),
            }
        })
        .sum();

    Ok(count)
}
