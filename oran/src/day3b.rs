use std::{fs::read_to_string, ops::Range, str::FromStr};

use anyhow::Result;

const INPUT: &str = "inputs/day3";

#[derive(Debug)]
struct Matrix {
    length: usize,
    inner: Vec<Vec<Item>>,
}

#[derive(Debug, PartialEq, Eq)]
enum Item {
    Number(u32),
    Gear,
    Empty,
}

impl Matrix {
    fn get_clusters(&self) -> Vec<Cluster> {
        let mut res = vec![];
        for (i, row) in self.inner.iter().enumerate() {
            let mut cur: Option<(usize, u32)> = None;

            for (j, item) in row.iter().enumerate() {
                match (cur, item) {
                    (None, Item::Number(n)) => cur = Some((j, *n)),
                    (Some((begin, c)), Item::Number(n)) => cur = Some((begin, c * 10 + n)),
                    (Some((begin, c)), _) => {
                        res.push(Cluster {
                            number: c,
                            col_range: begin..j,
                            row: i,
                        });
                        cur = None;
                    }
                    _ => (),
                }
            }
            if let Some((begin, c)) = cur {
                res.push(Cluster {
                    number: c,
                    col_range: begin..self.length,
                    row: i,
                })
            }
        }
        res
    }

    fn get_gears(&self) -> Vec<(usize, usize)> {
        let mut res = vec![];

        for (i, row) in self.inner.iter().enumerate() {
            for (j, item) in row.iter().enumerate() {
                if item == &Item::Gear {
                    res.push((i, j));
                }
            }
        }
        res
    }

    fn get_gear_ratio(&self) -> u32 {
        let clusters = self.get_clusters();
        let gears = self.get_gears();

        gears
            .into_iter()
            .map(|gear| {
                let gear_row_range = (gear.0 - 1)..=(gear.0 + 1);
                let gear_col_range = (gear.1 - 1)..=(gear.1 + 1);

                let clusters_in_range: Vec<Cluster> = clusters
                    .clone()
                    .into_iter()
                    .filter(|cluster| {
                        let row_in_range = gear_row_range.contains(&cluster.row);
                        let col_in_range = cluster
                            .col_range
                            .clone()
                            .any(|x| gear_col_range.contains(&x));

                        row_in_range && col_in_range
                    })
                    .collect();

                if clusters_in_range.len() == 2 {
                    clusters_in_range
                        .into_iter()
                        .map(|c| c.number)
                        .product::<u32>()
                } else {
                    0
                }
            })
            .sum()
    }
}

#[derive(Debug, Clone)]
struct Cluster {
    number: u32,
    col_range: Range<usize>,
    row: usize,
}

impl FromStr for Matrix {
    type Err = anyhow::Error;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        let mut length = None;
        let mut inner: Vec<Vec<Item>> = vec![];

        for line in s.lines() {
            match length {
                Some(len) => assert!(line.len() == len),
                None => length = Some(line.len()),
            }

            inner.push(
                line.chars()
                    .map(|chr| match chr {
                        c if c.is_numeric() => Item::Number(c.to_digit(10).unwrap()),
                        '.' => Item::Empty,
                        _ => Item::Gear,
                    })
                    .collect(),
            );
        }

        Ok(Matrix {
            length: length.unwrap(),
            inner,
        })
    }
}

fn parse_input() -> Result<Matrix> {
    let input = read_to_string(INPUT)?;

    let matrix = Matrix::from_str(&input)?;

    Ok(matrix)
}

pub fn solve() -> Result<u32> {
    let matrix = parse_input()?;

    let ratio = matrix.get_gear_ratio();

    Ok(ratio)
}
