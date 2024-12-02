pub fn get_input () -> (Vec<i32>, Vec<i32>) {
    let input = include_bytes!("../inputs/day1.txt");
    return String::from_utf8_lossy(input).split("\n").fold((vec![], vec![]), |(mut left_list, mut right_list): (Vec<i32>, Vec<i32>), line| {
        let values: Vec<&str> = line.split_whitespace().collect();
        if let Some(left_value) = values.get(0) {
            left_list.push(i32::from_str_radix(&left_value, 10).unwrap());
        }
        if let Some(right_value) = values.get(1) {
            right_list.push(i32::from_str_radix(&right_value, 10).unwrap());
        }
        return (left_list, right_list)
    });
}
