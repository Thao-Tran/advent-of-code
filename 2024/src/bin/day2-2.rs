extern crate advent_of_code_2024;
use advent_of_code_2024::day2::{get_input,is_report_safe};

// Answer: 296
fn main () {
    let reports = get_input();
    let safe_reports = reports.iter().filter(|report| {
        let safe = is_report_safe(&report);

        if safe {
            return safe
        }

        report.iter()
            .enumerate()
            .any(|(i, _)| {
                let mut report_without_level = report.to_vec();
                report_without_level.remove(i);
                is_report_safe(&report_without_level)
            })
    }).count();

    println!("{}", safe_reports)
}
