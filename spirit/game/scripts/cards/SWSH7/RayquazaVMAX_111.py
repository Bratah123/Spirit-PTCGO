from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e31a9323-5de3-549a-9f42-e74704534e1a",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaVMAX.Name",
    display_name="Rayquaza VMAX",
    searchable_by=["Rayquaza VMAX", "VMAX", "Rapid Strike", "RayquazaVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=111,
    set_code="SWSH7",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaV.Name",
    family_id=384,
    abilities=[
        Ability(
            title="Azure Pulse",
            game_text="Once during your turn, you may discard your hand and draw 3 cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Max Burst",
            game_text="You may discard any amount of basic Fire Energy or any amount of basic Lightning Energy from this Pok\u00e9mon. This attack does 80 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)