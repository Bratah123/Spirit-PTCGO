from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9d2ad624-8d85-5bc5-a125-72be7a1494e4",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    display_name="Doublade",
    searchable_by=["Doublade", "Stage 1", "Doublade"],
    subtypes=["Stage 1"],
    collector_number=106,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name",
    family_id=679,
    abilities=[
        Attack(
            title="Cut Down",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)