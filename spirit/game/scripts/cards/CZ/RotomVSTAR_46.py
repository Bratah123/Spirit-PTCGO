from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cbd69b89-554e-5b7b-96c8-bbc2d3da9271",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RotomVSTAR.Name",
    display_name="Rotom VSTAR",
    searchable_by=["Rotom VSTAR", "VSTAR", "RotomVSTAR"],
    subtypes=["VSTAR"],
    collector_number=46,
    set_code="CZ",
    rarity=Rarities.RareHoloVSTAR,
    hp=250,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VSTAR,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RotomV.Name",
    family_id=479,
    abilities=[
        Ability(
            title="Conversion Star",
            game_text="During your turn, you may use this Ability. Discard any number of cards from your hand. Then, draw that many cards. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Scrap Pulse",
            game_text="Put any number of Pok\u00e9mon Tool cards from your discard pile in the Lost Zone. This attack does 40 more damage for each card you put in the Lost Zone in this way.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)