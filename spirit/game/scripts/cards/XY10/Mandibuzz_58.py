from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for


def _has_ability(p):
    return any(not isinstance(a, Attack) for a in (getattr(def_for(p.archetype_id), "abilities", None) or []))


async def _bone_drop(ctx):
    """60 to 1 of your opponent's Pokemon that has an Ability."""
    pool = [p for p in ctx.opponent_pokemon_in_play() if _has_ability(p)]
    if pool:
        target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Choose a Pokémon with an Ability")
        if target is not None:
            await ctx.deal_damage(60, target=target)


card = PokemonCardDef(
    guid="cb965dbe-39e1-522e-b9fc-b2ff67b6863d",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name",
    display_name="Mandibuzz",
    searchable_by=["Mandibuzz", "Stage 1", "Mandibuzz"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    family_id=629,
    abilities=[
        Attack(
            title="Bone Drop",
            game_text="This attack does 60 damage to 1 of your opponent's Pok\u00e9mon that has an Ability. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_bone_drop,
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)