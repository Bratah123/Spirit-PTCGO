from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c248dd62-7d8e-5a80-90ea-6315ac52d071",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SerperiorVSTAR.Name",
    display_name="Serperior VSTAR",
    searchable_by=["Serperior VSTAR", "VSTAR", "SerperiorVSTAR"],
    subtypes=["VSTAR"],
    collector_number=8,
    set_code="SWSH12",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VSTAR,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SerperiorV.Name",
    family_id=497,
    abilities=[
        Attack(
            title="Regal Blender",
            game_text="You may move any amount of Energy from your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=190,
            effect=unimplemented,
        ),
        Attack(
            title="Star Winder",
            game_text="This attack does 60 damage for each Energy attached to this Pok\u00e9mon. Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)