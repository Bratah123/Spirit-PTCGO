from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0e4aa482-8295-5b75-b012-daf58cb96397",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegigigasVSTAR.Name",
    display_name="Regigigas VSTAR",
    searchable_by=["Regigigas VSTAR", "VSTAR", "RegigigasVSTAR"],
    subtypes=["VSTAR"],
    collector_number=114,
    set_code="CZ",
    rarity=Rarities.RareHoloVSTAR,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RegigigasV.Name",
    family_id=486,
    abilities=[
        Ability(
            title="Star Guardian",
            game_text="During your turn, if your opponent has exactly 1 Prize card remaining, you may choose 1 of your opponent's Benched Pok\u00e9mon. They discard that Pok\u00e9mon and all attached cards. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=230,
            effect=unimplemented,
        ),
    ],
)