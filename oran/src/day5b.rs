use std::{fs::read_to_string, ops::Range, str::FromStr, collections::HashMap};

use anyhow::{anyhow, Result};
use scan_fmt::scan_fmt;

const INPUT: &str = "inputs/day5";

#[derive(Debug)]
struct Input {
    seeds: Vec<Range<i64>>,
    modifications: Vec<ModificationList>,
}

#[derive(Debug)]
struct ModificationList {
    sections: Vec<CustomRangeWithModifier>,
}

#[derive(Debug)]
struct CustomRangeWithModifier {
    range: Range<i64>,
    modifyer: i64,
}

impl FromStr for ModificationList {
    type Err = anyhow::Error;

    fn from_str(s: &str) -> std::result::Result<Self, Self::Err> {
        let mut lines = s.lines();
        let _ = lines.next(); // ignore the name

        let mut sections = vec![];

        for line in lines {
            let (dest, source, length) = scan_fmt!(line, "{} {} {}", i64, i64, i64)?;
            let modifyer = dest - source;
            let range = source..source + length;

            sections.push(CustomRangeWithModifier { range, modifyer });
        }

        sections.sort_by_key(|m| m.range.start);

        Ok(ModificationList { sections })
    }
}

fn parse_input() -> Result<Input> {
    let input = read_to_string(INPUT)?;

    let mut mappers = vec![];

    let (seeds, rest) = input.split_once("\n\n").ok_or(anyhow!("no seeds found"))?;
    let (_, seeds) = seeds
        .split_once(": ")
        .ok_or(anyhow!("wrong seed format"))?;

    let seeds: Vec<i64> = seeds
        .to_string()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let seeds: Vec<Range<i64>> = seeds.chunks(2).map(|chunk| chunk[0]..chunk[0]+chunk[1]).collect();


    let chunks = rest.split("\n\n");

    for chunk in chunks {
        mappers.push(ModificationList::from_str(chunk)?);
    }

    Ok(Input {
        seeds,
        modifications: mappers,
    })
}

pub fn solve() -> Result<i64> {
    let input = parse_input().unwrap();
    let mut seedranges = input.seeds;

    for mods in input.modifications {
        let sections = mods.sections;
        // note: sections are sorted by start of range

        let mut new_seed_ranges = vec![];
        for seedrange in seedranges {
            let mut curr = seedrange.start;

            for section in sections.iter() {
                // this section is only relevant it it's within seed range
                if section.range.start < seedrange.end {
                    let end = seedrange.end.min(section.range.end);

                    // if the seed range starts before this section, 
                    // leave all seeds until the start of this range untouched
                    if curr < section.range.start {
                        new_seed_ranges.push(curr..section.range.start);
                        curr = section.range.start;
                    }

                    // the overlap between the seed range and the section
                    if curr < section.range.end {
                        let modifyer = section.modifyer;
                        new_seed_ranges.push(curr+modifyer..end+modifyer);
                        curr = end;
                    }

                    // leave everything after the end of this section untouched (might be picked up by the next section)
                } else {
                    // this section is after seed range, but there may be some residue curr..seedrange_end
                    if curr < seedrange.end {
                        new_seed_ranges.push(curr..seedrange.end);
                        break;
                    }
                }
            }
            let seedrange_start = seedrange.start;
            let seedrange_end = seedrange.end;

            // after we have gone through all the sections, we need to add [last_section_end..seedrange_end]
            let last_section_end = sections.last().unwrap().range.end;
            if last_section_end < seedrange_end {
                //also handle special case: seed range is after every section
                let min = last_section_end.max(seedrange_start);
                new_seed_ranges.push(min..seedrange_end);
            }
        }
        seedranges = new_seed_ranges;
    }

    Ok(seedranges.into_iter().map(|r| r.start).min().unwrap())
}
