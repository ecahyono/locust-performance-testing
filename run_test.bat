@echo off

echo ====================================
echo Starting Performance Test
echo ====================================

mkdir reports 2>nul

locust -f locustfile.py ^
--host=https://dummyjson.com ^
--users 100 ^
--spawn-rate 10 ^
--run-time 2m ^
--headless ^
--html reports/report.html ^
--csv reports/result ^
--stop-timeout 10

echo.
echo ====================================
echo Test Completed
echo HTML Report : reports\report.html
echo CSV Results : reports\
echo ====================================

pause