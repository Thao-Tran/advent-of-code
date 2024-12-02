extern crate advent_of_code_2024;
use advent_of_code_2024::day1::get_input;

// Answer: 765748
fn main () {
    let (mut left_list, mut right_list) = get_input();
    left_list.sort();
    right_list.sort();
    let total_distance = left_list.iter().zip(right_list.iter()).fold(0, |total_distance, (left_val, right_value)| {
        total_distance + left_val.abs_diff(*right_value)
    });

    println!("{}", total_distance)
}
