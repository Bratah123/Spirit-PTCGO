from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e06f7936-d07c-565d-ae63-5967b6ba2380",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VirizionV.Name",
    display_name="Virizion V",
    searchable_by=["Virizion V", "Basic", "V", "VirizionV"],
    subtypes=["Basic", "V"],
    collector_number=164,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=640,
    abilities=[
        Ability(
            title="Verdant Wind",
            game_text="Each of your Pok\u00e9mon that has any Grass Energy attached to it can't be affected by any Special Conditions. (Remove any Special Conditions affecting those Pok\u00e9mon.)",
            effect=unimplemented,
        ),
        Attack(
            title="Emerald Blade",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)