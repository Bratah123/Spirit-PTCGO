from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bb2c0ebf-f849-5ed4-9f57-de5eb87cfa8c",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NinetalesV.Name",
    display_name="Ninetales V",
    searchable_by=["Ninetales V", "Basic", "V", "NinetalesV"],
    subtypes=["Basic", "V"],
    collector_number=26,
    set_code="SWSH2",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=38,
    abilities=[
        Attack(
            title="Nine-Tailed Shapeshifter",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=unimplemented,
        ),
    ],
)