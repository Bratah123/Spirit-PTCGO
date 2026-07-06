from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b77472f2-c926-5367-b469-8e680bc0e647",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MelmetalV.Name",
    display_name="Melmetal V",
    searchable_by=["Melmetal V", "Basic", "V", "MelmetalV"],
    subtypes=["Basic", "V"],
    collector_number=47,
    set_code="PGO",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=809,
    abilities=[
        Attack(
            title="Arm Charge",
            game_text="You may attach a Metal Energy card from your hand to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.METAL: 3},
            damage=140,
        ),
    ],
)