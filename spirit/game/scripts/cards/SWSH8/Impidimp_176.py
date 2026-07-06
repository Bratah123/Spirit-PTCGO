from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7a75dcf2-6fa1-523f-bdaf-fe50cc34bf32",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Impidimp.Name",
    display_name="Impidimp",
    searchable_by=["Impidimp", "Basic", "Single Strike", "Impidimp"],
    subtypes=["Basic", "Single Strike"],
    collector_number=176,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=859,
    abilities=[
        Attack(
            title="Play Rough",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)