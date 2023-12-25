if mkdir -p "corpus_treated_by_Freeling"; then
    echo "Directory ensured to exist."
else
    echo "Failed to ensure directory exists."
fi

for dir in $(ls corpus_reformed)
	do
        for file in $(ls corpus_reformed/$dir)
            do
                if mkdir -p "corpus_treated_by_Freeling/$dir"; then
                    analyze -f fr.cfg < corpus_reformed/$dir/$file > corpus_treated_by_Freeling/$dir/$file
                fi
                
                # mkdir corpus_treated_by_Freeling/$dir
                # analyze -f fr.cfg <  $file  >  corpus_treated_by_Freeling/$dir/$file
            done
	done