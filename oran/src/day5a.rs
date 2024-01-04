use std::{fs::read_to_string, ops::Range, str::FromStr};

use anyhow::{anyhow, Result};
use scan_fmt::scan_fmt;

const INPUT: &str = "inputs/day5";

#[derive(Debug)]
struct Input {
    seeds: Vec<i64>,
    modifications: Vec<Modifications>,
}

#[derive(Debug)]
struct Modifications {
    maps: Vec<Maps>,
}

#[derive(Debug)]
struct Maps {
    range: Range<i64>,
    modifyer: i64,
}

impl FromStr for Modifications {
    type Err = anyhow::Error;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        let mut lines = s.lines();
        let _ = lines.next(); // ignore the name

        let mut maps = vec![];

        for line in lines {
            let (dest, source, length) = scan_fmt!(line, "{} {} {}", i64, i64, i64)?;
            let modifyer = dest - source;
            let range = source..source + length;

            maps.push(Maps { range, modifyer });
        }

        Ok(Modifications { maps })
    }
}

fn parse_input() -> Result<Input> {
    let input = read_to_string(INPUT)?;

    let mut mappers = vec![];

    let (seeds, rest) = input.split_once("\n\n").ok_or(anyhow!("no seeds found"))?;
    let seeds = seeds
        .split(": ")
        .skip(1)
        .next()
        .ok_or(anyhow!("wrong seed format"))?;
    let seeds: Vec<i64> = seeds
        .to_string()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let chunks = rest.split("\n\n");

    for chunk in chunks {
        mappers.push(Modifications::from_str(chunk)?);
    }

    Ok(Input {
        seeds,
        modifications: mappers,
    })
}

pub fn solve() -> Result<i64> {
    let input = parse_input().unwrap();
    let mut seeds = input.seeds;

    for mods in input.modifications {
        for seed in seeds.iter_mut() {
            for map in &mods.maps {
                if map.range.contains(seed) {
                    *seed = *seed + map.modifyer;
                    break;
                }
            }
        }
    }

    Ok(seeds.into_iter().min().ok_or(anyhow!("no seeds found"))?)
}
