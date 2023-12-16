

use std::fs;

pub fn day3() {
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
        if field[i] == '*' {
            let mut v = Vec::new();
            if i > 139 {
                v = matchem(derive_number_mid(field, i-140),v);
                if v.len() == 0 {
                    v = matchem(derive_number_left(field, i-140-1),v);
                    v = matchem(derive_number_right(field, i-140+1),v);
                }
            }
            if i < 19460 {
                let veclen = v.len();
                v = matchem(derive_number_mid(field, i+140),v);
                if veclen == v.len() {
                    v = matchem(derive_number_left(field, i+140-1),v);
                    v = matchem(derive_number_right(field, i+140+1),v);
                }
            }
            v = matchem(derive_number_left(field, i-1),v);
            v = matchem(derive_number_right(field, i+1),v);
            println!("{:?}", v);
            if v.len() >= 2 {
                //print!("{:?}", v);
                let mulp = v.pop().unwrap() * v.pop().unwrap();

                //println!("{:?}", mulp);
                total += mulp;
            }
        }
        i = i + 1;

        /*if field[i].is_numeric() {
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
        }*/
    }
    println!("{}", total);
}

/*fn haspart (field: [char;19600],mut lengte: usize, mut start: usize) -> bool {
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
}*/


fn derive_number_left (field: [char;19600], mut start: usize) -> Option<u32> {
    while field[start].is_numeric(){
        start -= 1;
    }
    derive_number_right(field,start+1)
}

fn derive_number_right (field: [char;19600], mut start: usize) -> Option<u32> {
    let mut number = 0;
    while field[start].is_numeric(){
        number = 10 * number + field[start].to_digit(10).unwrap();
        start += 1;
    }
    if number > 0 {
        Some(number)
    }else{
        None
    }
}

fn derive_number_mid (field: [char;19600], start: usize) -> Option<u32> {
    if !field[start].is_numeric() {
        None
    }else if field[start-1].is_numeric(){
        derive_number_left(field,start)
    }else{
        derive_number_right(field,start)
    }
}

fn matchem (avar:Option<u32>, mut v:Vec<u32>) -> Vec<u32>{
    match avar {
        Some(x) => {v.push(x);/*println!("{}",x)*/},
        None => (),
    }
    return v;
}