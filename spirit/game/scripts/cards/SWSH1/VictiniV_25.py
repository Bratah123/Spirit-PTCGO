from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3b65f1a3-5299-5b0e-8a5b-524bf177645b",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VictiniV.Name",
    display_name="Victini V",
    searchable_by=["Victini V", "Basic", "V", "VictiniV"],
    subtypes=["Basic", "V"],
    collector_number=25,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="Spreading Flames",
            game_text="Attach up to 3 Fire Energy cards from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Energy Burst",
            game_text="This attack does 30 damage for each Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)