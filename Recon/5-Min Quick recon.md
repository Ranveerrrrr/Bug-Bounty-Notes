---
Creator: Lostsec
Type: Article
tags:
  - Recon
  - Article
  - bugbounty
---
## Mass Scanning with Shodan & Nuclei
- **Find Your Target CVE**: pick a CVE you want to hunt for
- **Shodan Dorking**: Head over to **Shodan** and use a specific search dork related to the product or CVE
- **Extract and Scan**: IP, Domain
- ```cat ip.txt | nuclei -tags {{According to you}} -bs 50 -c 50 -es info```

## Automated Bug Hunting Toolkit: A Deep Dive into Each Tool
- **AlienVault OTX**:  Mass URL Discovery
- ```./alienvault.sh domain.com```