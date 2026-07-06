from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="44d1a4de-d325-5bf3-ab01-a81510979fff",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZapdos.Name",
    display_name="Galarian Zapdos",
    searchable_by=["Galarian Zapdos", "Basic", "GalarianZapdos"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=145,
    abilities=[
        Ability(
            title="Strong Legs Charge",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may attach up to 2 Fighting Energy cards from your hand to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Zapper Kick",
            game_text="You may discard all Energy from this Pok\u00e9mon. If you do, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)