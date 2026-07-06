from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2174ff3d-db2d-5c1b-b463-d4000d47b760",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StonjournerV.Name",
    display_name="Stonjourner V",
    searchable_by=["Stonjourner V", "Basic", "V", "StonjournerV"],
    subtypes=["Basic", "V"],
    collector_number=193,
    set_code="SWSH1",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=874,
    abilities=[
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Mega Kick",
            cost={PokemonTypes.FIGHTING: 3},
            damage=150,
        ),
    ],
)