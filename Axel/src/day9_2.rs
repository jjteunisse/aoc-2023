use std::fs;

fn predict (row: &mut [isize]) -> Result<isize,String>  {
    if row.iter().all(|a| a == &0) {
        return Ok(0);
    }
    println!("{:?}", row);
    let mut temp1 = None;
    let mut temp2;
    for index in 0..row.len() {
        if index < row.len()-1 {
            temp2 = temp1;
            temp1 = Some(row[index+1]-row[index]);
            if temp2 != None {
                row[index] = temp2.unwrap();
            }
        }
    }
    row[row.len()-1] = temp1.unwrap();
    Ok(row[0] - predict(&mut row[1..])?)
}

pub fn day9_2() -> Result<isize,String> {
    let contents = fs::read_to_string("inputs/day9")
        .expect("Should have been able to read the file");
    let lines = contents.lines();
    let total = lines.map(|x| {
        let mut initrow:Vec<isize> = x
            .split(' ')
            .filter_map(|y| 
                y.parse::<isize>()
                .ok()
            ).collect();

        predict(&mut initrow)
        }).sum::<Result<isize,String>>()?;


    Ok(total)
}
