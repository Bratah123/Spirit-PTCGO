from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c34abac5-9916-5499-afe3-3b6849265dae",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianFarfetchd.Name",
    display_name="Galarian Farfetch'd",
    searchable_by=["Galarian Farfetch'd", "Basic", "Single Strike", "GalarianFarfetchd"],
    subtypes=["Basic", "Single Strike"],
    collector_number=78,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=83,
    abilities=[
        Attack(
            title="Puncture",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)