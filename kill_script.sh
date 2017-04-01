echo '###############################'
echo '# Testing shred:'
echo '###############################'
echo '# -> Creating test_shred.txt'
echo 'THIS IS A TEST TEXT' > test_shred.txt
cat test_shred.txt
shred -fuvz test_shred.txt
cat test_shred.txt
# shred -fuvz /dev/vda
