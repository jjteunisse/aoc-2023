use anyhow::Result;
use roots::{find_roots_quadratic, Roots};

pub fn solve() -> Result<u32> {
    let times = vec![54, 70, 82, 75];
    let distances = vec![239, 1142, 1295, 1253];

    let combined = times.iter().zip(distances.iter());

    // total traveled distance: D =  x * (t - x)
    // where variable x is the time waited in milliseconds
    // rewritten to quadratic equation 0 = x^2 - tx + D

    let product = combined
        .into_iter()
        .map(|(time, dist)| {
            if let Roots::Two([a, b]) = find_roots_quadratic(1f32, -*time as f32, *dist as f32) {
                (b.floor() as u32) - (a.ceil() as u32) + 1
            } else {
                panic!("not supposed to occur");
            }
        })
        .product();

    Ok(product)
}
