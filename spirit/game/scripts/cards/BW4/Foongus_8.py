from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="ca5709e5-f088-500d-9d17-10e2627a0af6",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    display_name="Foongus",
    searchable_by=["Foongus", "Basic", "Foongus"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="BW4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=590,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text="Flip a coin. If heads, search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Rising Lunge",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)