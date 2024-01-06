use std::fs;
use core::ops::Add;

const HANDLEN:usize = 5;

#[derive(Eq, PartialEq, PartialOrd, Ord, Debug)]
struct Set {
    handtype: Handtype,
    hand: [Card;5],
    bid:usize,
}

#[derive(Eq, PartialEq, PartialOrd, Ord, Debug)]
enum Handtype {
    Highcard,
    Pair,
    Twopair,
    Threeofakind,
    Fullhouse,
    Fourofakind,
    Fiveofakind,
}

#[derive(Eq, PartialEq, PartialOrd, Ord, Clone, Debug)]
enum Card {
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    Ten,
    Jack,
    Queen,
    King,
    Ace,
}

impl Add for Handtype {
    type Output = Self;

    fn add(self, other: Self) -> Self {
        if self == Handtype::Pair && other == Handtype::Pair {
            Handtype::Twopair
        }else if self == Handtype::Pair && other == Handtype::Threeofakind{
            Handtype::Fullhouse
        }else if self == Handtype::Threeofakind && other == Handtype::Pair{
            Handtype::Fullhouse
        }else{
            self
        }
    }
}

fn verify_len<T: Clone>(hand:&Vec<T>) -> Result<[T;HANDLEN],String> {
    match hand.len() {
        HANDLEN => Ok([hand[0].clone(),hand[1].clone(),hand[2].clone(),hand[3].clone(),hand[4].clone()]),
        _       => Err("hand too short".to_string()),
    }
}

fn calc_type(inputhand:&Vec<Card>) -> Result<Handtype,String> {
    let mut inputhandvec:Vec<_> = inputhand.clone();
    let mut handtypes:Vec<Handtype> = vec![];
    let mut carddel = 0;
    for card in inputhand.iter() {
        inputhandvec = inputhandvec.into_iter()
            .filter_map(|x| 
                if &x == card {
                    None
                }else{
                    Some(x)
                }
            ).collect();
        match HANDLEN - carddel - inputhandvec.len() {
            1 => carddel += 1,
            2 => {carddel += 2; handtypes.push(Handtype::Pair)},
            3 => {carddel += 3; handtypes.push(Handtype::Threeofakind)},
            4 => {carddel += 4; handtypes.push(Handtype::Fourofakind)},
            5 => {carddel += 5; handtypes.push(Handtype::Fiveofakind)},
            _ => println!("{}","nocardsleft"),
        };
        //println!("{:?}",handtypes);
    }
    if handtypes.len() == 0 {
        Ok(Handtype::Highcard)
    }else if handtypes.len() == 2{
        Ok(handtypes.pop().unwrap()+handtypes.pop().unwrap())
    }else{
        Ok(handtypes.pop().unwrap())
    }
}

pub fn day7_1() -> Result<usize,String> {
    let contents = fs::read_to_string("inputs/day7")
        .expect("Should have been able to read the file");

    let mut sets:Vec<Set> = contents
        .lines()
        .map(|line| {
            let split_line = line.split_once(' ').unwrap();
            let hand:Vec<_> = split_line.0
                .chars()
                .map(|x| {
                    match x {
                        '2' => Ok(Card::Two),
                        '3' => Ok(Card::Three),
                        '4' => Ok(Card::Four),
                        '5' => Ok(Card::Five),
                        '6' => Ok(Card::Six),
                        '7' => Ok(Card::Seven),
                        '8' => Ok(Card::Eight),
                        '9' => Ok(Card::Nine),
                        'T' => Ok(Card::Ten),
                        'J' => Ok(Card::Jack),
                        'Q' => Ok(Card::Queen),
                        'K' => Ok(Card::King),
                        'A' => Ok(Card::Ace),
                        _ => Err("invalid card".to_string()),
                    }
                }).collect::<Result<_,_>>()?;

            println!("{:?}", hand);
            let bid = split_line.1.parse::<usize>().unwrap();
            let handtype = calc_type(&hand)?;
            let handarray = verify_len(&hand)?;
            Ok(Set {
                handtype: handtype,
                hand: handarray,
                bid: bid,
            })
        }).collect::<Result<Vec<Set>,String>>()?;
    
    
    sets.sort();
    println!("{:?}",sets);
    let total = sets.iter()
        .enumerate()
        .map(|(index,x)| {
            println!("{}  {}",index+1,x.bid);
            x.bid*(index+1)
        }).sum();
            
    Ok(total)
}