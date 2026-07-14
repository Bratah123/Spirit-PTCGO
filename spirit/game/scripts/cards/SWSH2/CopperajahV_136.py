from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="185034a7-7022-5565-9333-d8289166f437",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CopperajahV.Name",
    display_name="Copperajah V",
    searchable_by=["Copperajah V", "Basic", "V", "CopperajahV"],
    subtypes=["Basic", "V"],
    collector_number=136,
    set_code="SWSH2",
    rarity=Rarities.RareHoloV,
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
            effect=protect_next_turn(reduce=30),
        ),
        Attack(
            title="Wrack Down",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)