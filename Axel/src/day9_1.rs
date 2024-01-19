use std::fs;

fn predict (row:&[isize]) -> Result<isize,String>  {
    if row.iter().all(|a| a == &0) {
        return Ok(0);
    }
    let mut nextrow:Vec<isize> = Vec::new();
    for (index,_oasisvalue) in row.iter().enumerate() {
        if index != 0 {
            nextrow.push(row[index]-row[index-1]);
        }
    }
    Ok(row.iter().last().unwrap() + predict(&nextrow)?)
}

pub fn day9_1() -> Result<isize,String> {
    let contents = fs::read_to_string("inputs/day9")
        .expect("Should have been able to read the file");
    let lines = contents.lines();
    let total = lines.map(|x| {
        let initrow:Vec<isize> = x
            .split(' ')
            .filter_map(|y| 
                y.parse::<isize>()
                .ok()
            ).collect();

        predict(&initrow)
        }).sum::<Result<isize,String>>()?;


    Ok(total)
}
