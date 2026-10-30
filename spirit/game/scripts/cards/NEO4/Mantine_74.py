from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import giant_wave


card = PokemonCardDef(
    guid="72a75df2-3851-5d89-af74-0b24bdb25449",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name",
    display_name="Mantine",
    searchable_by=["Mantine", "Basic", "Mantine"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=226,
    abilities=[
        Attack(
            title="Giant Wave",
            game_text="Mantine can't attack during your next turn.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=giant_wave,
        ),
    ],
)
