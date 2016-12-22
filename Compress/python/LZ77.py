# coding:utf-8


class LZ77:

    def __init__(self, windowSize):
        self.windowSize = windowSize
        self.bufferSize = 4

    def compress(self, message):
        cursor = 0
        out = []
        while cursor < len(message):
            (p, l, c) = self.longestMatch(message, cursor)
            out.append((p, l, c))
            cursor += (l + 1)
        return out

    def longestMatch(self, data, cursor):
        endCursor = min(cursor + self.bufferSize, len(data))
        bufferString = data[cursor:endCursor]
        startCursor = max(0, cursor - self.windowSize)
        windowString = data[startCursor:cursor]

        # print 'WindowString = ', windowString, 'BufferString = ', bufferString

        p = 0
        l = 0
        c = ''
        i = 0
        searchCursor = 0
        hasSearched = False
        while i < len(windowString):
            if searchCursor >= len(bufferString):
                searchCursor = 0
            if windowString[i] == bufferString[searchCursor]:
                hasSearched = True
                if searchCursor == 0:
                    p = i
                l = (searchCursor + 1)
                searchCursor = searchCursor + 1
            else:
                if searchCursor != 0:
                    i = i - 1
                searchCursor = 0
            i = i + 1

        if hasSearched:
            if cursor > self.windowSize - 1:
                p = self.windowSize - p
            else:
                p = cursor - p
        if cursor + l < len(data):
            c = data[cursor + l]
        # print p, l, c
        return p, l, c

    def decompress(self, compressed):
        out = ''
        for (p, l, c) in compressed:
            out = out + out[len(out) - p:l + len(out) - p]+ c
        return out


if __name__ == '__main__':
    compressor = LZ77(6)
    origin = list('aacaacabcabaaacsadsaasdfdsfsadfdffuioasjfmnjkchasn,nm,c mnxzbcuiwbsnbvckdsgaffjkdsgahjbcqwgelrjhdssad3rwa')
    pack = compressor.compress(origin)
    unpack = compressor.decompress(pack)
    print pack
    print unpack
    print unpack == 'aacaacabcabaaacsadsaasdfdsfsadfdffuioasjfmnjkchasn,nm,c mnxzbcuiwbsnbvckdsgaffjkdsgahjbcqwgelrjhdssad3rwa'
