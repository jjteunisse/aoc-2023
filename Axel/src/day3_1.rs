use std::fs;

pub fn day3_1() -> Result<u32,String> {
    let mut total = 0;
    let contents = fs::read_to_string("inputs/day3")
        .expect("Should have been able to read the file");
    let mut field: [char;19600] = [',';19600];
    let mut fileiter = contents.chars();
    field = field.map(|_x| {
        let mut volgende = fileiter.next().unwrap();
        if volgende == '\n' {
            volgende = fileiter.next().unwrap();
        }
        volgende
    });

    //for kar in field {
    //    print!("{}",kar);
    //}

    let mut i = 0;
    while i<19600 {
        if field[i].is_numeric() {
            println!("{}",i);
            let mut machinepart = field[i].to_digit(10).unwrap();
            
            if field[i+1].is_numeric() {
                machinepart = machinepart * 10 + field[i+1].to_digit(10).unwrap();
                if field[i+2].is_numeric() {
                    machinepart = machinepart * 10 + field[i+2].to_digit(10).unwrap();
                    if haspart(field,3,i) {
                        println!("{}", machinepart);
                        total = total + machinepart;
                    }
                    i = i + 4;
                }else{
                    if haspart(field,2,i) {
                        println!("{}", machinepart);
                        total = total + machinepart;
                    }
                    i = i + 3;
                }
            }else{
                if haspart(field,1,i) {
                    println!("{}", machinepart);
                    total = total + machinepart;
                }
                i = i + 2;
            }

            println!("{}", machinepart);
        }else{
            i = i + 1;
        }
    }
    Ok(total)
}

fn haspart (field: [char;19600],mut lengte: usize, mut start: usize) -> bool {
    if start %140 == 0{
        start += 1;
        lengte -= 1;

    }else if !field[start-1].is_numeric() && field[start-1] != '.' {
        println!("{}", field[start-1]);
        return true;
    }
    if start+lengte %140 == 0{
        lengte -= 1;

    }else if !field[start+lengte].is_numeric() && field[start+lengte] != '.' {
        println!("{}", field[start+lengte]);
        return true;
    }
    if !(start < 140){
        for i in start-1-140..start+lengte-140+1{
            if !field[i].is_numeric() && field[i] != '.' {
                println!("{}", field[i]);
                return true;
            }
        }
    }
    if !(start > 19460){
        for i in start-1+140..start+lengte+140+1{
            if !field[i].is_numeric() && field[i] != '.' {
                println!("{}", field[i]);
                return true;
            }
        }
    }
    return false;
}

