from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2e5d208b-d544-51df-9508-5c784a705da5",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LandorusEX.Name",
    display_name="Landorus-EX",
    searchable_by=["Landorus-EX", "Basic", "EX", "LandorusEX"],
    subtypes=["Basic", "EX"],
    collector_number=89,
    set_code="BW7",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=645,
    abilities=[
        Attack(
            title="Hammerhead",
            game_text="Does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Land's Judgment",
            game_text="You may discard all Fighting Energy attached to this Pok\u00e9mon. If you do, this attack does 70 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)