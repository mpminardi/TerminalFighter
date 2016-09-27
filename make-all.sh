RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

if astyle *.h *.cpp -r --dry-run | grep Formatted; then
    printf "\n${RED}|*******| STYLE CHECK FAILED |*******|${NC}\n\n"
    exit 1
else
    printf "\n${GREEN}|*******| STYLE CHECK SUCCESSFUL |*******|${NC}\n\n"    
fi

make
if [ $? -eq 0 ]; then
	printf "\n${GREEN}|*******| SOURCE COMPILATION SUCCESSFUL |*******|${NC}\n\n"
else
	printf "\n${RED}|*******| SOURCE COMPILATION FAILED |*******|${NC}\n\n"
	exit 1
fi

make -C ./test
if [ $? -eq 0 ]; then
	printf "\n${GREEN}|*******| TEST COMPILATION SUCCESSFUL |*******|${NC}\n\n"
else
	printf "\n${RED}|*******| TEST COMPILATION FAILED |*******|${NC}\n\n"
	exit 1
fi

./test/run-tests
