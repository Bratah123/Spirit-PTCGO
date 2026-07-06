from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b8e06064-7163-5025-a0c8-c71699c59c0d",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormeDialgaV.Name",
    display_name="Origin Forme Dialga V",
    searchable_by=["Origin Forme Dialga V", "Basic", "V", "OriginFormeDialgaV"],
    subtypes=["Basic", "V"],
    collector_number=177,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=483,
    abilities=[
        Attack(
            title="Metal Coating",
            game_text="Attach up to 2 Metal Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Temporal Rupture",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)