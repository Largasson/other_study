class SequenceZip:
    def __init__(self, *sequences):
        self.sequence_zip = list(zip(*sequences))

    def __iter__(self):
        yield from self.sequence_zip

    def __len__(self):
        return len(self.sequence_zip)

    def __getitem__(self, key):
        return self.sequence_zip[key]



# TEST_3:
print(len(SequenceZip([1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 4], 'data')))

# TEST_4:
x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
sequencezip = SequenceZip(x, y, z)

print(sequencezip[2])
x[-1], z[-1] = z[-1], x[-1]
print(sequencezip[2])

# TEST_5:
many_large_sequences = [range(100000) for _ in range(100)]
sequencezip = SequenceZip(*many_large_sequences)
print(sequencezip[99999])

# TEST_6:
sequencezip = SequenceZip()
print(len(sequencezip))
print(list(sequencezip))

# TEST_7:
data1 = [1, 2, 3, 4, 5]
data2 = 'abcde'

sequencezip = SequenceZip(data1, data2)
data1.extend([6, 7, 8, 9, 10])
data2 += 'fghij'

print(data1)
print(data2)
print(len(sequencezip))
print(list(sequencezip))