from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, bonus_if, count_energy

card = PokemonCardDef(
    guid="6f965d44-d7c5-5ddb-88f0-864be98052cf",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MetagrossV.Name",
    display_name="Metagross V",
    searchable_by=["Metagross V", "Basic", "V", "Rapid Strike", "MetagrossV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=181,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=376,
    abilities=[
        Attack(
            title="Bullet Punch",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
        Attack(
            title="Synchro Hammer",
            game_text="If this Pok\u00e9mon and your opponent's Active Pok\u00e9mon have the same amount of Energy attached, this attack does 90 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=bonus_if(
                lambda ctx: count_energy("self")(ctx) == count_energy("defender")(ctx),
                90,
            ),
        ),
    ],
)