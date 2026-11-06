from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import damage_each_in_play_unmodified


card = PokemonCardDef(
    guid="e2055332-f46d-5d19-9ef2-1e5cbbac9d3d",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    display_name="Pupitar",
    searchable_by=["Pupitar", "Stage 1", "Pupitar"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Skull Bash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Dust Devil",
            game_text="Does 10 damage to each non-Fighting Pok\u00e9mon in play. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.FIGHTING: 2},
            effect=damage_each_in_play_unmodified(
                10, exclude_type=PokemonTypes.FIGHTING),
        ),
    ],
)
