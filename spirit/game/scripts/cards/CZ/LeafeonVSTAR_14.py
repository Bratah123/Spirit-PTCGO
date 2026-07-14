from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1c418037-55c4-561c-b98b-acb0a20099c0",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonVSTAR.Name",
    display_name="Leafeon VSTAR",
    searchable_by=["Leafeon VSTAR", "VSTAR", "LeafeonVSTAR"],
    subtypes=["VSTAR"],
    collector_number=14,
    set_code="CZ",
    rarity=Rarities.RareHoloVSTAR,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonV.Name",
    family_id=470,
    abilities=[
        Ability(
            title="Ivy Star",
            game_text="During your turn, you may switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Leaf Guard",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=unimplemented,
        ),
    ],
)