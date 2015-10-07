rm `find . -name NOTES `
mkdir cleaned_data
ls
mv data/*/* cleaned_data/
for file in cleaned_data/*; do mv $file $file.txt; done
la cleaned_data/
history
