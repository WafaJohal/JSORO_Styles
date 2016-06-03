for f in *.pdf; do
	convert ./"$f" ./"${f%.pdf}.eps"
done
