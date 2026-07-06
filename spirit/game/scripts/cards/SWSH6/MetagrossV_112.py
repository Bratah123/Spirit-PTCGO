from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="afcc4e86-e3fe-55fb-9aed-e531912c1b91",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MetagrossV.Name",
    display_name="Metagross V",
    searchable_by=["Metagross V", "Basic", "V", "Rapid Strike", "MetagrossV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=112,
    set_code="SWSH6",
    rarity=Rarities.RareHoloV,
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
            effect=unimplemented,
        ),
        Attack(
            title="Synchro Hammer",
            game_text="If this Pok\u00e9mon and your opponent's Active Pok\u00e9mon have the same amount of Energy attached, this attack does 90 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)