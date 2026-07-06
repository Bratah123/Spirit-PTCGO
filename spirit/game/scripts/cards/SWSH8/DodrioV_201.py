from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="779dd8e1-7210-502d-b99e-71cae4a22a57",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DodrioV.Name",
    display_name="Dodrio V",
    searchable_by=["Dodrio V", "Basic", "V", "Rapid Strike", "DodrioV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=201,
    set_code="SWSH8",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=85,
    abilities=[
        Attack(
            title="No Reprieve",
            game_text="During your next turn, this Pok\u00e9mon's attacks do 80 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Rampage Drill",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=unimplemented,
        ),
    ],
)