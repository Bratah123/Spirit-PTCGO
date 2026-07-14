from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.card_effects.attacks_common import damage_per


def _is_pokemon_tool_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value,
    )


def _tool_count_in_lost_zones(ctx):
    return sum(
        1 for pid in (ctx.player_id, ctx.opponent_id)
        for c in ctx.lost_zone(pid)
        if _is_pokemon_tool_card(c)
    )


card = PokemonCardDef(
    guid="666df858-b9db-54ae-9f46-e5a334267fc2",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    display_name="Porygon2",
    searchable_by=["Porygon2", "Stage 1", "Porygon2"],
    subtypes=["Stage 1"],
    collector_number=141,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    family_id=137,
    abilities=[
        Attack(
            title="Garbage Attack",
            game_text="This attack does 20 damage for each Pokémon Tool card in the Lost Zone (both yours and your opponent's).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(_tool_count_in_lost_zones, 20),
        ),
    ],
)
