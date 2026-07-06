from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3d3731ef-4935-55e2-83e8-2f466bf5d9f1",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eiscue.Name",
    display_name="Eiscue",
    searchable_by=["Eiscue", "Basic", "Fusion Strike", "Eiscue"],
    subtypes=["Basic", "Fusion Strike"],
    collector_number=44,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=875,
    abilities=[
        Attack(
            title="Block Slider",
            game_text="This attack does 40 damage to 1 of your opponent's Pok\u00e9mon for each Fusion Strike Energy attached to all of your Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Icicle Missile",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)