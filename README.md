# Toksikologiasovellus

### Välipalautus 2

**Sovelluksen nykyinen tilanne**:

* Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
    * Tämänhetkisessä versiossa käyttäjä voi tunnuksen luomisen yhteydessä itse valita, luoko peruskäyttäjän vai ylläpitäjän tilin.
* Käyttäjä näkee listan, jossa näkyvät aineiden nimet. Klikkaamalla aineen nimeä käyttäjä näkee kyseisen aineen tiedot (esim. nimi, käyttötarkoitus, vaikutuskohde, haittavaikutukset) sekä aineeseen liittyvät mahdolliset yhteisvaikutukset, mikäli tällaisia on lisätty tietokantaan.
    * Tämänhetkisessä versiossa yhteisvaikutukset toimivat ainoastaan kahden aineen välillä.
* Ylläpitäjä voi lisätä uusia aineita sekä niiden välisiä yhteisvaikutuksia.

**Sovellus Herokussa**

Sovellus sijaitsee osoitteessa https://toksikologiasovellus.herokuapp.com/.

* Aloitusnäkymä:
    * Jos käyttäjä ei ole kirjautunut sisään, aloitusnäkymässä näkyy kentät käyttäjätunnukselle ja salasanalle sekä *Kirjaudu sisään* -nappi. Mikäli käyttäjä on aiemmin luonut itselleen käyttäjätilin, hän voi kirjautua sisään syöttämällä käyttäjätunnuksensa ja salasanansa niille varattuihin kenttiin sekä klikkaamlla tämän jälkeen *Kirjaudu sisään* -nappia.
    * Jos käyttäjällä ei ole käyttäjätiliä tai hän haluaa muusta syystä luoda itselleen uuden tilin, tämä onnistuu klikkaamalla linkkiä *Luo uusi käyttäjätili*.
    * Kun käyttäjä on kirjautunut sisään, aloitusnäkymässä näkyy lista tietokannassa olevista aineista sekä linkki *Kirjaudu ulos*, jonka klikkaaminen nimensä mukaisesti kirjaa käyttäjän ulos, jolloin näkymä palautuu ei-kirjautuneen käyttäjän mukaiseksi.
    * Jos sisään kirjautunut käyttäjä on ylläpitäjä, hän näkee edellämainittujen lisäksi linkit *Lisää uusi aine* sekä *Lisää yhteisvaikutus*.
* Ainekohtainen tietonäkymä:
    * Kun käyttäjä on kirjautunut sisään, aloitusnäkymässä näkyy lista tietokannassa olevista aineista. Kukin aine toimii linkkinä, jonka klikkaaminen avaa kyseisen aineen tiedot.
    * Tietonäkymästä pääsee takaisin aloitusnäkymään klikkaamalla linkkiä *Takaisin*.
* Uuden käyttäjätilin luonti:
    * Uuden käyttäjätilin luontinäkymään pääsee klikkaamalla aloitusnäkymässä olevaa linkkiä *Luo uusi käyttäjätili*.
    * Käyttäjä voi syöttää haluamansa käyttäjänimen sekä salasanan niille varattuihin kenttiin.
    * Kun käyttäjä on syöttänyt haluamansa käyttäjänimen ja salasanan sekä valinnut käyttäjäroolin, hän voi luoda uuden tilin klikkaamalla nappia *Luo tili*. Sovellus kirjaa käyttäjän automaattisesti sisään uudella tilillä ja palaa aloitusnäkymään.
    * Linkki *Peruuta* palauttaa käyttäjän aloitusnäkymään luomatta uutta tiliä.
* Uuden aineen lisääminen:
    * Kun käyttäjä on kirjautunut sisään ylläpitäjänä, hän pääsee aloitusnäkymästä uuden aineen luontinäkymään klikkaamalla linkkiä *Lisää uusi aine*.
    * Uuden aineen luontinäkymässä on kentät, joihin ylläpitäjä voi syöttää aineen nimen, vaikutuskohteen, vaikutusmekanismin, metaboloitumisreitin, vaikutusajan, mahdolliset muut huomiot sekä mahdolliset haittavaikutukset. Kun halutut tiedot on syötetty niille varattuihin kenttiin, aineen lisääminen tietokantaan tapahtuu klikkaamalla nappia *Luo aine*.
    * Linkki *Peruuta* palauttaa käyttäjän aloitusnäkymään lisäämättä uutta ainetta tietokantaan.
* Uuden yhteisvaikutuksen lisääminen:
    * Kun käyttäjä on kirjautunut sisään ylläpitäjänä, hän pääsee aloitusnäkymästä uuden yhteisvaikutuksen luontinäkymään klikkaamalla linkkiä *Lisää yhteisvaikutus*.
    * Yhteisvaikutuksen luontinäkymässä ylläpitäjä näkee kutakin ainetta vastaavan valintaruudun. Yhteisvaikutus luodaan valitsemalla siihen kuuluvat aineet sekä kirjoittamalla yhteisvaikutuksen kuvaus sille varattuun tekstikenttään ja tämän jälkeen klikkaamalla nappia *Lisää yhteisvaikutus*.
    * * Linkki *Peruuta* palauttaa käyttäjän aloitusnäkymään lisäämättä uutta yhteisvaikutusta tietokantaan.

### Välipalautus 1
Sovellus antaa tietoa lääkeaineiden sekä eräiden muiden kemikaalien aiheuttamista haitallisista ja myrkyllisistä vaikutuksista ihmiselimistöön sekä näiden hoitoperiaatteista. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

* Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
* Käyttäjä näkee listan, jossa näkyvät aineiden nimet. Klikkaamalla aineen nimeä käyttäjä näkee kyseisen aineen tiedot (esim. nimi, käyttötarkoitus, vaikutuskohde, haittavaikutukset) sekä listan aineista, jonka kanssa valitulla aineella on yhteisvaikutuksia.
* Klikkaamalla aineen tiedoista toista ainetta, jolla on ko. aineen kanssa yhteisvaikutuksia, käyttäjä näkee tiedot yhteisvaikutuksista.
* Käyttäjä voi hakea ainetta sen nimen perusteella.
* Käyttäjä voi hakea kaikki aineet, jotka kuuluvat tiettyyn aineluokkaan (esim. tulehduskipulääke, beetasalpaaja, viemärinpuhdistusaine) tai joilla on tietty käyttötarkoitus tai vaikutuskohde (kohde-elin, -entsyymi, -reseptori tmv.).
* Ylläpitäjä voi lisätä uusia aineita sekä muokata aineiden tietoja.
