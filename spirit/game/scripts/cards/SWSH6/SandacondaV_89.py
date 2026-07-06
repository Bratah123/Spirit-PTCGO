from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b81ff529-46c1-5666-9904-b326fa3ca0ef",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SandacondaV.Name",
    display_name="Sandaconda V",
    searchable_by=["Sandaconda V", "Basic", "V", "SandacondaV"],
    subtypes=["Basic", "V"],
    collector_number=89,
    set_code="SWSH6",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=844,
    abilities=[
        Ability(
            title="Wall of Sand",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Land Crush",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)