from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn

card = PokemonCardDef(
    guid="9979e429-cad5-5a90-af2d-2460c4fb21c3",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMeowth.Name",
    display_name="Galarian Meowth",
    searchable_by=["Galarian Meowth", "Basic", "GalarianMeowth"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=52,
    abilities=[
        Attack(
            title="Hone Claws",
            game_text="During your next turn, this Pok\u00e9mon's Slash attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=boost_own_next_turn(60, attack_title="Slash"),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)