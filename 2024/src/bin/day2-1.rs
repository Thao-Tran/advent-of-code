extern crate advent_of_code_2024;
use advent_of_code_2024::day2::{get_input,is_report_safe};

// Answer: 220
fn main () {
    let reports = get_input();
    let safe_reports = reports.iter()
        .filter(|report| is_report_safe(&report))
        .count();

    println!("{}", safe_reports)
}
