
def get_safety(levels):
    is_safe = True
    last_value = None

    is_increasing = None
    last_is_increasing = None

    for level in levels:
        value = int(level)

        if last_value is not None:
            dif = abs(value - last_value)

            if(value - last_value > 0):
                is_increasing = True
            else:
                is_increasing = False

            if(dif < 1 or dif > 3):
                return False

            if(last_is_increasing is not None):
                if(last_is_increasing != is_increasing):
                    return False 

        last_is_increasing = is_increasing
        last_value = value


    return True

with open("2.txt") as file:

    report_outcome = []
    report_data = []
    report_problem_damper = []
    report_number = 0

    for report in file:

        levels = report.split()

        safety = get_safety(levels)

        if(safety is True):
            report_problem_damper.append(f"")


        if(safety is False):
            print(f"{len(levels)}")
            for x in range(len(levels)):
                removed_levels = levels[:]
                print(f"RL {len(removed_levels)} , Popping {x}")
                removed_levels.pop(x)
                safety = get_safety(removed_levels)
                if(safety is True):
                    report_problem_damper.append(f"Adjusted: {removed_levels}, Removed index ({x})")
                    break

        if(safety is False):
            report_problem_damper.append(f"")

         
        report_data.append(report)
        report_outcome.append(safety)

        report_number+=1


report_cnt = 0
safe_reports = 0
unsafe_reports = 0

for report_safety in report_outcome:
    if(report_safety is True):
        safe_reports+=1
        print(f"Report {report_cnt} - Safe: {report_data[report_cnt]}, {report_problem_damper[report_cnt]}", end='')

    if(report_safety is False):
        unsafe_reports+=1
        print(f"Report {report_cnt} - Unsafe: {report_data[report_cnt]}", end='')

        #print(unsafe_report)
#        print(str.join(',', report_data[report_cnt].split()))
        #print(f"Status: {is_safe}")

    report_cnt+=1

print(f"Safe reports: {safe_reports}, Unsafe reports: {unsafe_reports}")



