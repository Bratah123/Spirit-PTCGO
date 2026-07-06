from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e639e595-bb1d-55a4-a0c0-b4e3dc1d153d",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DhelmiseV.Name",
    display_name="Dhelmise V",
    searchable_by=["Dhelmise V", "Basic", "V", "DhelmiseV"],
    subtypes=["Basic", "V"],
    collector_number=9,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=781,
    abilities=[
        Attack(
            title="Anchor Anger",
            game_text="If any of your Grass Pok\u00e9mon were Knocked Out by damage from an opponent's attack during their last turn, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Giga Hammer",
            game_text="During your next turn, this Pok\u00e9mon can't use Giga Hammer.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)