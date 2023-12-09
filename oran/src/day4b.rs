use std::{collections::HashSet, fs::read_to_string, str::FromStr};

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

    let mut amounts = vec![1; cards.len()];

    for (i, card) in cards.iter().enumerate() {
        let count = amounts.get(i).unwrap().clone();

        let matches = card.winning.intersection(&card.numbers).count();

        for i in i + 1..i + matches + 1 {
            if let Some(elem) = amounts.get_mut(i) {
                *elem += count;
            }
        }
    }

    let res = amounts.iter().sum();

    Ok(res)
}
