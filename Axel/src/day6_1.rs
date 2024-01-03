use std::fs;

pub fn day6_1() {
    let contents = fs::read_to_string("inputs/day6")
        .expect("Should have been able to read the file");
    let mut races = contents
        .split('\n')
        .map(|x| x.
            split_whitespace()
            .filter_map(|x| x
                .parse::<usize>().ok()
            )).collect::<Vec<_>>();
    
    races.pop();
    let table:Vec<_> = races.pop().unwrap().zip(races.pop().unwrap()).collect();
    let total:usize = table
        .iter()
        .map(|(x,y)| {
            let mut min = x/y;
            loop{
                if x < &((y-min)*min) {
                    break;
                }else{
                    min += 1;
                }
            }
            let mut max = *y;
            loop{
                if x < &((y-max)*max) {
                    break;
                }else{
                    max = max-1;
                }
            }
            max-min+1
        }).product();
    println!("{:?}",total);
}


//x  =   root(x53-313)
