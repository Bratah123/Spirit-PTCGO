from spirit.game.data_utils import DeckEntry, ThemeDeckDef


product = ThemeDeckDef(
    guid="6ade6e18-f382-42bd-a2ea-18244f23f8f4",
    key="NoSet",
    name="Water Practice",
    description="Evolve Sobble and Chewtle into powerful Water Pokemon.",
    image_name="_default_deckbox",
    theme_legal=True,
    contents=[
        DeckEntry("SWSH1/54", 4),  # Sobble
        DeckEntry("SWSH1/56", 3),  # Drizzile
        DeckEntry("SWSH1/58", 2),  # Inteleon
        DeckEntry("SWSH1/60", 4),  # Chewtle
        DeckEntry("SWSH1/61", 3),  # Drednaw
        DeckEntry("SWSH1/165", 4),  # Hop
        DeckEntry("SWSH1/178", 4),  # Professor's Research
        DeckEntry("SWSH1/164", 4),  # Great Ball
        DeckEntry("SWSH1/177", 4),  # Potion
        DeckEntry("SWSH1/183", 2),  # Switch
        DeckEntry("SWSH1/163", 2),  # Evolution Incense
        DeckEntry("SWSH1/176", 2),  # Pokemon Center Lady
        DeckEntry("Free_Energy/3", 22), # Basic Water Energies
    ],
)
