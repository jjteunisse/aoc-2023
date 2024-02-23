use std::fs;
use std::error::Error;

#[derive(Debug)]
struct Pipegrid {
    pipes:Vec<Pipe>,
    width:usize,
    heigth:usize,
}

impl Pipegrid {
    fn find_con (&self, pos:usize) -> Option<usize> {
        let mut outgoing:Vec<Connection> = Vec::new();
        match &self.pipes[pos] {
            Pipe::Connections(x,y) => outgoing = vec![*x,*y],
            Pipe::Start => outgoing = vec![Connection::Up,Connection::Down,Connection::Left,Connection::Right],
            Pipe::Nocons => println!("{}", "should never start looking from no cons"),
        }
        
        for out in outgoing.iter() {
            match out {
                Connection::Up => if match_connections(&self.pipes[pos-self.width],Connection::Down) {
                                        return Some(pos-self.width);},
                Connection::Down => if match_connections(&self.pipes[pos+self.width],Connection::Up) {
                                        return Some(pos+self.width);},
                Connection::Left => if match_connections(&self.pipes[pos-1],Connection::Right) {
                                        return Some(pos-1);},
                Connection::Right => if match_connections(&self.pipes[pos+1],Connection::Left) {
                                        return Some(pos+1);},
            }
        }
        
    
        None
    }
}



fn match_connections (inc: &Pipe, out:Connection) -> bool {
    match inc {
        Pipe::Connections(x,y) => [x,y].contains(&&out),
        Pipe::Start => true,
        Pipe::Nocons => false,
    }
}

#[derive(Eq, PartialEq, Debug)]
enum Pipe {
    Connections(Connection,Connection),
    Start,
    Nocons,
}

#[derive(Eq, PartialEq, Debug, Clone, Copy)]
enum Connection {
    Up,
    Down,
    Left,
    Right,
}

pub fn day10_1() -> Result<usize,Box<dyn Error>> {
    let contents = fs::read_to_string("inputs/day10")
        .expect("Should have been able to read the file");

    let grid = Pipegrid {
        heigth:contents.lines().count(),
        width:contents.lines().next().unwrap().chars().count(),
        pipes:{
            let tempvec = contents.chars()
                .filter_map(|x|
                    match x {
                        '\n' => None,
                        '.' => Some(Pipe::Nocons),
                        '-' => Some(Pipe::Connections(Connection::Left,Connection::Right)),
                        '|' => Some(Pipe::Connections(Connection::Up,Connection::Down)),
                        'F' => Some(Pipe::Connections(Connection::Down,Connection::Right)),
                        'J' => Some(Pipe::Connections(Connection::Up,Connection::Left)),
                        '7' => Some(Pipe::Connections(Connection::Down,Connection::Left)),
                        'L' => Some(Pipe::Connections(Connection::Up,Connection::Right)),
                        'S' => Some(Pipe::Start),
                        _ => {println!("unexpected char in input");None},
                    }
                
                ).collect();
            tempvec
        }
    };

    let start = grid.pipes.iter().position(|x| x == &Pipe::Start).unwrap();
    let mut pos = 0;
    println!("{:?}", grid.pipes[start]);
    println!("{:?}", start);
    match grid.find_con(start) {
        Some(x) => pos = x,
        None => println!("{}", "???"),
    }
    let mut entered = Connection::Up;

    let mut len = 1;
    loop{
        println!("{:?}", grid.pipes[pos]);
        println!("{:?}", pos);
        match &grid.pipes[pos] {
            Pipe::Connections(x,y) => {
                let direction = [x,y].into_iter().find(|x| *x != &entered).unwrap();
                match direction {
                    Connection::Up => {pos = pos - grid.heigth; entered = Connection::Down},
                    Connection::Down => {pos = pos + grid.heigth; entered = Connection::Up},
                    Connection::Left => {pos -=1; entered = Connection::Right},
                    Connection::Right => {pos += 1; entered = Connection::Left},
                }
            }
            _ => println!("{}","zz"),
        }

        println!("{:?}", grid.pipes[pos]);
        len += 1;
        println!("{:?}", len);
        if grid.pipes[pos] == Pipe::Start {
            break;
        }

    }
    


    Ok(len/2)
}