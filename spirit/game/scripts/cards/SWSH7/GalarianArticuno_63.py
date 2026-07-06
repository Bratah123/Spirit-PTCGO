from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="013aa082-f0ea-5824-a357-4f63b661ecb9",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianArticuno.Name",
    display_name="Galarian Articuno",
    searchable_by=["Galarian Articuno", "Basic", "GalarianArticuno"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Ability(
            title="Cruel Charge",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may attach up to 2 Psychic Energy cards from your hand to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Psylaser",
            game_text="Discard all Psychic Energy from this Pok\u00e9mon. This attack does 120 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)