from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, condition_attack
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="3f1e9ab3-ed1d-5535-b82a-cdc227da419f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysGoldeen.Name",
    display_name="Misty's Goldeen",
    searchable_by=["Misty's Goldeen", "Basic", "MistysGoldeen"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=118,
    abilities=[
        Attack(
            title="Fury Attack",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=10),
        ),
        Attack(
            title="Supersonic",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
