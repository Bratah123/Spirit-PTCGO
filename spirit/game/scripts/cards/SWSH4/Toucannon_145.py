from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="04604f09-8442-5980-bb14-52a847738fb7",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toucannon.Name",
    display_name="Toucannon",
    searchable_by=["Toucannon", "Stage 2", "Toucannon"],
    subtypes=["Stage 2"],
    collector_number=145,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trumbeak.Name",
    family_id=731,
    abilities=[
        Attack(
            title="Energy Cutoff",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Loop Cannon",
            game_text="Put 2 Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=unimplemented,
        ),
    ],
)