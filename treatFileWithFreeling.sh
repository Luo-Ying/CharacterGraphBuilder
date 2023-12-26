if mkdir -p "corpus/corpus_treated_by_Freeling"; then
    echo "Directory ensured to exist."
else
    echo "Failed to ensure directory exists."
fi

for dir in $(ls corpus/corpus_reformed)
	do
        for file in $(ls corpus/corpus_reformed/$dir)
            do
                if mkdir -p "corpus/corpus_treated_by_Freeling/$dir"; then
                    analyze -f fr.cfg < corpus/corpus_reformed/$dir/$file > corpus/corpus_treated_by_Freeling/$dir/$file
                fi
            done
	done