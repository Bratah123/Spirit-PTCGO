from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f7f1ecfb-c51a-592c-8f53-c0699cf6d49a",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PidgeotV.Name",
    display_name="Pidgeot V",
    searchable_by=["Pidgeot V", "Basic", "V", "PidgeotV"],
    subtypes=["Basic", "V"],
    collector_number=188,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=18,
    abilities=[
        Ability(
            title="Vanishing Wings",
            game_text="Once during your turn, if this Pok\u00e9mon is on your Bench, you may shuffle it and all attached cards into your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Flight Surf",
            game_text="If you have a Stadium in play, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)