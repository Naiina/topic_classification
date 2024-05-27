import json


data = [
    {"sentence": "Die neuen Technologien verändern die Arbeitswelt.", "topic": "Technologien"},
    {"sentence": "In der Stadt gibt es viele Parks und Grünflächen.", "topic": "Parks"},
    {"sentence": "Das Interesse an Nachhaltigkeit wächst stetig.", "topic": "Nachhaltigkeit"},
    {"sentence": "Viele Wissenschaftler forschen an erneuerbaren Energien.", "topic": "Energien"},
    {"sentence": "Die Preise für Immobilien steigen weiter an.", "topic": "Preise"},
    {"sentence": "Sport ist für die Gesundheit sehr wichtig.", "topic": "Sport"},
    {"sentence": "Die Politik hat großen Einfluss auf das tägliche Leben.", "topic": "Politik"},
    {"sentence": "Kunst und Kultur bereichern unser Leben.", "topic": "Kultur"},
    {"sentence": "Bildung ist der Schlüssel zu einem besseren Leben.", "topic": "Bildung"},
    {"sentence": "Das Internet hat die Kommunikation revolutioniert.", "topic": "Internet"},
    {"sentence": "Moderne Medizin verlängert das Leben vieler Menschen.", "topic": "Medizin"},
    {"sentence": "Die Umweltverschmutzung bedroht viele Tierarten.", "topic": "Umweltverschmutzung"},
    {"sentence": "Musik kann die Stimmung erheblich beeinflussen.", "topic": "Musik"},
    {"sentence": "Das neue Buch des Autors ist sehr spannend.", "topic": "Buch"},
    {"sentence": "Die neuen Rezepte sind bei den Gästen sehr beliebt.", "topic": "Rezepte"},
    {"sentence": "Sportliche Aktivitäten fördern die Fitness.", "topic": "Aktivitäten"},
    {"sentence": "Das Konzert gestern war ein voller Erfolg.", "topic": "Konzert"},
    {"sentence": "Viele Menschen bevorzugen biologisches Essen.", "topic": "Essen"},
    {"sentence": "Die neueste Technologie beeindruckt alle Anwesenden.", "topic": "Technologie"},
    {"sentence": "Kulturelle Vielfalt bereichert das Zusammenleben.", "topic": "Vielfalt"},
    {"sentence": "Die Arbeitslosigkeit ist in vielen Regionen ein Problem.", "topic": "Arbeitslosigkeit"},
    {"sentence": "Das Klima ändert sich schneller als erwartet.", "topic": "Klima"},
    {"sentence": "Viele Unternehmen investieren in erneuerbare Energien.", "topic": "Unternehmen"},
    {"sentence": "Die Gesundheit der Bevölkerung ist ein wichtiges Thema.", "topic": "Gesundheit"},
    {"sentence": "Die neuen Filme sind bei den Zuschauern sehr beliebt.", "topic": "Filme"},
    {"sentence": "Der technische Fortschritt schreitet rasant voran.", "topic": "Fortschritt"},
    {"sentence": "Die Digitalisierung verändert die Arbeitswelt.", "topic": "Digitalisierung"},
    {"sentence": "Das Projekt ist auf einem guten Weg.", "topic": "Projekt"},
    {"sentence": "Der Austausch von Wissen ist essentiell.", "topic": "Austausch"},
    {"sentence": "In der Stadt gibt es viele historische Gebäude.", "topic": "Gebäude"},
    {"sentence": "Die Forschung an Impfstoffen ist sehr wichtig.", "topic": "Impfstoffen"},
    {"sentence": "Neue Technologien erleichtern den Alltag.", "topic": "Technologien"},
    {"sentence": "Das Interesse an Kunst steigt.", "topic": "Kunst"},
    {"sentence": "Sportveranstaltungen ziehen viele Besucher an.", "topic": "Sportveranstaltungen"},
    {"sentence": "Nachhaltige Mode wird immer beliebter.", "topic": "Mode"},
    {"sentence": "Die Reisebranche erholt sich langsam.", "topic": "Reisebranche"},
    {"sentence": "Der Austausch von Kulturen fördert das Verständnis.", "topic": "Kulturen"},
    {"sentence": "Das Lesen fördert die geistige Entwicklung.", "topic": "Lesen"},
    {"sentence": "Der Tourismus boomt in vielen Ländern.", "topic": "Tourismus"},
    {"sentence": "Das neue Gesetz soll die Umwelt schützen.", "topic": "Gesetz"},
    {"sentence": "Das Wetter spielt im Urlaub eine große Rolle.", "topic": "Wetter"},
    {"sentence": "Viele Menschen träumen von einem eigenen Haus.", "topic": "Haus"},
    {"sentence": "Das Essen im neuen Restaurant ist hervorragend.", "topic": "Essen"},
    {"sentence": "Die soziale Gerechtigkeit ist ein wichtiges Thema.", "topic": "Gerechtigkeit"},
    {"sentence": "Bildung ist der Schlüssel zu vielen Chancen.", "topic": "Bildung"},
    {"sentence": "Das Interesse an Geschichte nimmt zu.", "topic": "Geschichte"},
    {"sentence": "Neue Technologien können das Leben verbessern.", "topic": "Technologien"},
    {"sentence": "Sportliche Betätigung fördert die Gesundheit.", "topic": "Betätigung"},
    {"sentence": "Die Umwelt muss geschützt werden.", "topic": "Umwelt"},
    {"sentence": "Das neue Auto ist sehr umweltfreundlich.", "topic": "Auto"},
    {"sentence": "Viele Menschen lieben es zu reisen.", "topic": "reisen"},
    {"sentence": "Die Digitalisierung bietet viele Vorteile.", "topic": "Digitalisierung"},
    {"sentence": "Das neue Smartphone hat viele Funktionen.", "topic": "Smartphone"},
    {"sentence": "Musik spielt eine wichtige Rolle im Leben.", "topic": "Musik"},
    {"sentence": "Das Lernen neuer Sprachen erweitert den Horizont.", "topic": "Lernen"},
    {"sentence": "Der Einsatz von Robotern nimmt zu.", "topic": "Robotern"},
    {"sentence": "Der Umweltschutz ist eine dringende Aufgabe.", "topic": "Umweltschutz"},
    {"sentence": "Das Lesen fördert die Kreativität.", "topic": "Lesen"},
    {"sentence": "Das Kino bietet eine große Auswahl an Filmen.", "topic": "Kino"},
    {"sentence": "Die Künstliche Intelligenz verändert viele Branchen.", "topic": "Intelligenz"},
    {"sentence": "Das neue Gesetz tritt ab nächsten Monat in Kraft.", "topic": "Gesetz"},
    {"sentence": "Die Stadt investiert in den Ausbau des öffentlichen Nahverkehrs.", "topic": "Nahverkehrs"},
    {"sentence": "Nachhaltigkeit ist ein wichtiges Ziel.", "topic": "Nachhaltigkeit"},
    {"sentence": "Der Ausbau der Infrastruktur ist dringend notwendig.", "topic": "Infrastruktur"},
    {"sentence": "Das Bildungswesen steht vor großen Herausforderungen.", "topic": "Bildungswesen"},
    {"sentence": "Neue Bücher bereichern die Bibliothek.", "topic": "Bücher"},
    {"sentence": "Die Qualität des Wassers muss regelmäßig überprüft werden.", "topic": "Qualität"},
    {"sentence": "Das Wirtschaftswachstum ist in vielen Ländern positiv.", "topic": "Wachstum"},
    {"sentence": "Das Einkaufen im Internet wird immer beliebter.", "topic": "Einkaufen"},
    {"sentence": "Die Forschung im Bereich der Medizin macht Fortschritte.", "topic": "Forschung"},
    {"sentence": "Das Klima spielt eine wichtige Rolle in der Landwirtschaft.", "topic": "Klima"},
    {"sentence": "Das Essen in der neuen Kantine ist sehr lecker.", "topic": "Essen"},
    {"sentence": "Die Nachfrage nach Elektroautos steigt.", "topic": "Elektroautos"},
    {"sentence": "Das neue Theaterstück ist sehr unterhaltsam.", "topic": "Theaterstück"},
    {"sentence": "Der Ausbau erneuerbarer Energien ist wichtig.", "topic": "Ausbau"},
    {"sentence": "Das Recycling von Plastik ist notwendig.", "topic": "Recycling"},
    {"sentence": "Die Renovierung des alten Gebäudes kostet viel Geld.", "topic": "Renovierung"},
    {"sentence": "Der Schutz der Artenvielfalt ist entscheidend.", "topic": "Schutz"},
    {"sentence": "Das Lernen neuer Fähigkeiten ist wichtig.", "topic": "Fähigkeiten"},
    {"sentence": "Die Entwicklung der Technologie schreitet voran.", "topic": "Entwicklung"},
    {"sentence": "Das Lesen von Büchern fördert die Bildung.", "topic": "Lesen"},
    {"sentence": "Das Wachstum der Wirtschaft ist beeindruckend.", "topic": "Wachstum"},
    {"sentence": "Der Tourismus bringt viele Vorteile.", "topic": "Tourismus"},
    {"sentence": "Die Qualität der Luft in der Stadt ist schlecht.", "topic": "Qualität"},
    {"sentence": "Die sozialen Medien haben die Kommunikation verändert.", "topic": "Medien"},
    {"sentence": "Die Renovierung des Parks ist abgeschlossen.", "topic": "Renovierung"},
    {"sentence": "Das Reisen bildet den Geist.", "topic": "Reisen"},
    {"sentence": "Die Digitalisierung der Bildung hat viele Vorteile.", "topic": "Digitalisierung"},
    {"sentence": "Das Interesse an Fotografie wächst.", "topic": "Fotografie"},
    {"sentence": "Die Organisation des Events war hervorragend.", "topic": "Organisation"},
    {"sentence": "Das Studium an der Universität ist sehr anspruchsvoll.", "topic": "Studium"},
    {"sentence": "Die Nachhaltigkeit ist ein langfristiges Ziel.", "topic": "Nachhaltigkeit"},
    {"sentence": "Der Einsatz von Technologie in Schulen nimmt zu.", "topic": "Technologie"},
    {"sentence": "Die Preise für Lebensmittel steigen.", "topic": "Preise"},
    {"sentence": "Das Lernen im Ausland bietet viele Chancen.", "topic": "Lernen"},
    {"sentence": "Im Sommer steigen die Temperaturen oft über 30 Grad.", "topic": "Temperaturen"},
    {"sentence": "Die neue Software verbessert die Effizienz im Büro.", "topic": "Software"},
    {"sentence": "Viele Menschen nutzen öffentliche Verkehrsmittel.", "topic": "Verkehrsmittel"},
    {"sentence": "Die Lehrer bereiten die Schüler auf die Prüfungen vor.", "topic": "Lehrer"},
    {"sentence": "Das Museum zeigt eine Ausstellung moderner Kunst.", "topic": "Ausstellung"},
    {"sentence": "Im Herbst fallen die Blätter von den Bäumen.", "topic": "Blätter"},
    {"sentence": "Das Internet hat die Art und Weise der Kommunikation verändert.", "topic": "Internet"},
    {"sentence": "Die Ärzte empfehlen regelmäßige Vorsorgeuntersuchungen.", "topic": "Ärzte"},
    {"sentence": "Im Winter locken die Berge viele Skifahrer an.", "topic": "Berge"},
    {"sentence": "Die Umweltverschmutzung ist ein großes Problem in Großstädten.", "topic": "Umweltverschmutzung"},
    {"sentence": "Das neue Restaurant bietet exotische Gerichte an.", "topic": "Restaurant"},
    {"sentence": "Im Frühling blühen die Blumen in allen Farben.", "topic": "Blumen"},
    {"sentence": "Viele Studenten arbeiten nebenbei in Teilzeitjobs.", "topic": "Studenten"},
    {"sentence": "Das Konzert war ein großer Erfolg.", "topic": "Konzert"},
    {"sentence": "Die neuen Smartphones haben viele innovative Funktionen.", "topic": "Smartphones"},
    {"sentence": "Die Eltern kümmern sich liebevoll um ihre Kinder.", "topic": "Eltern"},
    {"sentence": "Im Supermarkt gibt es eine große Auswahl an Bio-Produkten.", "topic": "Supermarkt"},
    {"sentence": "Die Polizei ermittelt in einem schwierigen Fall.", "topic": "Polizei"},
    {"sentence": "Die Musik beruhigt und entspannt nach einem stressigen Tag.", "topic": "Musik"},
    {"sentence": "Das Buch handelt von einer abenteuerlichen Reise.", "topic": "Buch"},
    {"sentence": "Die Stadt plant den Bau einer neuen Brücke.", "topic": "Stadt"},
    {"sentence": "Das Kino zeigt diese Woche viele interessante Filme.", "topic": "Kino"},
    {"sentence": "Die Gesundheitsbehörden warnen vor einer Grippewelle.", "topic": "Gesundheitsbehörden"},
    {"sentence": "Im Zoo können Besucher viele exotische Tiere sehen.", "topic": "Zoo"},
    {"sentence": "Das neue Gesetz soll die Umwelt schützen.", "topic": "Gesetz"},
    {"sentence": "Die Schüler freuen sich auf die Sommerferien.", "topic": "Schüler"},
    {"sentence": "Der Park ist ein beliebter Ort für Spaziergänge.", "topic": "Park"},
    {"sentence": "Im Herbst beginnt die Weinlese in den Weinbergen.", "topic": "Weinlese"},
    {"sentence": "Das Unternehmen expandiert in internationale Märkte.", "topic": "Unternehmen"},
    {"sentence": "Der Arzt verschreibt dem Patienten ein neues Medikament.", "topic": "Arzt"},
    {"sentence": "Die Technik entwickelt sich rasant weiter.", "topic": "Technik"},
    {"sentence": "Das Theaterstück erhielt hervorragende Kritiken.", "topic": "Theaterstück"},
    {"sentence": "Im Winter freuen sich viele auf den ersten Schnee.", "topic": "Schnee"},
    {"sentence": "Die Politiker diskutieren über die neuen Reformen.", "topic": "Politiker"},
    {"sentence": "Der Hund spielt gerne im Garten.", "topic": "Hund"},
    {"sentence": "Die Bibliothek bietet eine Vielzahl an Büchern und Zeitschriften.", "topic": "Bibliothek"},
    {"sentence": "Das Auto wurde gestern repariert.", "topic": "Auto"},
    {
      "sentence": "Sie waren aber alle beide fromm vor Gott und wandelten in allen Geboten und Satzungen des Herrn untadelig.",
      "topic": "Sie"
    },
    {
      "sentence": "Und sie hatten kein Kind, denn Elisabeth war unfruchtbar.",
      "topic": "sie"
    },
    {
      "sentence": "Und es begab sich, da er des Priesteramts waltete vor Gott, als seine Ordnung an der Reihe war.",
      "topic": "er"
    },
    {
      "sentence": "Er traf ihn nach dem Brauch der Priesterschaft das Los, zu räuchern; und er ging in den Tempel des Herrn.",
      "topic": "er"
    },
    {
   "sentence": "Und die ganze Menge des Volks war draußen und betete zur Stunde des Räucherns.",
      "topic": "Menge des Volks"
    },
    {
      "sentence": "Es erschien ihm aber ein Engel des Herrn und stand zur rechten Hand am Räucheraltar.",
      "topic": "Engel"
    },
    {
      "sentence": "Und als Zacharias ihn sah, erschrak er, und es kam ihn eine Furcht an.",
      "topic": "Zacharias"
    },
    {
      "sentence": "Ich stand im Gespräch mit einem Bekannten etwas abseits von diesem Getümmel auf dem Promenadendeck, als neben uns zwei- oder dreimal Blitzlicht scharf aufsprühte – anscheinend war irgend-ein Prominenter knapp vor der Abfahrt noch rasch von Reportern interviewt und photographiert worden.",
      "topic": "Prominenter"
    },
    {
      "sentence": "Mein Freund blickte hin und lächelte.",
      "topic": "Freund"
    },
    {
      "sentence": "Sie haben da einen raren Vogel an Bord, den Czentovic.",
      "topic": "Czentovic"
    },
    {
      "sentence": "Und da ich offenbar ein ziemlich verständnisloses Gesicht zu dieser Mitteilung machte, fügte er erklärend bei:",
      "topic": "ich"
    },
    {
      "sentence": "Mirko Czentovic, der Weltschachmeister.",
      "topic": "Czentovic"
    },
    {
      "sentence": "Er hat ganz Amerika von Ost nach West mit Turnierspielen abgeklappert und fährt jetzt zu neuen Triumphen nach Argentinien.",
      "topic": "Czentovic"
    },

    {
      "sentence": "Die Zahl der Fachpublikationen ist in der akademischen Welt eine wichtige Größe.",
      "topic": "Zahl der Fachpublikationen"
    },
    {
      "sentence": "Wer viel veröffentlicht, hat offenbar viel Neues herausgefunden, er kommt leichter in gute Positionen, kann Karriere machen.",
      "topic": "Wer"
    },
    {
      "sentence": "In der Branche hat sich daher das Konzept der kleinsten publizierbaren Einheit durchgesetzt - jeder Fitzel neuer Erkenntnis wird veröffentlicht.",
      "topic": "Konzept"
    },
    {
      "sentence": "Zum Erfolg der chinesischen Wissenschaft trägt offenbar aber auch eine äußerst fragwürdige Publikationspraxis bei.",
      "topic": "Publikationspraxis"
    },
    {
      "sentence": "In dem Land beeinflusst die Publikationsliste die Karrierechancen besonders stark.",
      "topic": "Publikationsliste"
    },
    {
      "sentence": "Auch die dort erwähnte Social-Priming-Theorie existiert tatsächlich, wenngleich sie umstritten ist: Diese Theorie besagt, dass Menschen, die zuvor unbewusst für ein bestimmtes Thema sensibilisiert wurden, anschließend entsprechende körperliche Reaktionen zeigen können.",
      "topic": "Social-Priming-Theorie"
    },
    {
      "sentence": "So bewegten sich Menschen langsamer, wenn sie zuvor mit dem Thema Altern in Berührung kamen - etwa durch Bilder, die ihnen gezeigt wurden.",
      "topic": "Menschen"
    },
    {
      "sentence": "In einer weiteren Studie schrieben Forscher: Wer mit einem Stift zwischen den Zähnen Comics anschaut und so unbewusst ein Lächeln nachahmt, findet die Cartoons lustiger.",
      "topic": "Wer"
    },
    {
      "sentence": "Doch was Lewis auf Grundlage der Theorie angeblich untersucht hat, klingt dann doch ziemlich absurd.",
      "topic": "Lewis"
    },
    {
      "sentence": "Kurz gefasst geht es darum, ob die politischen Vorlieben eines Menschen einen Einfluss darauf haben, mit welcher Hand er sich auf der Toilette den Hintern abwischt.",
      "topic": "politischen Vorlieben"
    },
    {
      "sentence": "Nehmen linke Politiker nur die linke Hand?",
      "topic": "linke Politiker"
    } ,
 
    {
      "sentence": "Wissenschaftliche Publikationen sollen künftig für jeden leichter zugänglich sein. Das Bundesforschungsministerium startete dazu am Dienstag eine Open-Access-Strategie, damit Veröffentlichungen der Allgemeinheit unentgeltlich über das Internet zur Verfügung gestellt werden.",
      "topic": "Wissenschaftliche Publikationen"
    },
    {
      "sentence": "\"Freier Zugang zu Wissen ist ein Sprungbrett für die gesellschaftliche Entwicklung\", erklärte Forschungsministerin Johanna Wanka (CDU).",
      "topic": "Zugang"
    },
    {
        "sentence": "Zu der Strategie gehört etwa eine Klausel für alle durch das Forschungsministerium geförderten Projekte. Wissenschaftliche Artikel zu diesen Projekten sollen demnach entweder gleich unter einem Open-Access-Modell publiziert oder nach Ablauf einer Embargofrist in einen geeigneten Dokumentenserver eingestellt werden können.",
      "topic": "Strategie"
    },
    {
      "sentence": "Das Ministerium will zudem Länder, Hochschulen und Forschungseinrichtungen beim Ausbau ihrer Aktivitäten in diesem Bereich unterstützen.",
      "topic": "Ministerium"
    },
    {
      "sentence": "Am Rande eines großen Waldes wohnte ein armer Holzhacker mit seiner Frau und seinen zwei Kindern, Hänsel und Gretel.",
      "topic": "Holzhacker"
    },
    {
      "sentence": "Sie waren so arm, dass sie oft nichts zu essen hatten.",
      "topic": "sie"
    },
    {
      "sentence": "Als nun eine Teuerung kam, mussten sie jeden Abend hungrig zu Bett gehen.",
      "topic": "sie"
    },
    {
      "sentence": "In ihrer Not beschlossen die Eltern, die Kinder am nächsten Morgen in den Wald zu führen und sie dort zurückzulassen.",
      "topic": "Eltern"
    },
    {
      "sentence": "Gott sollte ihnen weiter helfen. Aber Hänsel schlief nicht und hörte alles.",
      "topic": "Hänsel"
    },
    {
      "sentence": "Am nächsten Tag, als sie in den Wald gingen, streute er kleine Steinchen auf den Weg.",
      "topic": "Hänsel"
    },
    {
      "sentence": "Die Kinder blieben im Wald zurück, aber sie konnten durch die Steinchen den Rückweg ins Elternhaus finden.",
      "topic": "Kinder"
    },
    {
      "sentence": "Ein anderes Mal, als die Not wieder groß war, wollten die Eltern ihre Kinder wieder in den Wald führen.",
      "topic": "Eltern"
    },
    {
      "sentence": "Hänsel hörte wieder alles und wollte nachts heimlich Steinchen sammeln, um sie auf den Weg zu streuen.",
      "topic": "Hänsel"
    },
    {
      "sentence": "Aber die Haustür war verschlossen.",
      "topic": "Haustür"
    },
    {
      "sentence": "Am nächsten Tag nahm er sein letztes Stück Brot und streute kleine Bröckchen davon auf den Weg.",
      "topic": "Hänsel"
    },
    {
      "sentence": "Die Kinder blieben allein im Wald zurück.",
      "topic": "Kinder"
    },
    {
      "sentence": "Sie suchten nach den Brotbröckchen; aber die Vögel hatten alle aufgepickt.",
      "topic": "Vögel"
    },
    {
      "sentence": "So fanden Hänsel und Gretel ihren Weg nach Haus nicht mehr und verirrten sich immer mehr im Wald.",
      "topic": "Hänsel und Gretel"
    },
    {
      "sentence": "Sie schliefen unter einem Baum, und am nächsten Morgen standen sie hungrig auf, um weiter nach dem Weg zu suchen.",
      "topic": "sie"
    },
    {
      "sentence": "Plötzlich sahen sie ein seltsames kleines Häuschen.",
      "topic": "sie"
    },
    {
      "sentence": "Es war aus Brot gebaut, das Dach war mit süßen Kuchen gedeckt und die Fenster waren aus hellem Zucker.",
      "topic": "Häuschen"
    },
    {
    "sentence": "Voll Freude brachen sich die hungrigen Kinder Stücke von dem Dach ab und bissen hinein.",
      "topic": "Kinder"
    },
    {
      "sentence": "Da öffnete sich plötzlich die Tür, und eine hässliche, steinalte Frau mit einem Stock kam heraus.",
      "topic": "Tür"
    },
    {
      "sentence": "Die Kinder erschraken furchtbar, aber die Alte wackelte mit dem Kopf und sagte ganz freundlich: Ei, ihr lieben Kinder, kommt nur in mein Häuschen und bleibt bei mir.",
      "topic": "Alte"
    },

    {
      "sentence": "Es war einmal ein kleines süßes Mädchen, das hatte jeder lieb, am allerliebsten ihre Großmutter.",
      "topic": "Mädchen"
    },
    {
      "sentence": "Einmal schenkte die Großmutter dem Mädchen ein rotes Käppchen, und weil das Mädchen dieses Käppchen nicht mehr absetzen wollte, hieß es nur das Rotkäppchen.",
      "topic": "Großmutter"
    },
    {
      "sentence": "Eines Tages sprach ihre Mutter zu ihr: \"Komm, Rotkäppchen, da hast du ein Stück Kuchen und eine Flasche Wein, bring das der Großmutter.",
      "topic": "Mutter"
    },
    {
      "sentence": "Sie ist krank und schwach.",
      "topic": "Sie"
    },
    {
      "sentence": "Mach dich auf, bevor es heiß wird und lauf nicht vom Wege ab, sonst fällst du und zerbrichst das Glas, und die Großmutter hat nichts.\"",
      "topic": "Wege"
    },
    {
      "sentence": "\"Ich will schon alles richtig machen,\" versprach Rotkäppchen ihrer Mutter.",
      "topic": "Rotkäppchen"
    },
    {
      "sentence": "Die Großmutter wohnte draußen im Wald, eine halbe Stunde vom Dorf.",
      "topic": "Großmutter"
    },
    {
      "sentence": "Als nun Rotkäppchen in den Wald kam, begegnete ihr der Wolf.",
      "topic": "Rotkäppchen"
    },
    {
      "sentence": "Rotkäppchen aber wusste nicht, was das für ein böses Tier war, und fürchtete sich nicht vor ihm.",
      "topic": "Tier"
    },
    {
      "sentence": "\"Guten Tag, Rotkäppchen!\" sprach er.",
      "topic": "Rotkäppchen"
    },
    {
      "sentence": "\"Schönen Dank, Wolf!\"",
      "topic": "Wolf"
    },
    {
      "sentence": "\"Wo willst du so früh hin, Rotkäppchen?\"",
      "topic": "Rotkäppchen"
    },
    {
      "sentence": "\"Kuchen und Wein. Das soll ich der Großmutter bringen.\"",
      "topic": "Großmutter"
    },
    {
      "sentence": "Der Wolf dachte bei sich: Das junge, zarte Rotkäppchen, das ist ein leckerer Bissen.",
      "topic": "Wolf"
    },
    {
      "sentence": "Du musst es listig anfangen, damit du beide schnappst.",
      "topic": "Du"
    },
    {
      "sentence": "Er sprach: \"Rotkäppchen, sieh einmal die schönen Blumen, die ringsumher stehen.",
      "topic": "Blumen"
    },
    {
      "sentence": "Warum pflückst du deiner Großmutter nicht einen Strauß davon?\"",
      "topic": "Großmutter"
    },
    {
      "sentence": "Da dachte sich Rotkäppchen: Wenn ich der Großmutter einen frischen Strauß mitbringe, der wird ihr auch Freude machen.",
      "topic": "Rotkäppchen"
    },
    {
      "sentence": "Sie lief vom Wege ab in den Wald hinein und suchte Blumen.",
      "topic": "Blumen"
    },
    {
      "sentence": "Der Wolf aber ging geradewegs zu dem Haus der Großmutter und klopfte an die Türe.",
      "topic": "Wolf"
    },
    {
      "sentence": "\"Wer ist draußen?\"",
      "topic": "Wer"
    },
    {
      "sentence": "\"Rotkäppchen, das bringt Kuchen und Wein, mach auf!\"",
      "topic": "Rotkäppchen"
    },
    {
      "sentence": "\"Drück nur auf die Klinke!\" rief die Großmutter, \"ich bin zu schwach und kann nicht aufstehen.\"",
      "topic": "Großmutter"
    },
    {
      "sentence": "Der Wolf drückte auf die Klinke, die Türe sprang auf und er ging, ohne ein Wort zu sprechen, gerade zum Bett der Großmutter und verschluckte sie.",
      "topic": "Wolf"
    },
    {
      "sentence": "Dann zog er ihre Kleider an, setzte ihre Haube auf und legte sich in ihr Bett.",
      "topic": "Kleider"
    },
    {
      "sentence": "Rotkäppchen kam nun mit einem Blumenstrauß vor dem Haus der Großmutter an und wunderte sich, dass die Tür aufstand.",
      "topic": "Rotkäppchen"
    },
    {
      "sentence": "Es rief: \"Guten Morgen,\" bekam aber keine Antwort.",
      "topic": "Es"
    },
    {
      "sentence": "Darauf ging es zum Bett.",
      "topic": "Bett"
    },
    {
      "sentence": "Da lag die Großmutter und hatte die Haube tief ins Gesicht gezogen und sah so seltsam aus.",
      "topic": "Großmutter"
    },
    {
      "sentence": "Es war einmal in einem kleinen Dorf in den Bergen, tief versteckt zwischen dichten Wäldern und glitzernden Seen, wo ein Junge namens Emil lebte.",
      "topic": "Emil"
    },
    {
      "sentence": "Emil war für seine unerschöpfliche Neugier und seinen freien Geist bekannt und lebte mit seiner Familie in einem kleinen, gemütlichen Haus am Rande des Dorfes.",
      "topic": "Emil"
    },
    {
      "sentence": "Seine Familie lebte einfach, aber glücklich, umgeben von Natur und Gemeinschaft.",
      "topic": "Familie"
    },
    {
      "sentence": "Eines Morgens, als der Tau noch frisch auf den Feldern lag, beschloss Emil, tiefer in den Wald zu gehen als je zuvor.",
      "topic": "Emil"
    },
    {
      "sentence": "Sein Vater hatte ihm oft von den alten Legenden erzählt, die in diesen Wäldern verborgen waren, Geschichten von geheimnisvollen Wesen und magischen Orten, die nur darauf warteten, entdeckt zu werden.",
      "topic": "Vater"
    },
    {
      "sentence": "Bewaffnet mit einem kleinen Rucksack, einem Kompass und einer großen Portion Mut machte sich Emil auf den Weg.",
      "topic": "Emil"
    },
    {
      "sentence": "Der Wald begrüßte ihn mit dem Rauschen der Blätter und dem Zwitschern der Vögel.",
      "topic": "Wald"
    },
    {
      "sentence": "Je weiter er ging, desto dichter und mysteriöser wurde der Wald.",
      "topic": "Wald"
    },
    {
      "sentence": "Nach einigen Stunden des Wanderns entdeckte Emil eine verborgene Lichtung, die von der Sonne erhellt wurde und in der Mitte ein alter, von Moos bedeckter Stein stand.",
      "topic": "Emil"
    },
    {
      "sentence": "Auf dem Stein waren seltsame Symbole eingraviert, die wie eine alte, vergessene Sprache aussahen.",
      "topic": "Stein"
    },
    {
      "sentence": "Emil war fasziniert und spürte, dass der Stein wichtig sein musste.",
      "topic": "Emil"
    },
    {
      "sentence": "Plötzlich hörte er ein leises Summen, welches die Luft erfüllte.",
      "topic": "Summen"
    },
    {
      "sentence": "Es schien von dem Stein selbst zu kommen.",
      "topic": "Stein"
    },
    {
      "sentence": "Als er seine Hand auf die kalte, feuchte Oberfläche legte, flackerte das Summen auf und wurde zu einer Melodie, die sich irgendwie vertraut anfühlte.",
      "topic": "Melodie"
    },
    {
      "sentence": "Es war, als würde der Wald selbst zu ihm sprechen.",
      "topic": "Wald"
    },
    {
      "sentence": "Emil zog seinen Notizblock und begann, die Symbole schnell zu skizzieren, in der Hoffnung, mehr über ihre Bedeutung zu erfahren.",
      "topic": "Emil"
    },
    {
      "sentence": "Kaum hatte er die letzten Linien gezeichnet, öffnete sich plötzlich ein verborgener Pfad hinter dem Stein, der zuvor von Dickicht und Moos verdeckt gewesen war.",
      "topic": "Pfad"
    },
    {
      "sentence": "Ohne zu zögern folgte Emil dem Pfad, der ihn tiefer und tiefer in einen Teil des Waldes führte, den selbst die Sonne nicht durchdringen konnte.",
      "topic": "Emil"
    },
    {
      "sentence": "Nach einer Weile erreichte er ein altes, verfallenes Schloss, das von der Natur fast vollständig zurückerobert worden war.",
      "topic": "Schloss"
    },
    {
      "sentence": "Die Tür stand offen, als würde sie auf ihn warten.",
      "topic": "Tür"
    },
    {
      "sentence": "Im Innern des Schlosses entdeckte Emil einen großen Saal, in dessen Mitte ein glänzender Kristall auf einem Altar ruhte.",
      "topic": "Emil"
    },
    {
      "sentence": "Das Licht, das durch die gebrochenen Fenster fiel, ließ den Kristall in allen Farben schimmern.",
      "topic": "Licht"
    },
    {
      "sentence": "Als er näher trat, fühlte er eine warme, einladende Energie, die von dem Kristall ausging.",
      "topic": "Kristall"
    },
    {
      "sentence": "Ohne es zu merken, hatte die Sonne begonnen, sich zu senken, und das Licht im Saal wurde schwächer.",
      "topic": "Sonne"
    },
    {
      "sentence": "Emil wusste, dass er bald den Heimweg antreten sollte, aber der Kristall schien ihm etwas mitteilen zu wollen.",
      "topic": "Emil"
    },
    {
      "sentence": "Er legte erneut seine Hand darauf, und in diesem Moment erfüllte ein helles Leuchten den Raum.",
      "topic": "Hand"
    },
    {
      "sentence": "Als das Licht nachließ, sah Emil, dass sich im Kristall Szenen aus der Vergangenheit des Dorfes abspielten.",
      "topic": "Kristall"
    },

    {
      "sentence": "Meine sehr geehrten Damen und Herren,",
      "topic": "Damen und Herren"
    },
    {
      "sentence": "ich freue mich sehr, heute hier zu sein und vor Ihnen, den Menschen, die das Herz und die Seele unserer Nation bilden, sprechen zu dürfen.",
      "topic": "Nation"
    },
    {
      "sentence": "Wir stehen heute an einem entscheidenden Punkt in unserer Geschichte, einem Punkt, an dem die Entscheidungen, die wir treffen, und die Maßnahmen, die wir ergreifen, den Weg in unsere Zukunft bestimmen werden.",
      "topic": "Zukunft"
    },
    {
      "sentence": "Es ist eine Zeit gekommen, in der das Wohl des Einzelnen und das Wohl der Gemeinschaft untrennbar miteinander verbunden sind.",
      "topic": "Gemeinschaft"
    },
    {
      "sentence": "In einer Ära der Globalisierung und technologischen Revolutionen müssen wir sicherstellen, dass niemand zurückgelassen wird.",
      "topic": "Globalisierung"
    },
    {
      "sentence": "Unsere Politik muss inklusiv, gerecht und nachhaltig sein.",
      "topic": "Politik"
    },
    {
      "sentence": "Wir leben in einer Zeit großer Herausforderungen, aber auch großer Chancen.",
      "topic": "Herausforderungen"
    },
    {
      "sentence": "Die Welt kämpft mit einer Klimakrise, die unsere Umwelt, unsere Gesundheit und unsere Wirtschaft bedroht.",
      "topic": "Klimakrise"
    },
    {
      "sentence": "Wir können und dürfen nicht untätig bleiben.",
      "topic": "Untätigkeit"
    },
    {
      "sentence": "Unsere Antwort auf diese Krise wird nicht nur zeigen, wie wir die Umwelt schätzen, sondern auch, wie wir zukünftigen Generationen gegenübertreten.",
      "topic": "Umwelt"
    },
    {
      "sentence": "Daher verpflichte ich mich dem Ziel, bis 2030 eine klimaneutrale Politik zu verfolgen.",
      "topic": "klimaneutrale Politik"
    },
    {
      "sentence": "Wir werden in erneuerbare Energien investieren, unsere Verkehrssysteme modernisieren und nachhaltige Technologien fördern.",
      "topic": "erneuerbare Energien"
    },
    {
      "sentence": "Jeder Euro, der in diese Bereiche fließt, ist eine Investition in eine saubere und sichere Zukunft.",
      "topic": "Investition"
    },
    {
      "sentence": "Aber Umwelt ist nicht unser einziges Anliegen.",
      "topic": "Umwelt"
    },
    {
      "sentence": "Bildung ist der Schlüssel zur Freiheit und zur Zukunftsfähigkeit unseres Landes.",
      "topic": "Bildung"
    },
    {
      "sentence": "Jedes Kind verdient Zugang zu erstklassiger Bildung – unabhängig von seiner Herkunft oder dem Einkommen seiner Eltern.",
      "topic": "Bildung"
    },
    {
      "sentence": "Wir werden unsere Schulen besser ausstatten, Lehrpläne modernisieren und digitale Bildung flächendeckend einführen.",
      "topic": "Schulen"
    },
    {
    "sentence": "Die Digitalisierung bietet unermessliche Möglichkeiten, birgt aber auch Risiken.",
      "topic": "Digitalisierung"
    },
    {
      "sentence": "Datenschutz und die Sicherheit unserer Bürger im Netz sind oberste Priorität.",
      "topic": "Datenschutz"
    },
    {
      "sentence": "Wir werden strenge Richtlinien einführen, um persönliche Daten zu schützen und gleichzeitig die Freiheit des Internets zu gewährleisten.",
      "topic": "persönliche Daten"
    },
    {
      "sentence": "Sicherheit und Wohlstand für alle – das ist unser Ziel.",
      "topic": "Sicherheit"
    },
    {
      "sentence": "Das bedeutet auch, dass wir den Mittelstand stärken, der das Rückgrat unserer Wirtschaft bildet.",
      "topic": "Mittelstand"
    },
    {
      "sentence": "Kleine und mittlere Unternehmen benötigen unsere Unterstützung, um wettbewerbsfähig zu bleiben und Arbeitsplätze zu schaffen.",
      "topic": "kleine und mittlere Unternehmen"
    },
    {
      "sentence": "Wir werden bürokratische Hürden abbauen und Innovationen fördern.",
      "topic": "Innovationen"
    },
    {
      "sentence": "Gleichberechtigung und Gerechtigkeit sind Grundpfeiler unserer Gesellschaft.",
      "topic": "Gleichberechtigung"
    },
    {
      "sentence": "Wir werden aktiv gegen jede Form von Diskriminierung vorgehen und sicherstellen, dass jeder in diesem Land die gleichen Chancen hat, unabhängig von Geschlecht, Herkunft oder Religion.",
      "topic": "Diskriminierung"
    },
    {
      "sentence": "Die Sicherheit unseres Landes und seiner Bürger steht immer an erster Stelle.",
      "topic": "Sicherheit"
    },
    {
      "sentence": "Wir leben in einer Welt, in der neue Bedrohungen unsere Aufmerksamkeit erfordern.",
      "topic": "Bedrohungen"
    },
    {
      "sentence": "Unsere Streitkräfte müssen modern und effektiv sein, bereit, jeden zu schützen, der unter unserer Flagge lebt.",
      "topic": "Streitkräfte"
    },
    {
      "sentence": "Ich bitte Sie alle, mit mir auf diesem Weg zu gehen.",
      "topic": "Weg"
    },
    {
      "sentence": "Ein Weg, der Herausforderungen niemals scheut, sondern Chancen ergreift.",
      "topic": "Weg"
    },
    {
      "sentence": "Ein Weg, auf dem wir gemeinsam eine bessere, gerechtere und nachhaltigere Zukunft für uns alle schaffen.",
      "topic": "Zukunft"
    },
    {
      "sentence": "Vielen Dank für Ihr Vertrauen, Ihre Unterstützung und Ihren unermüdlichen Einsatz.",
      "topic": "Vertrauen"
    },
    {
      "sentence": "Gemeinsam werden wir nicht nur überstehen, sondern gedeihen.",
      "topic": "Gemeinsamkeit"
    },
    {
      "sentence": "Lassen Sie uns mutig und entschlossen sein und zusammen die Zukunft gestalten, die unser Land verdient.",
      "topic": "Zukunft"
    },
    {
      "sentence": "Vielen Dank.",
      "topic": "Dank"
    },
 
    {
      "sentence": "Schwertwale, auch bekannt als Orcas, gehören zu den mächtigsten Raubtieren in den Ozeanen.",
      "topic": "Schwertwael"
    },
    {
      "sentence": "Mit ihrer charakteristischen schwarz-weißen Färbung zählen sie zur Familie der Delfine, von denen sie die größten Mitglieder sind.",
      "topic": "Familie der Delfine"
    },
    {
      "sentence": "Orcas sind äußerst soziale Wesen, die in Familienverbänden, den sogenannten Pods, leben.",
      "topic": "soziale Wesen"
    },
    {
      "sentence": "Diese können manchmal Dutzende von Individuen umfassen.",
      "topic": "Dutzende von Individuen"
    },
    {
      "sentence": "Diese Pods sind nicht nur zufällige Ansammlungen; sie repräsentieren komplexe soziale Strukturen, die für ihr Überleben und ihren Alltag von entscheidender Bedeutung sind.",
      "topic": "komplexe soziale Strukturen"
    },
    {
      "sentence": "Die Intelligenz der Schwertwale ist bemerkenswert.",
      "topic": "Intelligenz"
    },
    {
      "sentence": "Sie haben große Gehirne und zeigen Verhaltensweisen, die auf hohe kognitive Fähigkeiten hinweisen, vergleichbar mit denen einiger Primaten.",
      "topic": "hohe kognitive Fähigkeiten"
    },
    {
      "sentence": "Diese Intelligenz zeigt sich in ihren Jagdstrategien.",
      "topic": "Intelligenz"
    },
    {
      "sentence": "Orcas sind dafür bekannt, koordinierte Jagdtaktiken zu verwenden, was sie zu den Wölfen des Meeres macht.",
      "topic": "koordinierte Jagdtaktiken"
    },
    {
      "sentence": "Sie nutzen vokale Kommunikation, um sich untereinander zu koordinieren, und können eine breite Palette von Beutetieren jagen, inklusive Fische, Robben und sogar viel größere Wale.",
      "topic": "vokale Kommunikation"
    },
    {
      "sentence": "Eine der bemerkenswertesten Jagdtechniken, die bei Orcas beobachtet wurde, ist ihre Fähigkeit, Wellen zu erzeugen, um Seehunde von Eisschollen ins Wasser zu stoßen.",
      "topic": "Jagdtechniken"
    },
    {
      "sentence": "Sie schwimmen schnell auf das Eis zu und arbeiten zusammen, um eine Welle zu erzeugen, die über das Eis schwemmt und den Seehund ins Meer spült, wo andere Mitglieder des Pods warten, um ihn zu fangen.",
      "topic": "Zusammenarbeit"
    },
    {
      "sentence": "Dies zeigt nicht nur ihre Intelligenz, sondern auch ihre Fähigkeit zur Zusammenarbeit und Problemlösung.",
      "topic": "Zusammenarbeit"
    },
    {
      "sentence": "Neben ihrer Jagdkompetenz sind Schwertwale auch für ihre Laute bekannt, die Klicks, Pfeiftöne und Impulse umfassen.",
      "topic": "Laute"
    },
    {
      "sentence": "Jeder Pod hat seinen eigenen Dialekt, eine Reihe von Lauten, die spezifisch für bestimmte Gruppen sind und über Generationen weitergegeben werden.",
      "topic": "eigener Dialekt"
    },
    {
      "sentence": "Diese Laute sind entscheidend für die Kommunikation, insbesondere in den trüben Gewässern des Ozeans, wo die Sichtbarkeit begrenzt ist.",
      "topic": "Kommunikation"
    },
    {
      "sentence": "Die soziale Struktur der Schwertwal-Pods ist matriarchalisch; das heißt, die Gruppen werden in der Regel von einem älteren Weibchen angeführt.",
      "topic": "soziale Struktur"
    },
    {
      "sentence": "Dieses Matriarchat spielt eine Schlüsselrolle im Pod, indem es die Gruppe während der Reisen und auf der Jagd anführt.",
      "topic": "Matriarchat"
    },
    {
      "sentence": "Die sozialen Bindungen in diesen Pods sind unglaublich stark, wobei die Nachkommen oft ihr ganzes Leben lang bei ihren Müttern bleiben.",
      "topic": "soziale Bindungen"
    },
    {
      "sentence": "Schwertwale zeigen eine Vielzahl von Verhaltensweisen, die auf ihre komplexen Gesellschaften hinweisen.",
      "topic": "komplexe Gesellschaften"
    },
    {
      "sentence": "Es ist bekannt, dass sie einander neue Jagdmethoden beibringen und sogar beobachtet wurde, wie sie Nahrung unter den Podmitgliedern teilen, was ein Zeichen für ihr ausgefeiltes soziales Verhalten ist.",
      "topic": "soziales Verhalten"
    },
    {
      "sentence": "Spielverhalten ist häufig, und junge Kälber sind oft beim Springen, Schwanzschlagen und Spy-Hopping zu sehen, während sie von ihren Älteren lernen.",
      "topic": "Spielverhalten"
    },
    {
      "sentence": "Trotz ihres Namens haben Schwertwale in freier Wildbahn historisch gesehen wenig Aggression gegenüber Menschen gezeigt.",
      "topic": "Aggression"
    },
    {
      "sentence": "In Gefangenschaft wurden jedoch mehrere Unfälle mit Orcas registriert, die einige Forscher auf den Stress und das psychologische Trauma zurückführen, das mit der Gefangenschaft einhergeht.",
      "topic": "Unfälle"
    },
    {
      "sentence": "Die Naturschutzbemühungen für Schwertwale stehen vor mehreren Herausforderungen.",
      "topic": "Naturschutzbemühungen"
    },
    {
      "sentence": "Sie werden häufig durch menschliche Aktivitäten beeinträchtigt, wie etwa durch Meeresverschmutzung und Lärm, der ihre natürliche Kommunikation stört.",
      "topic": "Meeresverschmutzung"
    },
    {
      "sentence": "Trotz internationaler Bemühungen und Schutzmaßnahmen bleibt der Erhalt dieser beeindruckenden Meeressäuger eine fortwährende Herausforderung.",
      "topic": "Schutzmaßnahmen"
    },
    {
      "sentence": "Es ist von entscheidender Bedeutung, dass wir unseren Einfluss auf ihre Lebensräume reduzieren und weiterhin Wege zur Koexistenz und zum Schutz dieser majestätischen Tiere finden.",
      "topic": "Lebensräume"
    }
  ]
























#save_file = open("chatgpt_german_data.json", "w", encoding='utf-8')  
#json.dump(data, save_file)  
#save_file.close() 



#exit()
def topic_pos(data):
    l_data_with_pos = []
    for i,d in enumerate(data):
        if i>4:
            break
        l_sent_split = d["sentence"].split()
        #print(l_sent_split)
        l_sent_split[-1] = l_sent_split[-1][:-1] #remove end ponctuation
        try:
            pos = l_sent_split.index(d["topic"])
        except ValueError:
            pos = None
        if pos!=None:
            d["topic_idx"] = pos
            d["sent_len"] = len(l_sent_split)
        #print(d)
        l_data_with_pos.append(d)
    return l_data_with_pos


def gpt_to_list_for_hug_format(data, idx_shift = 0):
    l_data_with_pos = topic_pos(data)
    l_sent_train,l_labels_train, l_id_train = [], [], []
    for i,d in enumerate(l_data_with_pos):
        l_sent_train.append(d["sentence"])
        l_id_train.append(i+idx_shift)
        labels = [0]*d["sent_len"]
        print()
        labels[d["topic_idx"]] = 1
        l_labels_train.append(labels)
    
    return l_sent_train,l_labels_train, l_id_train

#print(gpt_to_list_for_hug_format(data))




    





