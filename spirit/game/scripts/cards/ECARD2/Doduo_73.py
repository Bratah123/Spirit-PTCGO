from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="038dabeb-2156-5c96-8eb0-b0cf60865be5",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    display_name="Doduo",
    searchable_by=["Doduo", "Basic", "Doduo"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=84,
    abilities=[
        Attack(
            title="Super Speed",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Doduo.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
