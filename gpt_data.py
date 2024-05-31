import json


data_tales = [
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






data_UD = [

    {
      "sentence": "Der Friseursalon ist mit dem Bus sehr gut zu erreichen.",
      "topic": "Friseursalon"
    },
    {
      "sentence": "Terminfestlegung am Vortag war kein Problem; keine Wartezeiten.",
      "topic": "Terminfestlegung"
    },
    {
      "sentence": "Die Mitarbeiter waren sehr freundlich und es herrschte eine nette Stimmung im ganzen Salon.",
      "topic": "Mitarbeiter"
    },
    {
      "sentence": "Das Haareschneiden war auch schnell erledigt -- im Anschluss gab es sogar einen Kaffee --",
      "topic": "Haareschneiden"
    },
    {
      "sentence": "Die Arbeiten von Team VK sind nicht nur schön, sondern sind auch effektiv und führen zum Erfolg.",
      "topic": "Arbeiten"
    },
    {
      "sentence": "Zielorientiert.",
      "topic": "Zielorientiert"
    },
    {
      "sentence": "So profitiert nicht nur die Agentur, sondern in erster Linie der Kunde.",
      "topic": "Kunde"
    },
    {
      "sentence": "Hier ist Marketing eine Investition die sich auch auszahlt!",
      "topic": "Marketing"
    },
    {
      "sentence": "War jetzt in fast allen Tabledance Clubs in München wobei ich sagen muss, dass der neu eröffnete Laden Blackboxxx für Männer der mit Abstand beste Laden ist.",
      "topic": "Laden"
    },
    {
      "sentence": "Die Preise sind ok und die Frauen mindestens genau so hübsch wie im boobs, wo die Preise leider sehr unverschämt sind...",
      "topic": "Preise"
    },
    {
      "sentence": "Die Stuttgarter Volksbank Homepage ist übersichtlich und vom Design erste Klasse.",
      "topic": "Homepage"
    },
    {
      "sentence": "Finden kann man wirklich alles was man sucht.",
      "topic": "Finden"
    },
    {
      "sentence": "Sollte man was über die Navigation nicht finden, so lässt sich ein bestimmtes Bankprodukt oder Information schnell über die Suchfunktion finden.",
      "topic": "Suchfunktion"
    },
    {
      "sentence": "Eine echt gelungene Seite.",
      "topic": "Seite"
    },
    {
      "sentence": "Ich war schon in vielen Cafés in aller Herren Länder, aber mit diesen herrlichen Torten und Kuchen muss sich das Café am Rosengarten vor keinem davon verstecken.",
      "topic": "Café"
    },
    {
      "sentence": "Von außen unscheinbar, schlicht und nicht in der besten Lage, aber die Kuchen und Torten sind dafür umso scheinbarer und leckerer.",
      "topic": "Kuchen"
    },
    {
      "sentence": "Das Sushi schmeckt immer hervorragend.",
      "topic": "Sushi"
    },
    {
      "sentence": "Unbedingt mal ausprobieren!!!!",
      "topic": "ausprobieren"
    },
    {
      "sentence": "Das Angebot ist reichlich und unerwartet vielseitig!",
      "topic": "Angebot"
    },
    {
      "sentence": "Die Bedienung war sehr aufmerksam und schnell.",
      "topic": "Bedienung"
    },
    {
      "sentence": "Dabei sitzt man drinnen wie draußen in angenehm freundlicher und ruhiger Umgebung.",
      "topic": "Umgebung"
    },
    {
      "sentence": "Ein lohnendes Sonntagsvergnügen!",
      "topic": "Sonntagsvergnügen"
    },
    {
      "sentence": "Neubau für viele Schulklassen vorhanden, also alles in Einwandfreiem Zustand.",
      "topic": "Neubau"
    },
    {
      "sentence": "Ein hervorragender Schulgarten in dem die Schüler einiges über die Natur lernen können.",
      "topic": "Schulgarten"
    },
    {
      "sentence": "Das Bild auf Google Maps ist veraltet!",
      "topic": "Bild"
    },
    {
      "sentence": "Diese Schule ist schon lange keine Bauststelle mehr!",
      "topic": "Schule"
    },
    {
      "sentence": "Positiv: Schöne Zimmer, alles sauber, freundliches Personal, gut eingerichtet.",
      "topic": "Zimmer"
    },
    {
      "sentence": "Im April 09 hat mir meine Frau zum Geburtstag ein Seminar im Hotel Sonnenstrahl geschenkt.",
      "topic": "Seminar"
    },
    {
      "sentence": "Die Unterbringung im Doppelzimmer hat sie mir gleich mit dazugeschenkt -- als Überraschung.",
      "topic": "Unterbringung"
    },
    {
      "sentence": "Leider ist das Seminarhotel eine Enttäuschung.",
      "topic": "Seminarhotel"
    },
    {
      "sentence": "Die Zimmer sind total heruntergekommen, ungepflegt, veraltete Einrichtung, harte Matratzen und verwöhnt.",
      "topic": "Zimmer"
    },
    {
      "sentence": "Das Hotel war wohl mal ein Sanatorium oder Krankenhaus und die Zimmer wurden nahezu unverändert übernommen.",
      "topic": "Hotel"
    },
    {
      "sentence": "Wie sich so eine Unterkunft als 3 Sterne Unterkunft bezeichnen darf ist mir ein Rätsel.",
      "topic": "Unterkunft"
    },
    {
      "sentence": "Wir haben uns übrigens 3 verschiedene Zimmer angesehen und alle waren eine Katastrophe.",
      "topic": "Zimmer"
    },
    {
      "sentence": "Wir haben uns mehrfach beim Personal beschwert -- das Bett wurde zwar mit einer weiteren Matratze ausgestattet aber das hat nix gebracht.",
      "topic": "Personal"
    },
    {
      "sentence": "Bei der Abreise kam dann noch die böse Überraschung in Form von extrem überhöhten Übernachtungspreisen.",
      "topic": "Übernachtungspreisen"
    },
    {
      "sentence": "Nach langem Suchen endlich den richtigen gefunden!!!",
      "topic": "Suchen"
    },
    {
      "sentence": "Ich bin seit fast 5 Jahren auf der Suche nach jemandem gewesen, der mich nicht übers Ohr hauen wollte.",
      "topic": "Suche"
    },
    {
    "sentence": "Und dann bin ich auf Empfehlung einer sehr guten Freundin nach Dortmund gefahren um mich dort von Herrn Knauff behandeln zu lassen und kann nur sagen, dass das die beste Entscheidung gewesen ist.",
      "topic": "Empfehlung"
    },
    {
      "sentence": "Vielen Vielen Dank für die super professionelle Arbeit.",
      "topic": "Arbeit"
    },
    {
      "sentence": "Ich bin seit 3 Sitzungen in Behandlung und ich fühle mich super gut aufgehoben.",
      "topic": "Behandlung"
    },
    {
      "sentence": "Eine super professionelle Beratung und Risikoaufklärung, die nicht darauf abzielt das meiste Geld zu machen, sondern effektiv zu arbeiten.",
      "topic": "Beratung"
    },
    {
      "sentence": "Das Team ist super nett, ich fühle mich sehr gut aufgehoben und der Wohlfühlfaktor ist zu 100 % gegeben.",
      "topic": "Team"
    },
    {
      "sentence": "Ich bin sehr zufrieden!",
      "topic": "Ich"
    },
    {
      "sentence": "Auf jeden Fall zu empfehlen!",
      "topic": "Empfehlen"
    },
    {
      "sentence": "Besonders die professionelle Beratung und die individuell angepassten Behandlungen entsprechen dem, was ich unter bester Dienstleistungsqualität verstehe.",
      "topic": "Beratung"
    },
    {
      "sentence": "Meine Erfahrung sagt: Sehr zu empfehlen.",
      "topic": "Erfahrung"
    },
    {
      "sentence": "Dortmunds erste Wahl für dauerhafte Haarentfernung und Wellness.",
      "topic": "Dortmunds"
    },
    {
      "sentence": "Der mechanische Trackpad - Klick meines Macbook Pro funktionierte eines Tages nicht mehr.",
      "topic": "Trackpad"
    },
    {
      "sentence": "Das Personal ist sehr nett und versuchen einem gleich zu helfen.",
      "topic": "Personal"
    },
    {
      "sentence": "Sehr beruhigend ein solches Geschäft in der Nähe zu haben...",
      "topic": "Geschäft"
    },
    {
      "sentence": "Was für eine Bruchbude..",
      "topic": "Bruchbude"
    },
    {
      "sentence": "Das Hotel sah aus als wäre es kurz davor abgerissen zu werden.",
      "topic": "Hotel"
    },
    {
      "sentence": "Leider habe ich die anderen beiden Bewertungen zu spät gesehen und gebucht, da ich dringend ein Hotel in der Gegend brauchte und der Preis ok war.",
      "topic": "Hotel"
    },
    {
      "sentence": "Nun weis ich warum.",
      "topic": "Ich"
    },
    {
      "sentence": "Kurze Wartezeiten und Arbeiten die selbst andere Zahnärzte bewundern.",
      "topic": "Arbeiten"
    },
    {
      "sentence": "Leider nur Privat Patienten.",
      "topic": "Patienten"
    },
    {
      "sentence": "Pizza hat die Qualität eines besseren Tiefkühlproduktes aus dem Supermarkt.",
      "topic": "Pizza"
    },
    {
      "sentence": "Der Salat ist mit einem mayonnaiselastigem Dressing verunstaltet.",
      "topic": "Salat"
    },
    {
      "sentence": "Die Pizzen schmecken nicht wirklich gut das meiste scheint aus der Dose zu kommen.",
      "topic": "Pizzen"
    },
    {
      "sentence": "Im italienischen Restaurant Pinnocchio kann man nicht nur wunderbar Pizza essen, auch alle anderen Gerichte schmecken hervorragend.",
      "topic": "Restaurant"
    },
    {
      "sentence": "Die Preise sind akzeptabel und für die Gegend absolut üblich.",
      "topic": "Preise"
    },
    {
      "sentence": "So ist das Restaurant auch familienfreundlich.",
      "topic": "Restaurant"
    },
    {
      "sentence": "Es bietet nette Atmosphäre und eine motivierte und zuvorkommende Bedienung.",
      "topic": "Atmosphäre"
    },
    {
      "sentence": "Patient trägt seit 3 Monaten Kontaktlinsen.",
      "topic": "Patient"
    },
    {
      "sentence": "Wünscht Untersuchung im Hinblick auf Gegenanzeigen und Hinderungsgründe für das Tragen von Kontaktlinsen.",
      "topic": "Untersuchung"
    },
    {
      "sentence": "Wünscht Untersuchung auf evtl. bereits aufgetretene Schädigung des Auges.",
      "topic": "Untersuchung"
    },
    {
      "sentence": "Für dieses Jahr plane ich noch ein paar kleine Anschaffungen, die ich mir auf jeden Fall wieder hier holen werde.",
      "topic": "Anschaffungen"
    },
    {
      "sentence": "Auch ich musste suchen (1. OG) und fand es dann.",
      "topic": "suchen"
    },
    {
      "sentence": "Was soll ich sagen... netter Empfang, Möbel nicht die neusten aber OK.",
      "topic": "Empfang"
    },
    {
      "sentence": "Auf Essen musste nicht lange gewartet werden und es war sehr sehr lecker.",
      "topic": "Essen"
    },
    {
      "sentence": "Preise waren für das Essen günstig.",
      "topic": "Preise"
    },
    {
      "sentence": "Ich kann es nur weiter empfehlen.",
      "topic": "es"
    },
    {
      "sentence": "Habe dann New China entdeckt.",
      "topic": "New China"
    },
    {
      "sentence": "Auf dem Weg dort hin natürlich gleich mal dran vorbeigefahren....",
      "topic": "Weg"
    },
    {
      "sentence": "Als ich endlich da war, viel mir das Schild 13 Jahre 'New China' auf.",
      "topic": "Schild"
    },
    {
      "sentence": "Die Innenausstattung sah auch ein wenig in die Jahre gekommen aus.",
      "topic": "Innenausstattung"
    },
    {
      "sentence": "Dann habe ich bei der Bedienung zwei mal das Buffet und etwas zu trinken bestellt, welches sofort an meinem Tisch war.",
      "topic": "Buffet"
    },
    {
      "sentence": "Das Buffet war reichhaltig, die Auslage nicht überfüllt, wurde sofort nachgefüllt wenn etwas leer wurde.",
      "topic": "Buffet"
    },
    {
      "sentence": "Die Bedienung war sehr aufmerksam und zuvorkommend.",
      "topic": "Bedienung"
    },
    {
      "sentence": "Als ich satt war hatte ich das gefühl nur noch herausrollen zu können, woran nicht zu letzt die Gebackenen Bananen mit Honig schuld waren.",
      "topic": "Gefühl"
    },
    {
      "sentence": "DIe Kanzlei Seehofer ist eine super Kanzlei!",
      "topic": "Kanzlei Seehofer"
    },
    {
      "sentence": "Sie hat mir zu meinem Recht geholfen, als ich probleme mit einer Bank hatte.",
      "topic": "Sie"
    },
    {
      "sentence": "Gutes Hotel mit noch akzeptabler Küche.",
      "topic": "Hotel"
    },
    {
      "sentence": "Preis - Leistungsverhältnis jedoch eher schlecht.",
      "topic": "Preis-Leistungsverhältnis"
    },
    {
      "sentence": "Es lohnt sich!",
      "topic": "Es"
    },
    {
      "sentence": "Bevorzugt ausgeschenkt und verkauft werden hier im Weinkost Weine aus Deutschland, Schweiz und Österreich.",
      "topic": "Weine"
    },
    {
      "sentence": "Demnächst soll es hier sogar jeweils passend zur Saison Käsefondue und oder Grünkohl geben.",
      "topic": "Käsefondue"
    },
    {
      "sentence": "Man darf gespannt sein.",
      "topic": "Man"
    },
    {
      "sentence": "Wir kommen wieder.",
      "topic": "Wir"
    },
    {
      "sentence": "Die Musik war ok, das Publikum jung.",
      "topic": "Musik"
    },
    {
      "sentence": "Ich hatte mit sehr viel mehr gerechnet.",
      "topic": "Ich"
    },
    {
      "sentence": "An sich ist die Location gar nicht so schlecht, vielleicht ein bisschen klein aber ansonsten ganz schick.",
      "topic": "Location"
    },
    {
      "sentence": "Wegen dem Fahrstuhl dauert der Einlaß nämlich ziemlich lange.",
      "topic": "Einlass"
    },
    {
      "sentence": "Anfangs war es ganz cool.",
      "topic": "Anfangs"
    },
    {
      "sentence": "Der Ausblick von der Terrasse ist irgendwie der einzige der wirklich schön ist.",
      "topic": "Ausblick"
    },
    {
      "sentence": "Dieses kleine aber feine Hotel bietet sehr schöne Zimmer, das Badezimmer war nahezu neu und somit in einem tadellosen Zustand.",
      "topic": "Hotel"
    },
    {
      "sentence": "Für mich 10 von 10 Punkten -- TOP",
      "topic": "Punkten"
    },
    {
      "sentence": "ich bin recht oft in Hotels unterwegs.",
      "topic": "Hotels"
    },
    {
      "sentence": "Aber so schlecht und dreckig bin ich noch nie untergekommen.",
      "topic": "untergekommen"
    },
    {
      "sentence": "Gebacken wird direkt im Haus.",
      "topic": "Gebacken"
    },
    {
      "sentence": "Hier sieht man wirklich was man für seine Wohnung haben muss.",
      "topic": "Wohnung"
    },
    {
      "sentence": "Das andere Möbelhaus mit Geschichte und Zukunft.",
      "topic": "Möbelhaus"
    },
    {
      "sentence": "Geführt von einer Familie mit Herz!",
      "topic": "Familie"
    },
    {
      "sentence": "Sehr gemütlich, mit viel Platz für jede Feier.",
      "topic": "Platz"
    },
    {
      "sentence": "Wir gehen regelmäßigLogo? Experienced There.term caters",
      "topic": "Wir"
    },
    {
      "sentence": "Efes war eigentlich immer unser Stamm - Döner - Lieferant.",
      "topic": "Efes"
    },
    {
      "sentence": "Aber seit einiger Zeit schmeckt der Döner nicht mehr so lecker.",
      "topic": "Döner"
    },
    {
      "sentence": "Ich weiche dann oft auf Pizza oder Dönertasche aus.",
      "topic": "Pizza"
    },
  
    {
      "sentence": "Ich wünsche dem neuen Team für die Saison 2010 einen vollen Erfolg.",
      "topic": "Team"
    },
    {
      "sentence": "Komme bald wieder!",
      "topic": "Komme"
    },
    {
      "sentence": "wir waren zu einer feierlichkeit mit insgesamt 4 paaren angereist und in allen belangen restlos zufrieden.",
      "topic": "wir"
    },
    {
      "sentence": "das essen ist sehr gut und auch das frühstück hatte alles was man für einen guten start in den tag braucht.",
      "topic": "essen"
    },
    {
      "sentence": "die umgebung lädt zum segeln ein.",
      "topic": "umgebung"
    },
    {
      "sentence": "Ein Nachmittag in Strassenhof fühlt sich an einem warmen Frühlingssonntag im April schon fast wie Urlaub an.",
      "topic": "Nachmittag"
    },
    {
      "sentence": "Super Essen und ein toller Biergarten!",
      "topic": "Essen"
    },
    {
      "sentence": "Ob im Sommer im Biergarten oder im Winter in der Stube, uns schmeckt's hier immer richtig gut!",
      "topic": "Biergarten"
    },
    {
      "sentence": "Deshalb kommen wir schon seit gut 20 Jahren immer wieder gerne zum Strassenhof!",
      "topic": "Strassenhof"
    },
    {
      "sentence": "Herr Reichel ist ein guter Arzt rund um die Suchtmedizin.",
      "topic": "Herr Reichel"
    },
    {
      "sentence": "Er besitzt nicht nur die Kompetenz der allg. Medizin, sondern ebenfalls der psychologischen Diagnostik.",
      "topic": "Er"
    },
    {
      "sentence": "Gekaufter Strauß war schon nach zwei Tagen in erbärmlicher 'Verfassung'.",
      "topic": "Strauß"
    },
    {
      "sentence": "Und dabei war er noch nicht mal richtig günstig.",
      "topic": "er"
    },
    {
      "sentence": "Ich war bei Frau Dr.Röder - Dischinger zur Behandlung (2 Monate Wartezeit) meiner Akne, die ich seit 13 Jahre habe.",
      "topic": "Behandlung"
    },
    {
      "sentence": "Leider hat mich diese Ärztin bitter enttäuscht.",
      "topic": "Ärztin"
    },
    {
      "sentence": "Trotz Termin musste ich 60 Minuten warten.",
      "topic": "Termin"
    },

    {
      "sentence": "Zeit nahm sie sich nur für ein kostenpflichtiges teures Hautkrebsscreening.",
      "topic": "Zeit"
    },

    
    {
      "sentence": "Ich halte diese Ärztin fachlich für höchst inkompentent.",
      "topic": "Ärztin"
    },
    {
      "sentence": "Sie zeigte sich in Bezug auf Roaccutan zudem als sehr schlecht informiert.",
      "topic": "Sie"
    },
    {
      "sentence": "Heutzutage sollte jedem Arzt bekannt sein, dass diese Therapie nicht mehr zwangsläufig zum Selbstmord führt und je nach Krankheitsgrad auch verschieden stark dosiert werden kann.",
      "topic": "Arzt"
    },
    {
      "sentence": "Lediglich die Sprechstundenhilfen sind sehr entgegenkommend und engagiert.",
      "topic": "Sprechstundenhilfen"
    },
    {
      "sentence": "Leider nützt einem das wenig.",
      "topic": "das"
    },
    {
      "sentence": "Das Essen ist lecker, aber die Preise sind viel zu hoch.",
      "topic": "Essen"
    },
    {
      "sentence": "Bei meinem ersten Termin wurde mir alles erklärt, ich habe einen persönlichen Trainingsplan bekommen und mir wurden die Geräte gezeigt.",
      "topic": "Termin"
    },
    {
      "sentence": "Sehr freundliche und geduldige Tanzlehrer.",
      "topic": "Tanzlehrer"
    },
    {
      "sentence": "Die Räumlichkeiten sind sehr schön und vor allem sehr sauber.",
      "topic": "Räumlichkeiten"
    },
    {
      "sentence": "Hier macht tanzen lernen richtig Spaß.",
      "topic": "tanzen"
    },
    {
      "sentence": "Ich kann Kay Jays nur jedem vollstens empfehlen.",
      "topic": "Kay Jays"
    },
    {
      "sentence": "Vielen Dank an das ganze Team.",
      "topic": "Team"
    },
    {
      "sentence": "Sehr nette Trainer, sehr sauber, gut zu erreichen und nicht zu teuer.",
      "topic": "Trainer"
    },
    {
      "sentence": "Danke an das ganze Team, habe viel gelernt und komme bestimmt wieder.",
      "topic": "Team"
    },
    {
      "sentence": "Kayjays Tanzmobil ist die erste Adresse in München wenn es um HipHop, Jazz Dance, Breakdance oder Bellydance tanzen lernen geht.",
      "topic": "Kayjays Tanzmobil"
    },
    {
      "sentence": "Freundliches und sehr vielseitiges Tanzlehrerteam.",
      "topic": "Tanzlehrerteam"
    },
    {
      "sentence": "Günstige Preise und viele unterschiedliche Tanzkurse",
      "topic": "Preise"
    },
    {
      "sentence": "Die Tanzschule ist mit öffentlichen Verkehrsmitteln gut zu erreichen und für Autofahrer stehen viele kostenlose Parkplätze zur Verfügung.",
      "topic": "Tanzschule"
    },
    {
      "sentence": "Auf der sehr übersichtlich strukturierten Webseite dieser Tanzschule macht das Surfen Spaß und man findet schnell alle wichtigen Informationen.",
      "topic": "Webseite"
    },
    {
      "sentence": "Essen war ok.",
      "topic": "Essen"
    },
    {
      "sentence": "Bedienung etwas gestresst, versuchte aber nett zu sein.",
      "topic": "Bedienung"
    },
    {
      "sentence": "Nichts für Familien.",
      "topic": "Nichts"
    },
    {
      "sentence": "Ich war wirklich enttäuscht.",
      "topic": "Ich"
    },
    {
      "sentence": "Das Studio sagt zwar, dass keine Termine vergeben werden, aber es werden Termine vorreserviert, wenn man so vorbeikommt und gerade alles besetzt ist.",
      "topic": "Studio"
    },
    {
      "sentence": "So haben Leute, die danach vorbeikommen, keine Chance, doch noch an eine Behandlung zu kommen.",
      "topic": "Leute"
    },

    {
      "sentence": "Warum dann nicht doch einen Terminkalender anbieten?",
      "topic": "Terminkalender"
    },
    {
      "sentence": "In meinem Land Brasilien funktioniert das besser!",
      "topic": "Brasilien"
    },
    {
      "sentence": "Da werden Termine vergeben, eingehalten und alle sind zufrieden.",
      "topic": "Termine"
    },
    {
      "sentence": "Wenn man bis 20h offen hat, sollten Kunden, die um 17 Uhr vorbeikommen, doch noch eine Chance haben...",
      "topic": "Kunden"
    },
    {
      "sentence": "Ich werde das Studio auf keinen Fall weiterempfehlen -- und in Bonn gibts die Konkurrenz, die ist genauso gut.",
      "topic": "Studio"
    },
    {
      "sentence": "Die Mitarbeiterin hat nicht so viele Informationen.",
      "topic": "Mitarbeiterin"
    },
    {
      "sentence": "Dann habe zwar reparieren gelassen aber ohne Leihgerät und monatelang warten.",
      "topic": "reparieren"
    },
    {
      "sentence": "Nachdem an meinem Fahrrad die Kette gerissen ist, habe ich es dahin gebracht und mir wurde versichert, dass es innerhalb von 5 Tagen repariert ist.",
      "topic": "Fahrrad"
    },
    {
      "sentence": "Die Herren wollten dann von mir Geld sehen, um das Fahrrad zu reparieren.",
      "topic": "Herren"
    },
    {
      "sentence": "Man muss dazu sagen, dass das Fahrrad 15 Jahre alt ist und ich bei der Abgabe gesagt habe, dass ich nur eine neue Kette haben möchte.",
      "topic": "Fahrrad"
    },
    {
      "sentence": "Ich habe meine Kette dann bei RADSPORT ALTIG reparieren lassen.",
      "topic": "Kette"
    },
    {
      "sentence": "Anstatt 30 Euro habe ich dann nur 18 bezahlt, und mein Fahrrad wurde in nur 10 Minuten repariert.",
      "topic": "Fahrrad"
    },
    {
      "sentence": "Ich kann nur jedem raten die Finger von diesem Laden zu lassen.",
      "topic": "Laden"
    },
    {
      "sentence": "Super Service!",
      "topic": "Service"
    },
    {
      "sentence": "Hatte einen Platten, haben mir den neuen schlauch innerhalb von 10 min kostenlos eingebaut und zudem noch kleinere \"schäden\" des Fahrrades Repariert!",
      "topic": "Schlauch"
    },
    {
      "sentence": "Ich hab vor 4 Wochen unsere Fahrräder zur Reparatur gebracht, es war einiges zu machen.",
      "topic": "Fahrräder"
    },
    {
      "sentence": "Die Leute sind echt nett und haben Ahnung und die Reparaturen wurden flott durchgeführt.",
      "topic": "Leute"
    },
    {
      "sentence": "Wir waren jetzt 2 Wochen lang auf Radtour und keine Probleme gehabt.",
      "topic": "Radtour"
    },
    {
      "sentence": "Noch nie habe ich so schlechte Service gehabt als bei Biotopia.",
      "topic": "Service"
    },
    {
      "sentence": "Das Personal ist frech und wollte uns überhaupt nicht helfen.",
      "topic": "Personal"
    },
    {
      "sentence": "ich war allein dieses Jahr 4 mal in der Werkstatt mit meinem Fahrrad.",
      "topic": "Werkstatt"
    },
    {
      "sentence": "Über den Service kann man zwar nicht meckern, aber ich habe das Gefühl, dass die Reparatur selbst nur mittelmäßig ist.",
      "topic": "Service"
    },
    {
      "sentence": "ich werde die Werkstatt jetzt wechseln.",
      "topic": "Werkstatt"
    },
    {
      "sentence": "Find ich super, dass endlich die Firma auf Google Maps eingetragen ist!",
      "topic": "Firma"
    },
    {
      "sentence": "Nette Beratung und sehr gute Preise, gutes Sortiment.",
      "topic": "Beratung"
    },
    {
      "sentence": "Hab bis jetzt immer was gefunden.",
      "topic": "was"
    },
    {
      "sentence": "Im Winter sind die Lammfellmützen zu empfehlen.",
      "topic": "Lammfellmützen"
    },
    {
      "sentence": "Top Qualität zum super Preis.",
      "topic": "Qualität"
    },
    {
      "sentence": "Dort alles bekommen was ich für meinen Verkauf gesucht habe, vielen Dank nochmals!",
      "topic": "Verkauf"
    },
    {
      "sentence": "Es ist ein Familienhotel mit sehr herzlicher Führung!",
      "topic": "Familienhotel"
    },
    {
      "sentence": "Die Zimmer sind sehr gemütlich und modern eingerichtet und man fühlt sich, als ob man Teil der Familie wäre!!!",
      "topic": "Zimmer"
    },
    {
      "sentence": "Die Hotelanlage ist sehr gepflegt und es wird viel Wert auf die noch so kleinen Details gelegt!",
      "topic": "Hotelanlage"
    },
    {
      "sentence": "Die Zimmer sind neu und liebevoll renoviert, mit großem Balkon, hellem Zimmer und wunderschönem Bad mit Whirlwanne!",
      "topic": "Zimmer"
    },
    {
      "sentence": "Wir werden auf Alle Fälle wieder nach Reischach ins Petrus fahren!",
      "topic": "Petrus"
    },
    {
      "sentence": "Dieses italienische Restaurant \"Piazza Italiana\" bekommt für den Service, die Speisen und das Ambiente volle 5 Sterne.",
      "topic": "Restaurant"
    },
    {
      "sentence": "Diese Lokalität ist wirklich zu Empfehlen.",
      "topic": "Lokalität"
    },
    {
      "sentence": "B & S ist ein Car - Audio - Spezialist wie man ihn nur hier findet!",
      "topic": "Spezialist"
    },
    {
      "sentence": "Ich habe hier meinen Alfa GT mit Lautsprechern, Endstufen und Subwoofern der deutschen Marke AMPIRE ausstatten lassen.",
      "topic": "Alfa GT"
    },
    {
      "sentence": "Ein richtig geiles Sound war das Ergebnis.",
      "topic": "Sound"
    },
    {
      "sentence": "Macht alles richtig viel Spaß!",
      "topic": "Spaß"
    },
    {
      "sentence": "Also es ist zwar schon 6 Jahre her, dass mein Mann und ich mit unserer damals 2jährigen Tochter dort übernachtet haben, aber wir können es nur allzugerne weiterempfehlen.",
      "topic": "übernachtet"
    },
    {
      "sentence": "Was will man mehr?",
      "topic": "man"
    },
    {
      "sentence": "Habe dort meine Bachelorarbeit binden lassen für die RFH Köln.",
      "topic": "Bachelorarbeit"
    },
    {
      "sentence": "Netter Service und gute Qualität.",
      "topic": "Service"
    },
    {
      "sentence": "Das Essen ist nicht schlecht, leider sind die Mitarbeiter in der Früh etwas unfreundlich.",
      "topic": "Essen"
    },
    {
      "sentence": "In der ComputerAkademie Rosenheim werden zertifizierte Trainings zu den Microsoft Office - Produkten angeboten.",
      "topic": "Trainings"
    },
    {
      "sentence": "Darüber hinaus gibt es Adobe - Trainings, Firmen-/Inhouse-Seminare sowie Coaching für 1-2 Personen.",
      "topic": "Trainings"
    },
    {
      "sentence": "Somit bin ich dann aufgestanden und gegangen.",
      "topic": "aufgestanden"
    },
    {
      "sentence": "Es gibt ja noch jede Menge andere Saloons in Nürnberg, wo man freundlich behandelt wird.",
      "topic": "Saloons"
    },
    {
      "sentence": "Sehr nette, dynamische und fachlich sehr gut ausgebildete Therapeutinnen.",
      "topic": "Therapeutinnen"
    },
    {
      "sentence": "Hier können wohl alle Krankheiten behandelt werden, man trifft Kinder und alte Menschen.",
      "topic": "Krankheiten"
    },
    {
      "sentence": "Durch die räumliche Nähe der einzelnen Praxen konnte ich am gleichen Vormittag zwei Termine wahrnehmen.",
      "topic": "Praxen"
    },
    {
      "sentence": "Zwei Praxen die sich in ihren Therapiemöglichkeiten sehr gut ergänzen.",
      "topic": "Praxen"
    },
    {
      "sentence": "Liebe Ergo - und Physiotherapeuten, macht weiter so!!",
      "topic": "Ergo- und Physiotherapeuten"
    },
    {
      "sentence": "Und wie es sich lohnt...!",
      "topic": "es"
    },
    {
      "sentence": "Obwohl die Firma Hummer sich selbst gerade im Umzug befand, wurden alle unsere Wünsche zu unserer vollsten Zufriedenheit umgesetzt.",
      "topic": "Firma Hummer"
    },
    {
      "sentence": "Wir haben uns Anfang Dez. entschlossen unser Wohn - und Esszimmer vollständig umgestalten zu lassen.",
      "topic": "Wir"
    },
    {
      "sentence": "Da meine Freundin und ich recht unterschiedliche Ideen hatten, haben wir uns dementsprechend beraten lassen.",
      "topic": "Freundin und ich"
    },
    {
      "sentence": "Wir haben den gesamten Fußboden erneuert und sämtliche Fenster mit neuen Vorhängen versehen.",
      "topic": "Wir"
    },
    {
      "sentence": "Das beste ist aber unsere 'neue' Couch.",
      "topic": "Couch"
    },
    {
      "sentence": "Unsere 'alte Garnitur' haben wir so liebgewonnen, daß wir uns entschlossen hatten sie komplett neu polstern lassen.",
      "topic": "Garnitur"
    },
    {
      "sentence": "Der Laden ist uns von Freunden empfohlen worden und wir werden diese Empfehlung bestimmt ebenfalls weitergeben.",
      "topic": "Laden"
    },
    {
      "sentence": "Das cafe ist einfach nur klasse.",
      "topic": "cafe"
    },
    {
      "sentence": "Ich bin total begeistert seitdem ich das letzte Jahr das erste Mal hier war.",
      "topic": "Ich"
    },
    {
      "sentence": "Die Bedienung ist total nett und klasse und das Essen ist der Hammer.",
      "topic": "Bedienung"
    },
    {
      "sentence": "Das Dolce ist ein kleines, gemütliches Cafe mit sehr schönem Ambiente.",
      "topic": "Dolce"
    },
    {
      "sentence": "Der Service ist super, die Mitarbeiter kompetent.",
      "topic": "Service"
    },
    {
      "sentence": "Alle waren hellauf begeistert von den kreativen und wunderschönen Ideen.",
"topic": "Alle"
    },
    {
      "sentence": "Sehr gute Fahrschule.",
      "topic": "Fahrschule"
    },
    {
      "sentence": "Nett, kompetent und dazu noch im Herzen Müggelheims.",
      "topic": "Müggelheims"
    },
    {
      "sentence": "Sehr zu empfehlen.",
      "topic": "empfehlen"
    },
    {
      "sentence": "Noch eine von den gemütlichen Tavernen in Oostende sehr zu empfehlen.",
      "topic": "Tavernen"
    },
    {
      "sentence": "Der Metzger des Vertrauens, nur hier wird mit Liebe geschlachtet!",
      "topic": "Metzger"
    },
    {
      "sentence": "Nie wieder, nicht zu empfehlen!",
      "topic": "empfehlen"
    },
    {
      "sentence": "Haben online bestellt, wie verlangt, und kein Essen erhalten.",
      "topic": "Essen"
    },
    {
      "sentence": "Danke für die knurrenden Mägen, bestellen nun woanders.",
      "topic": "Mägen"
    },
    {
      "sentence": "Wir beauftragen das die Firma Ideengut Berroth schon seit vielen Jahren.",
      "topic": "Firma Ideengut Berroth"
    },
    {
      "sentence": "Wir sind mit der Arbeit und dem Service sehr zufrieden.",
      "topic": "Wir"
    },
    {
      "sentence": "Es werden immer wieder Konzepte vorgeschlagen, auf die wäre man selbst gar nicht gekommen.",
      "topic": "Konzepte"
    },
    {
      "sentence": "Ich war heute bei Frau Stoehr weil ich immer noch 'Wasser in den Ohren' hatte.",
      "topic": "Frau Stoehr"
    },
    {
      "sentence": "Sie war super freundlich und hat mich zwischen die Termine geschoben.",
      "topic": "Sie"
    },
    {
      "sentence": "Sie hörte aufmerksam zu, war sehr freundlich und zuvorkommend.",
      "topic": "Sie"
    },
    {
      "sentence": "Man fühlte sich sehr gut bei ihr aufgehoben.",
      "topic": "Man"
    },
    {
      "sentence": "Das Ende vom Lied ist, dass ich eine Gehörgangentzündung auf beiden Ohren habe.",
      "topic": "Ende"
    },
    {
      "sentence": "Bereits letzte Woche war ich bei einer anderen HNO - Ärztin, wegen meiner Beschwerden.",
      "topic": "HNO-Ärztin"
    },
    {
      "sentence": "Bei Frau Stoehr bin ich nun gut aufgehoben und dankbar, dass meinem Problem nun geholfen wird.",
      "topic": "Frau Stoehr"
    },
    {
      "sentence": "Ich kann Frau Stoehr nur weiter empfehlen.",
      "topic": "Frau Stoehr"
    },
    {
      "sentence": "Durch die räumliche Nähe der einzelnen Praxen konnte ich am gleichen Vormittag zwei Termine wahrnehmen.",
      "topic": "Praxen"
    },
    {
      "sentence": "Zwei Praxen die sich in ihren Therapiemöglichkeiten sehr gut ergänzen.",
      "topic": "Praxen"
    },
    {
      "sentence": "Liebe Ergo - und Physiotherapeuten, macht weiter so!!",
      "topic": "Ergo- und Physiotherapeuten"
    },
    {
        "sentence": "Und wie es sich lohnt...!",
        "topic": "es"
    },
    {
        "sentence": "Obwohl die Firma Hummer sich selbst gerade im Umzug befand, wurden alle unsere Wünsche zu unserer vollsten Zufriedenheit umgesetzt.",
        "topic": "Firma Hummer"
    },
    {
        "sentence": "Wir haben uns Anfang Dez. entschlossen unser Wohn - und Esszimmer vollständig umgestalten zu lassen.",
        "topic": "Wir"
    },
    {
        "sentence": "Da meine Freundin und ich recht unterschiedliche Ideen hatten, haben wir uns dementsprechend beraten lassen.",
        "topic": "Freundin und ich"
    },
    {
        "sentence": "Wir haben den gesamten Fußboden erneuert und sämtliche Fenster mit neuen Vorhängen versehen.",
        "topic": "Wir"
    },
    {
        "sentence": "Das beste ist aber unsere 'neue' Couch.",
        "topic": "Couch"
    },
    {
        "sentence": "Unsere 'alte Garnitur' haben wir so liebgewonnen, daß wir uns entschlossen hatten sie komplett neu polstern lassen.",
        "topic": "Garnitur"
    },
    {
        "sentence": "Der Laden ist uns von Freunden empfohlen worden und wir werden diese Empfehlung bestimmt ebenfalls weitergeben.",
        "topic": "Laden"
    },
    {
        "sentence": "Das cafe ist einfach nur klasse.",
        "topic": "cafe"
    },
    {
        "sentence": "Ich bin total begeistert seitdem ich das letzte Jahr das erste Mal hier war.",
        "topic": "Ich"
    },
    {
      "sentence": "Auch das Praxiskonzept mit vielen Ärzten unterschiedlicher Fachrichtungen und Spezialisierungen verhilft zu schneller Hilfe, wenn man sie braucht.",
      "topic": "Praxiskonzept"
    },
    {
      "sentence": "Sehr teuer und erst im dritten Anlauf haben wir unsere Vorhänge wiederbekommen.",
      "topic": "Vorhänge"
    },
    {
      "sentence": "Bei einer telefonischen Beschwerde wurde einfach aufgelegt.",
      "topic": "Beschwerde"
    },
    {
      "sentence": "Wir haben dort einen sehr schönen Abend verbracht!",
      "topic": "Abend"
    },
    {
      "sentence": "Das Essen war wirklich super und \"ECHT\".",
      "topic": "Essen"
    },
    {
      "sentence": "Nicht wie das typische asiatische Essen, was man für Europäer zubereitet. :-)",
      "topic": "Essen"
    },
    {
      "sentence": "Außerdem ist die Atmosphäre wirklich schön und der Service sehr zuvorkommend.",
      "topic": "Atmosphäre"
    },
    {
      "sentence": "Wir bekamen ein Begrüßungs - und ein Abschiedsschnaps und ausreichend Reis als Nachschub.",
      "topic": "Begrüßungsschnaps"
    },
    {
      "sentence": "Es lohnt sich wirklich dort Essen zu gehen!",
      "topic": "Essen"
    },
    {
      "sentence": "Wir hatten unter den Chinarestaurants das Dynasty über die gmaps Bewertungen ausgewählt.",
      "topic": "Dynasty"
    },
    {
      "sentence": "Unsere Erwartungen wurde nicht enttäuscht!!",
      "topic": "Erwartungen"
    },
    {
      "sentence": "Wir waren sechs Personen und haben alle das Buffet gewählt.",
      "topic": "Buffet"
    },
    {
      "sentence": "Dort findet man auf der einen Seite eine große Auswahl an verschiedenen chinesischen Spezialitäten.",
      "topic": "Auswahl"
    },
    {
      "sentence": "Auf der anderen Seite rohes Fleisch und Fisch, was man sich sofort mit einer noch vorher auszuwählenden Sauce braten lassen kann.",
      "topic": "Fleisch"
    },
    {
      "sentence": "Eine hervorragende Idee.",
      "topic": "Idee"
    },
    {
      "sentence": "Es gibt sogar Jakobsmuscheln!!!!",
      "topic": "Jakobsmuscheln"
    },
    {
      "sentence": "Auch das Sushi ist einwandfrei!",
      "topic": "Sushi"
    },
    {
      "sentence": "Und zum Nachtisch kann man verschiedene Früchte oder Eis wählen.",
      "topic": "Nachtisch"
    },
    {
      "sentence": "Überrascht hat uns ein wenig die Caprese (Tomaten und Mozzarella).",
      "topic": "Caprese"
    },
    {
      "sentence": "Dies ist doch eine italienische Spezialität und hat nichts in einem Chinarestaurant verloren.",
      "topic": "Spezialität"
    },
    {
      "sentence": "Ebenso zuvorkommend war der Service!",
      "topic": "Service"
    },
    {
      "sentence": "Das Personal ist sehr nett!",
      "topic": "Personal"
    },
    {
      "sentence": "Zum Schluss gibt es sogar noch typische chinesische Kitschgeschenke.",
      "topic": "Kitschgeschenke"
    },
    {
      "sentence": "Ein rundherum schöner Abend.",
      "topic": "Abend"
    },
    {
      "sentence": "Das Dynasty in Landshut ist wirklich empfehlenswert!",
      "topic": "Dynasty"
    },
    {
      "sentence": "Dieses Unternehmen bekommt keinen anständigen Privatanschluss hin, was soll das erst mit Geschäftskundenanschlüssen werden.",
      "topic": "Privatanschluss"
    },
    {
      "sentence": "Ich kann von diesem Unternehmen nur abraten.",
      "topic": "Unternehmen"
    },
    {
      "sentence": "Was gar nicht geht sind Kundensupport und Beschwerdemanagement.",
      "topic": "Kundensupport"
    },
    {
      "sentence": "Alles was das Fitnessherz begehrt",
      "topic": "Fitnessherz"
    },
    {
      "sentence": "Vom Klettern über Sauna bis zu den neusten Geräten alles da was man braucht!",
      "topic": "Geräte"
    },
    {
      "sentence": "als die billige Fertigsauce auf den Tisch kam, dachte ich erst, das wird nix.",
      "topic": "Fertigsauce"
    },
    {
      "sentence": "aber dann kam ein toller Salat, leckeres Lamm mit guten Beilagen und nettem Service.",
      "topic": "Salat"
    },
    {
      "sentence": "Ich war schon bei vielen Steak Restaurants, vor gut 2 Tagen habe ich dieses Steakhaus gefunden.",
      "topic": "Steakhaus"
    },
    {
      "sentence": "Wer in gepflegter Atmosphäre ein \"echtes\" Steak essen möchte ist hier genau richtig!",
      "topic": "Steak"
    },
    {
      "sentence": "super freundliches Personal.",
      "topic": "Personal"
    },
    {
      "sentence": "das erlebt man selten.",
      "topic": "das"
    },
    {
      "sentence": "Produkte wie gewohnt immer ordentlich.",
      "topic": "Produkte"
    },
    {
      "sentence": "mein Lieblingsrestaurant an der Autobahn.",
      "topic": "Lieblingsrestaurant"
    },
    {
      "sentence": "Wer richtig professionelles Webdesign und Websoftware sucht, ist hier genau richtig!",
      "topic": "Webdesign"
    },
    {
      "sentence": "Hr. Bruckner ist sehr bemüht die Kunden zufriedenzustellen.",
      "topic": "Bruckner"
    },
    {
      "sentence": "Fachkundige, kompetente und sehr freundliche Beratung.",
      "topic": "Beratung"
    },
    {
      "sentence": "Ausgezeichnetes Angebot.",
      "topic": "Angebot"
    },
    {
      "sentence": "Eine Werkstatt in der einem nichts aufgeschwätzt wird, sondern nur das repariert wird, was kaputt ist.",
      "topic": "Werkstatt"
    },
    {
      "sentence": "Außerdem werden vereinbarte Termine auch eingehalten!",
      "topic": "Termine"
    },
    {
      "sentence": "Die Preise sind teilweise etwas heftig, aber sonst alles toll.",
      "topic": "Preise"
    },
    {
      "sentence": "Das Personal ist überaus nett und hilfsbereit.",
      "topic": "Personal"
    },
    {
      "sentence": "Es werden oft Zutaten oder Beilagen vergessen.",
      "topic": "Zutaten"
    },
    {
      "sentence": "Beschwerdebriefe werden ignoriert.",
      "topic": "Beschwerdebriefe"
    },
    {
      "sentence": "Im Gegensatz zu anderen Filialen deutlich schlechter.",
      "topic": "Filialen"
    },
    {
      "sentence": "Fragen rund ums Radfahren kompetent beantwortet.",
      "topic": "Fragen"
    },
    {
      "sentence": "Habe mir 2004 hier mein erstes Rennrad gekauft.",
      "topic": "Rennrad"
    },
    {
      "sentence": "Meinen 'Flitzer' für 2011 habe ich ebenfalls bei Radsport Wulff gekauft.",
      "topic": "Flitzer"
    },
    {
      "sentence": "Habe mir auch gleich noch ein Trikot und eine Hose von Wulff zugelegt.",
      "topic": "Trikot"
    },
    {
      "sentence": "Habe heute online bestellt, ich war erstaunt wie schnell das Essen da war.",
      "topic": "Essen"
    },
    {
      "sentence": "Wir haben schon viele Hausgeräte bei MAXX gekauft und können die Firma nur empfehlen.",
      "topic": "Hausgeräte"
    },
    {
      "sentence": "Auch Freunde und Arbeitskollegen sind immer sehr zufrieden.",
      "topic": "Freunde"
    },
    {
      "sentence": "Achtung: Stadion - Restaurant, aber dafür sehr gut!",
      "topic": "Restaurant"
    },
    {
      "sentence": "Absolut unfreundliche Behandlung.",
      "topic": "Behandlung"
    },
    {
      "sentence": "In Zukunft tanke ich statt Ethanol, Super an anderen Tankstellen - und zwar gerne!!!",
      "topic": "Ethanol"
    },
    {
      "sentence": "Unser Unternehmen betreibt mehrere kommerzielle Websites, die online im internationalen Wettbewerb stehen.",
      "topic": "Websites"
    },
    {
      "sentence": "In Google kämpfen Millionen von Konkurrenzseiten um unsere wichtigsten Keywords.",
      "topic": "Keywords"
    },
    {
      "sentence": "Sehr, sehr guter Supermarkt.",
      "topic": "Supermarkt"
    },
    {
      "sentence": "Für einen Allrounder geht es eigentlich nicht besser.",
      "topic": "Allrounder"
    },
    {
      "sentence": "Ich habe die Stadtwerke als kompetenten und zuverlässigen Geschäftspartner kennengelernt und kann mich der ersten Beurteilung in keiner Hinsicht anschließen.",
      "topic": "Stadtwerke"
    },
    {
      "sentence": "Den Kommentar von unten kann ich nur unterstützen!",
      "topic": "Kommentar"
    },
    {
      "sentence": "Habe schon viele Pizzen in der Umgebung ausprobiert.",
      "topic": "Pizzen"
    },
    {
      "sentence": "Leider kein Lieferservice!",
      "topic": "Lieferservice"
    },
    {
      "sentence": "Am besten gefällt mir die sehr nette, auch persönliche Betreuung.",
      "topic": "Betreuung"
    },
    {
      "sentence": "Der Abend beim Landgasthof Hagenhoff hatte leider einen bitteren Beigeschmack.",
      "topic": "Abend"
    },
    {
      "sentence": "Ich hatte ein paar Geschäftsfreunde zum Essen eingeladen.",
      "topic": "Geschäftsfreunde"
    },
    {
      "sentence": "Sehr kompetente Zahnärztin.",
      "topic": "Zahnärztin"
    },
    {
      "sentence": "Das Team ist zudem auch sehr zuvorkommend und sympathisch.",
      "topic": "Team"
    },
    {
      "sentence": "Einen Termin bekommt man schnell und man hat kaum Wartezeiten.",
      "topic": "Termin"
    },
    {
      "sentence": "Ich war Anfang des Jahres auf Ihrem Reiterhof.",
      "topic": "Reiterhof"
    },
    {
      "sentence": "Schöne Gegend, nette Menschen und gepflegte Pferde.",
      "topic": "Gegend"
    },
    {
      "sentence": "Ich freue mich auf ein Wiedersehen.",
      "topic": "Wiedersehen"
    },
    {
      "sentence": "Habe hier letzte Woche Passfotos machen lassen.",
      "topic": "Passfotos"
    },
    {
      "sentence": "Ich kann dieses Studio nur weiterempfehlen -- super Bilder ohne Gruseleffekt!!!",
      "topic": "Studio"
    },
    {
      "sentence": "Preis für 4 Bilder: 14,95 und nette Beratung!",
      "topic": "Preis"
    },
    {
      "sentence": "Meine Bewerbungsfotos sind einfach total super geworden.",
      "topic": "Bewerbungsfotos"
    },
    {
      "sentence": "Der Service und die Qualität der Bilder hat einfach gestimmt.",
      "topic": "Service"
    },
    {
      "sentence": "Trotzdem ein sehr teures Vergnügen.",
      "topic": "Vergnügen"
    },
    {
      "sentence": "Die Fotos gehen von der Qualität in Ordnung.",
      "topic": "Fotos"
    },
    {
      "sentence": "Die Kneipe ist gemütlich und richtig knuffig.",
      "topic": "Kneipe"
    },
    {
      "sentence": "Das Dart - Spielen ist gesellig, das Bier schmeckt, man kommt mit den Gästen schnell ins Gespräch.",
      "topic": "Dart-Spielen"
    },
    {
      "sentence": "Ich kenne eigentlich kein besseres Restaurant als dieses.",
      "topic": "Restaurant"
    },
    {
      "sentence": "Vom Wirt über Speisen und Preise.",
      "topic": "Wirt"
    },
    {
      "sentence": "Er ist ein super Taxifahrer und immer Pünktlich und nett",
      "topic": "Taxifahrer"
    },
    {
      "sentence": "Die Anreise mit dem Auto war ganz okay.",
      "topic": "Anreise"
    },
    {
      "sentence": "Check in war sehr schnell.",
      "topic": "Check-in"
    },
    {
      "sentence": "Der Park ist recht sauber.",
      "topic": "Park"
    },
    {
      "sentence": "Das Frühstück ist lecker.",
      "topic": "Frühstück"
    },
    {
      "sentence": "Aqua Mundo ist einfach PERFEKT.",
      "topic": "Aqua Mundo"
    },
    {
      "sentence": "Der Park ist Kinder und Behinderten gerecht.",
      "topic": "Park"
    },
    {
      "sentence": "Wir können den Seeteufel nur empfehlen.",
      "topic": "Seeteufel"
    },
    {
      "sentence": "Sind zum Kurzurlaub in Duhnen gewesen und fanden aus Zufall ganz am Ende der Strasse im Hafen dieses tolle Restaurant.",
      "topic": "Restaurant"
    },
    {
      "sentence": "Die Qualität war spitze!",
      "topic": "Qualität"
    },
    {
      "sentence": "Haben uns dann Fisch zum Mitnehmen bestellt aus der Räucherei.",
      "topic": "Fisch"
    },
    {
      "sentence": "Wir freuen uns auf ein Wiedersehen jetzt im Dezember.",
      "topic": "Wiedersehen"
    },
    {
      "sentence": "Sehr kompetenter und freundlicher Meisterbetrieb.",
      "topic": "Meisterbetrieb"
    },
    {
      "sentence": "Wir waren vier Personen zum Abendessen.",
      "topic": "Abendessen"
    },
    {
      "sentence": "Keiner von uns kannte dieses kleine Lokal.",
      "topic": "Lokal"
    },
    {
      "sentence": "Der Hammer sind jedoch die süßen Sachen am Schluss.",
      "topic": "Sachen"
    },
    {
      "sentence": "Der Schokokuchen ist ja so was von super fein, beinahe hätte ich einen zweiten bestellt.",
      "topic": "Schokokuchen"
    },
    {
      "sentence": "Service sehr freundlich und korrekt.",
      "topic": "Service"
    },
    {
      "sentence": "Preise fair.",
      "topic": "Preise"
    },
    {
      "sentence": "Es war einfach ein toller Abend!",
      "topic": "Abend"
    },
    {
      "sentence": "Hab genug von der Praxis.",
      "topic": "Praxis"
    },
    {
      "sentence": "Ein richtiges Landgasthaus in dem man sich wohl fuhlt.",
      "topic": "Landgasthaus"
    },
    {
      "sentence": "Die Behandlung in dieser Praxis ist hervorragend!",
      "topic": "Behandlung"
    },
    {
      "sentence": "Schwestern und Ärzte überzeugen durch Kompetenz, Freundlichkeit und Aufmerksamkeit.",
      "topic": "Schwestern"
    },
    {
      "sentence": "Die Praxis ist trotz starker Auslastung sehr zu empfehlen!",
      "topic": "Praxis"
    },
    {
      "sentence": "Als Patient, auch wenn man noch nicht fortgeschrittenen Alters ist, wie ich fuhlt man sich sehr gut aufgehoben.",
      "topic": "Patient"
    },
    {
      "sentence": "Vielen Dank daher an das gesamte Team!!!!",
      "topic": "Team"
    },
    {
      "sentence": "Für Freunde des italienischen Abends.",
      "topic": "Abends"
    },
    {
      "sentence": "Bitte mit Taxi kommen, wenn ihr den Original Italienischen Wein genießen wollt!",
      "topic": "Wein"
    },
    {
      "sentence": "Ich hatte einen sehr schönen Abend!",
      "topic": "Abend"
    },
    {
      "sentence": "Super Saunalandschaft...",
      "topic": "Saunalandschaft"
    },
    {
      "sentence": "Wird immer alles ordentlich gehalten und gepflegt, was ja heut zu Tage nicht üblich ist!",
      "topic": "gepflegt"
    },

    {
      "sentence": "Die Aussicht ist einmalig, die Einrichtung schön.",
      "topic": "Aussicht"
    },
    {
      "sentence": "Essen werde ich da nichts mehr.",
      "topic": "Essen"
    },
    {
      "sentence": "Ich habe nur gute Erfahrungen mit der Werkstatt bei Reparaturen und Inspektionen gemacht.",
      "topic": "Werkstatt"
    },

    {
      "sentence": "Es sind nette Leute, fachlich kompetent, zuverlässig und flexibel.",
      "topic": "Leute"
    },
    {
      "sentence": "Gute Weinauswahl, nette und kompetente Beratung.",
      "topic": "Weinauswahl"
    },
    {
      "sentence": "Besonders zu empfehlen sind die Weinproben, die alle paar Monate stattfinden.",
      "topic": "Weinproben"
    },

    {
      "sentence": "Ich bin mit dem Kindergarten sehr zufrieden.",
      "topic": "Kindergarten"
    },
    {
      "sentence": "Die Außeneinrichtung könnten sie vielleicht noch etwas verbessern.",
      "topic": "Außeneinrichtung"
    },
    {
      "sentence": "Die Erzieher sind alle sehr freundlich und die Kinder anhänglich.",
      "topic": "Erzieher"
    },
    {
      "sentence": "Beim Mittagsschlaf kann es manchmal zu Schimpereien kommen, weil eigige nicht schlafen wollen.",
      "topic": "Mittagsschlaf"
    },
    {
      "sentence": "Die Angebote des Essens sind auch gut und man wir immer über den Speiseplan der Woche informiert.",
      "topic": "Angebote"
    },
    {
      "sentence": "Der Speiseplan ist ausgehängt und fen Paln für den jeweiligen Tag kann man sich inene an einem großen Schild ansehen.",
      "topic": "Speiseplan"
    },
    {
      "sentence": "Für die Kinder sind dort extra Bilder aufgehängt worden.",
      "topic": "Bilder"
    },
    {
      "sentence": "Sie bekommen Frühstüch, Mittag und einen Snack.",
      "topic": "Frühstück"
    },
    {
      "sentence": "Die Kleinen lernen schon frühzeitg Englisch, zum Beispiel hängt am jeweiligen Wochentag der Tag in Englisch da.",
      "topic": "Englisch"
    },
    {
      "sentence": "Ich war dort erst kürzlich als Praktikantin dort und muss sagen, es hat mir echt gut gefallen.",
      "topic": "Praktikantin"
    },
    {
      "sentence": "Sehr kompetente und nette Kosmetikerin.",
      "topic": "Kosmetikerin"
    },
    
    {
      "sentence": "Meine Wärmepumpenheizung habe ich vor zwei Jahren von der Firma Wachinger installieren lassen.",
      "topic": "Wärmepumpenheizung"
    },
    {
      "sentence": "Die Montage war tiptop und termingerecht.",
      "topic": "Montage"
    },
    {
      "sentence": "Die Anlage läuft seitdem sehr zuverlässig.",
      "topic": "Anlage"
    },
    {
      "sentence": "Bei einer Störung vergangenen Winter konnte mir der Wochenend - Notdienst telefonisch weiterhelfen.",
      "topic": "Störung"
    },
  
    
    {
      "sentence": "Hatte verschiedene Zimmer im EG und im OG.",
      "topic": "Zimmer"
    },
    {
      "sentence": "Die Zimmer waren sauber und gut eingerichtet.",
      "topic": "Zimmer"
    },
    {
      "sentence": "Zusätzlich hatte ich eine Terasse bzw. Balkon.",
      "topic": "Terasse"
    },
    {
      "sentence": "Der Fernseher hatte leider in beiden Zimmern ein schlechtes Bild.",
      "topic": "Fernseher"
    },
    {
      "sentence": "Das Restaurant bietet gute bis sehr gute Qualität zu annehmbar.",
      "topic": "Restaurant"    },
    {
      "sentence": "Beim Frühstück war ich dann eher enttäuscht.",
      "topic": "Frühstück"
    },
    {
      "sentence": "Tische nicht abgeräumt, ewig keinen Kaffe bekommen und die Auswahl eher Durchschnitt.",
      "topic": "Tische"
    },
    {
      "sentence": "Liegt wahrscheinlich an einer Servicekraft, die das alles garnicht schaffen kann -- schade.",
      "topic": "Servicekraft"
    },
    {
      "sentence": "Gutes Essen, nette Bedienung und das beste Bier der Stadt!",
      "topic": "Essen"
    },
    {
      "sentence": "Das Hotel bietet für den Preis keine besonders gute Leistung.",
      "topic": "Hotel"
    },
    {
      "sentence": "Zum Frühstück Saft aus Plastikbecher habe ich in den 16 Tagen in Italien nicht erlebt.",
      "topic": "Saft"
    },
    {
      "sentence": "Keine Eier.",
      "topic": "Eier"
    },
    {
      "sentence": "Personal nicht gerade freundlich.",
      "topic": "Personal"
    },
    {
      "sentence": "Lage ist jedoch gut.",
      "topic": "Lage"
    },
    {
      "sentence": "Nahe am Stadtzentrum und eine schönen Ausblick.",
      "topic": "Stadtzentrum"
    },
    {
      "sentence": "Die Bettdecke schaut man sich lieber nicht von unten an.",
      "topic": "Bettdecke"
    },

    {
      "sentence": "Nette Beratung, Umfangreiches Sortiment und viele Artikel die Ich vorher nicht kannte!",
      "topic": "Sortiment"
    },
    {
      "sentence": "Ich habe mich für Partynasenbecher und Gebisseiswürfelformen entschieden!",
      "topic": "Partynasenbecher"
    },
    {
      "sentence": "Damit lag ich auch genau richtig!",
      "topic": "Damit"
    },
    {
      "sentence": "Sehr schickes Geschäft mit einzigartigen Geschenken!",
      "topic": "Geschäft"
    },
    {
      "sentence": "Ein absolutes Highlight für jung und alt.",
      "topic": "Highlight"
    },
    {
      "sentence": "Sehr gute Beratung aber nicht aufdringlich.",
      "topic": "Beratung"
    },
    {
      "sentence": "In Frankfurt sollte mehr solcher Neueröffnungen geben!",
      "topic": "Neueröffnungen"
    },
    {
      "sentence": "Ich bin eigentlich nur durch Zufall dran vorbeigekommen und war total überrascht.",
      "topic": "Zufall"
    },
    {
      "sentence": "Echt tolle Geschenkideen, jede Menge ausgefallene Artikel und wirklich nette Bedienung.",
      "topic": "Geschenkideen"
    },
    {
      "sentence": "Und meine meine Weihnachtsgeschenke kaufe ich auch da!",
      "topic": "Weihnachtsgeschenke"
    },
    {
      "sentence": "StyleOn.de kannte ich schon aus dem Internet, aber so ein Laden ist halt doch noch mal besser.",
      "topic": "Laden"
    },
    {
      "sentence": "Das Sortiment ist wohl einmalig in Frankfurt.",
      "topic": "Sortiment"
    },
    {
      "sentence": "Jetzt ist man beim Geschenke finden nicht mehr überfragt.",
      "topic": "Geschenke"
    },
    {
      "sentence": "Beim Styleon.de concept store findet man wirklich die ausgefallensten Sachen.",
      "topic": "store"
    },
    {
      "sentence": "Qualität und Preise stimmen auch!",
      "topic": "Qualität"
    },
    {
      "sentence": "Fazit: Reinschauen lohnt sich!",
      "topic": "Fazit"
    },
    {
      "sentence": "Direkt neben dem großen neuen REWE in Bornheim hat vor Kurzem der Shop von Styleon aufgemacht.",
      "topic": "Shop"
    },
    {
      "sentence": "Dort findet man sehr ausgefallene, kreative und vor allem lustige Geschenkideen.",
      "topic": "Geschenkideen"
    },
    {
      "sentence": "Aber auch nette Dinge für die Wohnung: Deko, Accessoires etc.",
      "topic": "Dinge"
    },
    {
      "sentence": "Das Stöbern macht wirklich Spaß und irgendwas findet man immer.",
      "topic": "Stöbern"
    },
    {
      "sentence": "Ideal vor Weihnachten oder dem nächsten Geburtstag.",
      "topic": "Weihnachten"
    },
    {
      "sentence": "Das Ambiente stimmt, die Verkäufer sind nett.",
      "topic": "Ambiente"
    },
    {
      "sentence": "Von mir gibt es deshalb 5 Sterne!",
      "topic": "Sterne"
    },
    {
      "sentence": "Wir kommen gerne wieder.",
      "topic": "Wir"
    },
    {
      "sentence": "Super Service, sehr freundliches Personal.",
      "topic": "Service"
    },
    {
      "sentence": "Da leiht man doch gleich noch mehr Filme aus als nur einen.",
      "topic": "Filme"
    },
    {
      "sentence": "Wie mein Vorposter bereits erwähnt hat, wird hier sehr groß auf den Kundenservice geachtet.",
      "topic": "Kundenservice"
    },
    {
      "sentence": "Kennen sie noch das alte Andria in Springe?",
      "topic": "Andria"
    },
    {
      "sentence": "Was sich geändert hat?",
      "topic": "Was"
    },
    {
      "sentence": "Ist aber mein Gefühl, macht euch selbst ein Bild!",
      "topic": "Gefühl"
    },
    {
      "sentence": "Eine vernünftige Beratung gab es leider auch nicht.",
      "topic": "Beratung"
    },
    {
      "sentence": "Kann ich absolut nicht empfehlen.",
      "topic": "Kann"
    },
    {
      "sentence": "Alle konnten vor Ort sich den Entwurf anschauen.",
      "topic": "Entwurf"
    },
    {
      "sentence": "Es ist eine Super - Website.",
      "topic": "Website"
    },
    {
      "sentence": "Nie wieder ins \"Hotel am Rathaus\"!",
      "topic": "Hotel"
    },
    {
      "sentence": "Unser Gepäck bekamen wir erst gegen Zahlung von 50,00 € wieder.",
      "topic": "Gepäck"
    },
    {
      "sentence": "Das war eine Frechheit!",
      "topic": "Frechheit"
    },
    {
      "sentence": "Eine schön gestaltete Strandbar wo man sich gut entspannen kann.",
      "topic": "Strandbar"
    },
    {
      "sentence": "Hätten wir es mal angenommen, da unser Zimmer eine Aussicht in die Hotel - Beton - Wüste hatte.",
      "topic": "Zimmer"
    },
    {
      "sentence": "Die Sauberkeit des Zimmers ist positiv zu vermerken.",
      "topic": "Sauberkeit"
    },
    {
      "sentence": "Hier hört das Lob auf.",
      "topic": "Lob"
    },
    {
      "sentence": "Bester Eintrag und richtige Positionierung der Firma bei Google Maps.",
      "topic": "Firma"
    },
    {
      "sentence": "Das scheint ein Programmfehler von Google - Maps oder so zu sein.",
      "topic": "Programmfehler"
    },
    {
      "sentence": "Ich möchte mich für die Hilfe des Teams der Mentor Coaching bedanken.",
      "topic": "Hilfe"
    },
    {
      "sentence": "2009 bin ich zu dem Unternehmen Mentor Coaching gekommen.",
      "topic": "Unternehmen"
    },
    {
      "sentence": "Jedoch wurde mir sehr schnell klar, das ich hier, genau den richtigen Partner gefunden habe.",
      "topic": "Partner"
    },
    {
      "sentence": "Alle Empfehlungen wurden mir Praxisorientiert nahe gelegt und sind genau so eingetroffen.",
      "topic": "Empfehlungen"
    },
    {
      "sentence": "Da kann ich nur noch DANKE sagen!!!",
      "topic": "DANKE"
    },
    {
      "sentence": "Wir bedanken uns nachhaltig für die kompetente Beratung des Teams der Mentor - Coaching.",
      "topic": "Beratung"
    },
    {
      "sentence": "Für Ihre Hilfe einer Existenzfestigungsberatung.",
      "topic": "Hilfe"
    },
    {
      "sentence": "Wir werden uns auch in Zukunft einer weiterführenden Beratung durch die Mentor - Coaching unterziehen und uns somit im Markt etablieren.",
      "topic": "Beratung"
    },
    {
      "sentence": "Ich kann das Team nur wärmstens weiterempfehlen.",
      "topic": "Team"
    },
    {
      "sentence": "Ich möchte mich noch mal für Ihre Leistungen bedanken.",
      "topic": "Leistungen"
    },
    {
      "sentence": "Ich wünsche Ihnen weiterhin alles gute.",
      "topic": "gute"
    },
    {
      "sentence": "Inzwischen lebt sie wesentlich selbstbestimmter und froher auch wenn es lange dauert bis sie regeneriert.",
      "topic": "sie"
    },
    {
      "sentence": "Dabei hatte ich dem Polizisten erklärt, dass der Fahrradfahrer der Autofahrerin die Vorfahrt genommen hat.",
      "topic": "Polizisten"
    },
    {
      "sentence": "Der Polizist teilte mir mit, dass er die Situation durchaus selber beurteilen kann, was mich sehr verwunderte, er war ja nicht dabei.",
      "topic": "Polizist"
    },
    {
      "sentence": "Danach wurden unsere Personalien aufgenommen.",
      "topic": "Personalien"
    },
    {
      "sentence": "Ich komme ursprünglich aus Kasachstan.",
      "topic": "Kasachstan"
    }]


          
          
            

      
      

















save_file = open("UD_german_data.json", "w", encoding='utf-8')  
json.dump(data_UD, save_file)  
save_file.close() 



#exit()


#print(gpt_to_list_for_hug_format(data))




    





