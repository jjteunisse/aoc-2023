
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
    Joker,
}

#[derive(Eq, PartialEq, PartialOrd, Ord, Clone, Debug)]
enum Card {
    Joker,
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    Ten,
    Queen,
    King,
    Ace,
}

impl Add for Handtype {
    type Output = Self;

    fn add(self, other: Self) -> Self {
        if self == Handtype::Joker || other == Handtype::Joker {
            if self == Handtype::Highcard || other == Handtype::Highcard {
                Handtype::Pair
            }
            else if self == Handtype::Pair || other == Handtype::Pair {
                Handtype::Threeofakind
            }
            else if self == Handtype::Threeofakind || other == Handtype::Threeofakind {
                Handtype::Fourofakind
            }
            else if self == Handtype::Fourofakind || other == Handtype::Fourofakind {
                Handtype::Fiveofakind
            }
            else if self == Handtype::Twopair || other == Handtype::Twopair {
                Handtype::Fullhouse
            }else{
                self
            }
        }
        else if self == Handtype::Pair {
            if other == Handtype::Pair {
                Handtype::Twopair
            }
            else if other == Handtype::Threeofakind {
                Handtype::Fullhouse
            }else{
                self
            }
        }else if other == Handtype::Pair{
            if self == Handtype::Threeofakind {
                Handtype::Fullhouse
            }else{
                other
            }
        }else if self == Handtype::Highcard{
            other
        }else {
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
        if card == &Card::Joker {
            handtypes.push(Handtype::Joker);
            continue;
        }
        inputhandvec = inputhandvec.into_iter()
            .filter_map(|x| 
                if &x == card {
                    None
                }else{
                    Some(x)
                }
            ).collect();
        match HANDLEN - carddel - inputhandvec.len() {
            1 => {carddel += 1; handtypes.push(Handtype::Highcard)},
            2 => {carddel += 2; handtypes.push(Handtype::Pair)},
            3 => {carddel += 3; handtypes.push(Handtype::Threeofakind)},
            4 => {carddel += 4; handtypes.push(Handtype::Fourofakind)},
            5 => {carddel += 5; handtypes.push(Handtype::Fiveofakind)},
            _ => (),
        };
    }
    handtypes.sort();
    let mut finaltype:Handtype = Handtype::Highcard;
    for card in handtypes {
        finaltype = finaltype+card;
    }
    Ok(finaltype)
}

pub fn day7_2() -> Result<usize,String> {
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
                        'J' => Ok(Card::Joker),
                        'Q' => Ok(Card::Queen),
                        'K' => Ok(Card::King),
                        'A' => Ok(Card::Ace),
                        _ => Err("invalid card".to_string()),
                    }
                }).collect::<Result<_,_>>()?;

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
    let total = sets.iter()
        .enumerate()
        .map(|(index,x)| {
            x.bid*(index+1)
        }).sum();
            
    Ok(total)
}