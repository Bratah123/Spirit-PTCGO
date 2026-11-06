from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import mega_drain
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="346e82ad-894f-57fa-85de-0a411dc06b4f",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    display_name="Oddish",
    searchable_by=["Oddish", "Basic", "Oddish"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=43,
    abilities=[
        Attack(
            title="Hide",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Oddish.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Absorb",
            game_text="Remove a number of damage counters from Oddish equal to half the damage done to the Defending Pok\u00e9mon (after applying Weakness and Resistance) (rounded up to the nearest 10). If Oddish has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            effect=mega_drain,
        ),
    ],
)
