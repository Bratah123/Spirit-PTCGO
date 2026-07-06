from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="51cf594f-bd24-5bf1-9da5-7815dae5be1e",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KleavorVSTAR.Name",
    display_name="Kleavor VSTAR",
    searchable_by=["Kleavor VSTAR", "VSTAR", "KleavorVSTAR"],
    subtypes=["VSTAR"],
    collector_number=196,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    hp=270,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KleavorV.Name",
    family_id=900,
    abilities=[
        Attack(
            title="Axe Break",
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pok\u00e9mon V. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
        Attack(
            title="Rampaging Star",
            game_text="This attack does 30 damage for each Pok\u00e9mon in your discard pile. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)