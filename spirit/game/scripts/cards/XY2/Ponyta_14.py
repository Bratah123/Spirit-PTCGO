from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="e41b0182-0ab9-52f6-bd8e-43bf38609ded",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    display_name="Ponyta",
    searchable_by=["Ponyta", "Basic", "Ponyta"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=77,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Flame Tail",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)