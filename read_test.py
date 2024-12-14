import read;

res = [['every', '12'], ['everyone', '8'], ['everyones', '1'], ['everything', '27'], ['everythings', '1'], ['everythingthere', '1'], ['everywhere', '2'], ['exact', '1'], ['exactly', '4'], ['exaggerated', '1'], ['examination', '1'], ['example', '1'], ['except', '4'], ['exceptionally', '1'], ['excessive', '1'], ['exchange', '2'], ['excited', '1'], ['excitedly', '2'], ['excitement', '1'], ['exclaim', '1'], ['exclusion', '1'], ['excusal', '1'], ['excuse', '2'], ['exempt', '2'], ['exhausted', '2'], ['exhaustion', '1'], ['exists', '1'], ['expectations', '1'], ['expected', '7']]
def test_read():
    if read.read() == res:
        print("TEST PASSED")
    else:
        print("TEST FAILED")

if __name__ == "__main__":
    test_read()
