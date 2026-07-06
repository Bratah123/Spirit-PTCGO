from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4f757a17-5030-540a-a571-6e2b7f2cfe88",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CopperajahV.Name",
    display_name="Copperajah V",
    searchable_by=["Copperajah V", "Basic", "V", "CopperajahV"],
    subtypes=["Basic", "V"],
    collector_number=187,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=879,
    abilities=[
        Attack(
            title="Adamantine Press",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
        Attack(
            title="Wrack Down",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)