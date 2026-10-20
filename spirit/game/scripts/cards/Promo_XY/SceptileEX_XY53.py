from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="f8990f83-4b1d-579d-92b3-b6a010157d53",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SceptileEX.Name",
    display_name="Sceptile-EX",
    searchable_by=["Sceptile-EX", "Basic", "EX", "SceptileEX"],
    subtypes=["Basic", "EX"],
    collector_number=53,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=254,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Strong Slash",
            game_text="This Pok\u00e9mon can't use Strong Slash during your next turn.",
            cost={PokemonTypes.GRASS: 3},
            damage=130,
            effect=None,
            locks_next_turn=True,
        ),
    ],
)