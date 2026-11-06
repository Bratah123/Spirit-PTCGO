from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="11bb17be-fbc6-55e0-862f-c85d86594bcb",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name",
    display_name="Mantine",
    searchable_by=["Mantine", "Basic", "Mantine"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=226,
    abilities=[
        Attack(
            title="Undulate",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Mantine.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
    ],
)
