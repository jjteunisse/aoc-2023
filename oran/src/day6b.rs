use anyhow::Result;
use roots::{find_roots_quadratic, Roots};

pub fn solve() -> Result<u32> {
    let time = 54708275i64;
    let dist = 239114212951253i64;

    // total traveled distance: D =  x * (t - x)
    // where variable x is the time waited in milliseconds
    // rewritten to quadratic equation 0 = x^2 - tx + D

    if let Roots::Two([a, b]) = find_roots_quadratic(1f64, -time as f64, dist as f64) {
        Ok((b.floor() as u32) - (a.ceil() as u32) + 1)
    } else {
        panic!("not supposed to occur");
    }
}
