from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="50374220-b966-5236-9452-92bc151d71a1",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MawileVSTAR.Name",
    display_name="Mawile VSTAR",
    searchable_by=["Mawile VSTAR", "VSTAR", "MawileVSTAR"],
    subtypes=["VSTAR"],
    collector_number=200,
    set_code="SWSH12",
    rarity=Rarities.RareRainbow,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MawileV.Name",
    family_id=303,
    abilities=[
        Ability(
            title="Star Rondo",
            game_text="During your turn, if this Pok\u00e9mon is on your Bench, you may switch it with your Active Pok\u00e9mon. If you do, switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Sudden Eater",
            game_text="If this Pok\u00e9mon moved from your Bench to the Active Spot this turn, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)