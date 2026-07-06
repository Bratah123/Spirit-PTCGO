from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7ede9024-e3c6-5ba6-8d74-b92b700c48fd",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinderace.Name",
    display_name="Cinderace",
    searchable_by=["Cinderace", "Stage 2", "Cinderace"],
    subtypes=["Stage 2"],
    collector_number=36,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name",
    family_id=813,
    abilities=[
        Attack(
            title="Flame Cloak",
            game_text="Attach a Fire Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Bright Flame",
            game_text="Flip a coin. If tails, discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)