extern crate advent_of_code_2024;
use advent_of_code_2024::day1::get_input;

// Answer: 27732508
fn main () {
    let (left_list, right_list) = get_input();
    let similarity_score = left_list.iter().fold(0, |similarity_score, left_val| {
        similarity_score + *left_val * (right_list.iter().filter(|right_val| left_val == *right_val).count() as i32)

    });

    println!("{}", similarity_score)
}
