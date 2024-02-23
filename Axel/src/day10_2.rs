use std::fs;
use std::error::Error;

#[derive(Debug)]
struct Nodegrid {
    nodes:Vec<Node>,
    width:usize,
    heigth:usize,
}

impl Nodegrid {
    fn find_con (&self, pos:usize, momentum:usize) -> Result<(usize,usize), Box<dyn Error>> {
        let calc_pos = |positie:usize, side:usize| -> usize {
            match side {
                0 => positie + self.width,
                1 => positie - self.width,
                2 => positie + 1,
                3 => positie - 1,
                _ => positie,
            }
        };
        if let NodeType::Pipe(x) = &self.nodes[pos].nodetype {
            for side in x.iter().enumerate() {
                if side.1 == &SideType::Connection && side.0 != momentum {
                    if side.0 % 2 == 1 {
                        return Ok((calc_pos(pos,side.0 - 1),side.0 - 1))
                    }else{
                        return Ok((calc_pos(pos,side.0 + 1),side.0 + 1))
                    }
                };
            };
        }else if &self.nodes[pos].nodetype == &NodeType::Start {

            return Ok((calc_pos(pos,0),0));
        }else{
            return Err("Error: not a pipe or start?".into());
        }
        Err("Error: no connection found".into())
    }

    fn from_str(input:&str) -> Self {
        let nodes:Vec<Node> = input.chars()
            .filter_map(|x| {
                let nodesymbol = match x {
                    '\n' => None,
                    '.' => Some(NodeType::Empty),
                    '-' => Some(NodeType::Pipe([SideType::Outside,
                                            SideType::Outside,SideType::Connection,
                                            SideType::Connection])),
                    '|' => Some(NodeType::Pipe([SideType::Connection,
                                            SideType::Connection,SideType::Outside,
                                            SideType::Outside])),
                    'F' => Some(NodeType::Pipe([SideType::Outside,
                                            SideType::Connection,SideType::Outside,
                                            SideType::Connection])),
                    'J' => Some(NodeType::Pipe([SideType::Connection,
                                            SideType::Outside,SideType::Connection,
                                            SideType::Outside])),
                    '7' => Some(NodeType::Pipe([SideType::Outside,
                                            SideType::Connection,SideType::Connection,
                                            SideType::Outside])),
                    'L' => Some(NodeType::Pipe([SideType::Connection,
                                            SideType::Outside,SideType::Outside,
                                            SideType::Connection])),
                    'S' => Some(NodeType::Start),
                    _ => {println!("unexpected char in input");None},
                };
                match nodesymbol {
                    Some(x) => Some(Node {
                                    nodetype: x,
                                    tunnelpart: false,
                                }),
                    None => None,
                }
            }).collect();
        
        Nodegrid {
            nodes:nodes,
            heigth:input.lines().count(),
            width:input.lines().next().unwrap().chars().count(),
        }
    }

    fn countspace(&mut self, pos:usize) -> usize {
        if pos >= self.width * self.heigth {
            return 0
        }else if self.nodes[pos].tunnelpart == false && self.nodes[pos].nodetype != NodeType::Counted {
            self.nodes[pos].nodetype = NodeType::Counted;
            let mut bovensterij = 0;
            let mut topleft = 0;
            if pos > self.width {
                bovensterij = self.countspace(pos-self.width);
            }
            if pos != 0 {
                topleft = self.countspace(pos - 1);
            }
            return 1 + 
                self.countspace(pos + 1) + 
                topleft + 
                self.countspace(pos + self.width) + 
                bovensterij;
        }else{
            return 0;
        }
    }

    fn getright(&mut self, pos:usize, enteredfrom:usize) -> usize {
        if let NodeType::Pipe(x) = &self.nodes[pos].nodetype {
            match Nodegrid::l_or_rturn(enteredfrom,x){
                Some(x) => if !x {
                                return match enteredfrom {
                                    0 => self.countspace(pos-1)+self.countspace(pos+self.width),
                                    1 => self.countspace(pos+1)+self.countspace(pos-self.width),
                                    2 => self.countspace(pos+self.width) + self.countspace(pos+1),
                                    3 => self.countspace(pos-self.width) + self.countspace(pos-1),
                                    _ => 0,
                                }
                            }else{
                                ()
                            },
                None => (),
            };
        }
        match enteredfrom {
            0 => (self.countspace(pos-1)),
            1 => (self.countspace(pos+1)),
            2 => (self.countspace(pos+self.width)),
            3 => (self.countspace(pos-self.width)),
            _ => 0,
        }
    }

    fn getleft(&mut self, pos:usize, enteredfrom:usize) -> usize  {
        if let NodeType::Pipe(x) = &self.nodes[pos].nodetype {
            match Nodegrid::l_or_rturn(enteredfrom,x){
                Some(x) => if x {
                                return match enteredfrom {
                                    0 => self.countspace(pos+1)+self.countspace(pos+self.width),
                                    1 => self.countspace(pos-1)+self.countspace(pos-self.width),
                                    2 => self.countspace(pos-self.width) + self.countspace(pos+1),
                                    3 => self.countspace(pos+self.width) + self.countspace(pos-1),
                                    _ => 0,
                                }
                            }else{
                                ()
                            },
                None => (),
            };
        }
        match enteredfrom {
            0 => self.countspace(pos+1),
            1 => self.countspace(pos-1),
            2 => self.countspace(pos-self.width),
            3 => self.countspace(pos+self.width),
            _ => 0,
        }
        
    }

    fn l_or_rturn(enteredfrom:usize, x:&[SideType;4]) -> Option<bool> {
        if enteredfrom == 0 && x[2] == SideType::Connection {
            Some(true)
        }else if enteredfrom == 0 && x[3] == SideType::Connection {
            Some(false)
        }else if enteredfrom == 1 && x[2] == SideType::Connection {
            Some(false)
        }else if enteredfrom == 1 && x[3] == SideType::Connection {
            Some(true)
        }else if enteredfrom == 2 && x[0] == SideType::Connection {
            Some(false)
        }else if enteredfrom == 2 && x[1] == SideType::Connection {
            Some(true)
        }else if enteredfrom == 3 && x[0] == SideType::Connection {
            Some(true)
        }else if enteredfrom == 3 && x[1] == SideType::Connection {
            Some(false)
        }else{
            None
        }
    }
}

#[derive(Debug)]
struct Node {
    nodetype: NodeType,
    tunnelpart: bool,
}

#[derive(Eq, PartialEq, Debug)]
enum NodeType {
    Pipe([SideType;4]),
    Start,
    Empty, //empty/uncounted
    Counted,
}

#[derive(Eq, PartialEq, Debug)]
enum SideType {
    Connection, //includes start
    _Inside,
    Outside,
}




pub fn day10_2() -> Result<usize, Box<dyn Error>> {
    let contents = fs::read_to_string("inputs/day10")
        .expect("Should have been able to read the file");

    
    let mut grid = Nodegrid::from_str(&contents);
    let mut pos = grid.nodes.iter().position(|x| x.nodetype == NodeType::Start).ok_or("cannot find start")?;
    let mut enteredfrom = 0;
    
    let temp = grid.find_con(pos,enteredfrom)?;
    pos = temp.0;
    enteredfrom = temp.1;

    let mut righturn = 0;
    let mut areacount = 0;

    loop{
        grid.nodes[pos].tunnelpart = true;

        match &grid.nodes[pos].nodetype {
            NodeType::Pipe(x) => {
                match Nodegrid::l_or_rturn(enteredfrom,x){
                    Some(x) => if x {righturn += 1;}
                        else{righturn -= 1;},
                    None => (),
                }

                let tmpe = grid.find_con(pos,enteredfrom)?;
                pos = tmpe.0;
                enteredfrom = tmpe.1;
            }
            NodeType::Start => {
                break;
            }
            _ => println!("{}","zz"),
        }

    } 
    
    enteredfrom = 0;
    pos += grid.width;
    
    loop{
        if righturn > 0 {
            areacount += grid.getright(pos, enteredfrom);
        }else{
            areacount += grid.getleft(pos, enteredfrom);
        }
        match &grid.nodes[pos].nodetype {
            NodeType::Pipe(_x) => {
                let tmpe = grid.find_con(pos,enteredfrom)?;
                pos = tmpe.0;
                enteredfrom = tmpe.1;
            }
            NodeType::Start => {
                break;
            }
            _ => println!("{}","zz"),
        }
    }

    let mut counter = 0;
    for nod in grid.nodes {
        if counter  == grid.width {
            print!("{}", "\n");
            counter = 0;
        }
        counter += 1;
        match nod.nodetype   {
            NodeType::Pipe(x) => if nod.tunnelpart {
                                    if x[0] == SideType::Connection && x[1] == SideType::Connection {
                                        print!("{}", "|")
                                    }else if x[0] == SideType::Connection && x[2] == SideType::Connection {
                                        print!("{}", "J")
                                    }else if x[0] == SideType::Connection && x[3] == SideType::Connection {
                                        print!("{}", "L")
                                    }else if x[1] == SideType::Connection && x[2] == SideType::Connection {
                                        print!("{}", "7")
                                    }else if x[1] == SideType::Connection && x[3] == SideType::Connection {
                                        print!("{}", "F")
                                    }else if x[2] == SideType::Connection && x[3] == SideType::Connection {

                                        print!("{}", "-")
                                    }
                                }else{
                                    print!("{}", "P")
                                },
            NodeType::Start => print!("{}", "S"),
            NodeType::Counted => print!("{}", "+"),
            NodeType::Empty => print!("{}", "."),
        };
    }
    println!("{}","");

    Ok(areacount)
}