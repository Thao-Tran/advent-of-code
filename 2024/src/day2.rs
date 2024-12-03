pub fn get_input () -> Vec<Vec<i32>> {
    let input = include_bytes!("../inputs/day2.txt");
    return String::from_utf8_lossy(input).split("\n").fold(vec![], |mut reports: Vec<Vec<i32>>, line| {
        let values: Vec<i32> = line.split_whitespace().map(|value| i32::from_str_radix(&value, 10).unwrap()).collect();
        if values.len() > 0 {
            reports.push(values);
        }
        return reports
    });
}

pub fn is_report_safe (report: &Vec<i32>) -> bool {
    let diffs: Vec<i32> = report[0..(report.len() - 1)].iter().enumerate().map(|(i, val)| val - report[i + 1]).collect();

    return diffs.iter().all(|diff| {
        let abs_diff = diff.abs();
        return abs_diff >= 1 && abs_diff <= 3 && diff.is_positive() == diffs[0].is_positive()
    });
}
