def hanoi(n, initial_rod, final_rod, aux_rod):
    if n == 0:
        return
    
    hanoi(n-1, initial_rod, aux_rod, final_rod)
    print(f"Move disk {n} from rod {initial_rod} to rod {final_rod}")
    hanoi(n-1, aux_rod, final_rod, initial_rod)


hanoi(3, 'A', 'C', 'B')