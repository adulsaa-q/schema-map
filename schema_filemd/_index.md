# Schema Index

> Generated: 2026-05-04

| table | rows | type | connects to | referenced by |
|-------|------|------|-------------|---------------|
| [[inventory]] | 4,581 |  | [[film]], [[store]] | [[rental]] |
| [[film_actor]] | 5,462 | junction | [[actor]], [[film]] | — |
| [[address]] | 603 |  | [[city]] | [[customer]], [[staff]], [[store]] |
| [[city]] | 600 |  | [[country]] | [[address]] |
| [[actor]] | 200 |  | — | [[film_actor]] |
| [[film_category]] | 2,367 | junction | [[category]], [[film]] | — |
| [[category]] | 16 |  | — | [[film_category]] |
| [[country]] | 109 |  | — | [[city]] |
| [[language]] | 6 |  | — | [[film]], [[film]] |
| [[customer]] | 599 |  | [[address]], [[store]] | [[payment_p2022_06]], [[rental]], [[payment_p2022_03]], [[payment_p2022_04]], [[payment_p2022_05]], [[payment_p2022_01]], [[payment_p2022_02]] |
| [[film]] | 1,000 |  | [[language]], [[language]] | [[inventory]], [[film_actor]], [[film_category]] |
| [[payment_p2022_06]] | 2,654 |  | [[customer]], [[rental]], [[staff]] | — |
| [[rental]] | 16,044 |  | [[customer]], [[inventory]], [[staff]] | [[payment_p2022_06]], [[payment_p2022_03]], [[payment_p2022_04]], [[payment_p2022_05]], [[payment_p2022_01]], [[payment_p2022_02]] |
| [[payment]] | 16,049 |  | — | — |
| [[staff]] | 1,500 |  | [[address]], [[store]] | [[payment_p2022_06]], [[rental]], [[payment_p2022_03]], [[payment_p2022_04]], [[payment_p2022_05]], [[payment_p2022_01]], [[payment_p2022_02]] |
| [[payment_p2022_03]] | 2,713 |  | [[customer]], [[rental]], [[staff]] | — |
| [[payment_p2022_07]] | 2,334 |  | — | — |
| [[payment_p2022_04]] | 2,547 |  | [[customer]], [[rental]], [[staff]] | — |
| [[payment_p2022_05]] | 2,677 |  | [[customer]], [[rental]], [[staff]] | — |
| [[store]] | 500 |  | [[address]] | [[inventory]], [[customer]], [[staff]] |
| [[payment_p2022_01]] | 723 |  | [[customer]], [[rental]], [[staff]] | — |
| [[payment_p2022_02]] | 2,401 |  | [[customer]], [[rental]], [[staff]] | — |
