n = 1

while n <= 10:
	print(f"<h2>Tabuada de {n}:</h2>")
	print("<table border=1>")
	for i in range(0, 11):
		print(f"<tr><td>{n} x {i} =</td><td>{n * i}</td></tr>")
	print("</table>")
	n += 1
    

