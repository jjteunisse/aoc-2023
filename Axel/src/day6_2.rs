use std::fs;

pub fn day6_2() {
    let contents = fs::read_to_string("inputs/day6")
        .expect("Should have been able to read the file");
    let mut races = contents
        .split('\n')
        .filter_map(|x| x
            .chars()
            .filter(|x| x.is_numeric()).collect::<String>()
            .parse::<usize>().ok()
        ).collect::<Vec<_>>();
        
    let table:Vec<_> = vec![(races.pop().unwrap(),races.pop().unwrap())];
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
