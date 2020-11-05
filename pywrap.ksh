rm -f PowerInput.txt
while true; do
        read line
        echo "$line">>PowerInput.txt
        if [[ "$line" = "EOF" ]]; then
                break;
        fi
done
sort -u PowerInput.txt>PowerInputTmp.txt
python calcEnergy.py
