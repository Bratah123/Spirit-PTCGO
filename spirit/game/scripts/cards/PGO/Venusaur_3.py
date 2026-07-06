from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="48e0438d-10e4-5279-98ed-e89ff00e9f81",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name",
    display_name="Venusaur",
    searchable_by=["Venusaur", "Stage 2", "Venusaur"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Loopy Lasso",
            game_text="Once during your turn, you may flip a coin. If heads, switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon, and the new Active Pok\u00e9mon is now Asleep and Poisoned.",
            effect=unimplemented,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
        ),
    ],
)