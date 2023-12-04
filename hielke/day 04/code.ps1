# advent of code 2023 day 4
# by: hielke

class Card
{
    [int]$card_id
    [int]$card_count
    [Collections.Generic.List[Int]]$winning_numbers
    [Collections.Generic.List[Int]]$card_numbers

    Card () {}
    Card ([int]$card_id) {
        $this.card_id = $card_id
        $this.card_count = 1
        $this.winning_numbers = New-Object Collections.Generic.List[Int]
        $this.card_numbers = New-Object Collections.Generic.List[Int]
    }

    [int] get_win_amt () {
        $private:win_amt = 0
        foreach($private:card_number in $this.card_numbers) {
            if($this.winning_numbers -contains $private:card_number) {
                $private:win_amt += 1
            }
        }

        return $private:win_amt
    }

    [int] get_score () { # part 1: score = 2^win_amt
        $private:win_amt = $this.get_win_amt()

        if($private:win_amt -gt 0) { return [Math]::Pow(2, $private:win_amt - 1) }
        return 0
    }

    add_count([int] $card_count) {
        $this.card_count += $card_count
    }
}

$cards = New-Object Collections.Generic.List[Card]
# sample text for testing
foreach ($line in Get-Content $PSScriptRoot\input.txt) {
    # get card info
    # format Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    $card_id = [int]$line.Split(':')[0].Split(' ')[1]
    # write-host $card_id

    $str_winning_numbers = $line.Split(':')[1].Split('|')[0] # extract first set of values
    $str_winning_numbers = $str_winning_numbers.Trim() # remove leading and trailing spaces
    $str_winning_numbers = $str_winning_numbers.Replace('  ', ' ') # remove double spaces
    # write-host $str_winning_numbers

    $str_card_numbers = $line.Split(':')[1].Split('|')[1]
    $str_card_numbers = $str_card_numbers.Trim() # remove leading and trailing spaces
    $str_card_numbers = $str_card_numbers.Replace('  ', ' ') # remove double spaces
    # write-host $str_card_numbers

    # create new card and fill with string info
    $card = New-Object -TypeName Card -ArgumentList $card_id
    foreach ($winning_number in $str_winning_numbers.split(' ')) {
        $card.winning_numbers.Add([int]$winning_number)
    }
    foreach ($card_number in $str_card_numbers.split(' ')) {
        $card.card_numbers.add([int]$card_number)
    }
    $cards.add($card)
}

# part 1: calculate score
$card_score_sum = 0
foreach ($card in $cards) {
    # write-host 'ID:', $card.card_id
    # write-host 'score:', $card.get_score()
    $card_score_sum += $card.get_score()
}
write-host 'total score:', $card_score_sum

# part 2
# you win copies of the scratchcards below the winning card equal to the number of matches. 
# So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.
foreach ($i in 0..($cards.Count - 1)) {
    $amount = $cards[$i].get_win_amt()
    # add x tickets to the next n cards
    if ($amount -gt 0) {
        foreach ($j in ($i + 1)..($i+$amount)) {
            $cards[$j].add_count($cards[$i].card_count)
        }
    }
    # write-host 'ID:', $cards[$i].card_id, 'count:', $cards[$i].card_count
}

# get the sum of all scratch cards
$card_amt_sum = 0
foreach ($card in $cards) {
    $card_amt_sum += $card.card_count
}
write-host 'total scratch cards:', $card_amt_sum