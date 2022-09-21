# Torrent Analyze
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
SOS, someone is torrenting on our network. 
One of your colleagues has been using torrent to download some files on the company’s network.
Can you identify the file(s) that were downloaded? 
The file name will be the flag, like picoCTF{filename}. [Captured traffic]().
## HINTS:
1. Download and open the file with a packet analyzer like [Wireshark](https://www.wireshark.org/).
2. You may want to enable BitTorrent protocol (BT-DHT, etc.) on Wireshark. Analyze -> Enabled Protocols.
3. Try to understand peers, leechers and seeds. [Article](https://www.techworm.net/2017/03/seeds-peers-leechers-torrents-language.html).
4. The file name ends with `.iso`.
## STEPS:
1. First, download the file given.
2. 
