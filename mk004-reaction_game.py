def reaction_game():
    """
    A game measuring the players reaction time in seconds.
    """
    import time
    import random

    print("The epoch on this system starts at " + time.strftime("%c", time.gmtime(0)))
    print("The current timezone is " + f"{time.tzname[0]} with an offset of {time.timezone}")
    if time.daylight != 0:
        print("\tDaylight Saving Time is effect for this location.")
        print("\tThe DST timezone is " + time.tzname[1])
    print("Local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print("UTC time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    print(time.time())
    print("Year:", time.localtime()[0])
    input("Press enter to start.")
    time.sleep(random.randint(1, 3))
    start_time_t = time.time()
    start_time_p = time.perf_counter()
    start_time_m = time.monotonic()
    start_time_pt = time.process_time()
    input("Press enter to stop.")
    stop_time_t = time.time()
    stop_time_p = time.perf_counter()
    stop_time_m = time.monotonic()
    stop_time_pt = time.process_time()
    print(f"Your reaction time was {stop_time_t - start_time_t} seconds.")
    print(f"Your reaction perf time was {stop_time_p - start_time_p} seconds.")
    # Best function for reaction game.
    print("Your reaction monotonic time was " + f"{stop_time_m - start_time_m} seconds.")
    print("Your reaction process time is " + f"{stop_time_pt - start_time_pt} seconds.")


reaction_game()
